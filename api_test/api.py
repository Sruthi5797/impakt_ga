from fastapi import FastAPI, File, UploadFile, status, responses
import uuid, json
from typing import Union
from stats import dataPreprocessing
from fastapi.responses import JSONResponse
from starlette.responses import RedirectResponse
from pydantic import BaseModel
from starlette.requests import Request

app = FastAPI()


storeFilelist = []

req_url = "http://127.0.0.1:8000/"
"""
Start the process by uploading the input json file
"""

@app.post("/")
async def create_upload_file(file: UploadFile = File(...)):
    if not file:
        raise HTTPException(status_code=404, detail="Hero not found")
    else:
        id = str(uuid.uuid1())
        path = str(file.filename)
        #check the parameter once in fastapi
        json_data = json.load(file.file)
        storeDict = {}
        storeDict[id] = json_data
        storeFilelist.append(storeDict)
        headers = {"Link": req_url+id}
        return JSONResponse(status_code=status.HTTP_201_CREATED,headers=headers, content={"File uploaded successfully": id})

"""
Provide id of the operation to check the status of the operation
"""
@app.get("/{id}",
    responses={
        404: {"description": "An operation for uploaded model cannot be started"},
        204: {"description": "Queried operation finished with errors"},
        202: {"description": "Operation is in progress"},},)
async def get_status_of_id(id: str):
    decodedJSON = storeFilelist[0].get(id)
    result = dataPreprocessing(decodedJSON)
    
    if decodedJSON is not None:
        try:
            json.dumps(result, indent= 2)
        except ValueError as e:
            return JSONResponse(status_code=204, content={"Queried operation finished with errors": id})
        headers = {"Link": req_url + id +'/download'}
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


