from fastapi import FastAPI, File, HTTPException, UploadFile, status, responses
import uuid
import json
from fastapi.responses import JSONResponse
from starlette.responses import RedirectResponse
from pydantic import BaseModel
from starlette.requests import Request
import pandas as pd
from pandas.io.json import json_normalize
import networkx as nx
from sklearn.preprocessing import OrdinalEncoder
from os import getppid


def dataPreprocessing(output):
    #output = json.load(f)
    #processed_output = [output[k]['RelationShip'] for k in output]
    #df_encode = pd.DataFrame.from_records(processed_output[0])
    #preparing for the new version
    edge_instances = list(output.values())[4]
    edge_instances_df = pd.json_normalize(edge_instances)
    edge_instances_df["source"] = edge_instances_df["sourceId"]
    edge_instances_df["target"] = edge_instances_df["targetId"]
    df_encode = edge_instances_df
    df_encode['source'] = df_encode['source'].map(str)
    df_encode['target'] = df_encode['target'].map(str)
    df_graph = nx.from_pandas_edgelist(df_encode, "source", "target")
    density = nx.density(df_graph)
    components = nx.connected_components(df_graph)
    largest_component = max(components, key=len)
    subgraph = df_graph.subgraph(largest_component)
    diameter = nx.diameter(subgraph)
    triadic_closure = nx.transitivity(df_graph)

    dict_info = {
        "source_nodes": list(df_encode["source"].unique()),
        "target_nodes": list(df_encode["target"].unique()),
        "Number of source nodes": len(df_encode["source"].unique()),
        "Number of target nodes": len(df_encode["target"].unique()),
        "Graph Info": nx.info(df_graph),
        "Network density": density,
        #"Largest components in graph": list(largest_component),
        "Number of largest components in graph": len(largest_component),
        "Network diameter of larget component": diameter,
        "Triadic closure": triadic_closure
    }

    return dict_info


app = FastAPI()


storeFilelist = []

req_url = "http://127.0.0.1:8000/"
"""
Start the process by uploading the input json file
"""


@app.post("/")
async def create_upload_file(file: UploadFile = File(...)):
    if not file:
        raise HTTPException(status_code=404, detail="File not found")
    else:
        id = str(uuid.uuid1())
        path = str(file.filename)
        #check the parameter once in fastapi
        json_data = json.load(file.file)
        storeDict = {}
        storeDict[id] = json_data
        storeFilelist.append(storeDict)
        headers = {"Link": req_url+id}
        return JSONResponse(status_code=status.HTTP_201_CREATED, headers=headers, content={"File uploaded successfully": id})

"""
Provide id of the operation to check the status of the operation
"""


@app.get("/{id}",
         responses={
             404: {"description": "An operation for uploaded model cannot be started"},
             204: {"description": "Queried operation finished with errors"},
             202: {"description": "Operation is in progress"}, },)
async def get_status_of_id(id: str):
    decodedJSON = storeFilelist[0].get(id)
    result = dataPreprocessing(decodedJSON)
    if decodedJSON is not None:
        try:
            json.dumps(result, indent=2)
        except ValueError as e:
            return JSONResponse(status_code=204, content={"Queried operation finished with errors": id})
        headers = {"Link": req_url + id + '/download'}
        return JSONResponse(headers=headers, content={"Finished operation": id})
    elif len(result) == 0:
        return JSONResponse(status_code=202, content={"Operation in progress"})
    else:
        return JSONResponse(status_code=404, content={"An operation for uploaded model cannot be started": id})
"""
Provide id of the operation to delete the operation
"""

@app.delete("/{id}")
async def delete_id(id: str):
    for i in range(len(storeFilelist)):
        del storeFilelist[i][id]
    return {"message": "Delete operation success!"}


@app.get("/{id}/error")
async def show_error_log():
    return {"message": "Error code"}

"""
Provide id of the operation to download the result
"""

@app.get("/{id}/download")
async def download_result(id: str):
    for i in range(len(storeFilelist)):
        decodedJSON = storeFilelist[i].get(id)
        result = dataPreprocessing(decodedJSON)
    return {"result": result}
