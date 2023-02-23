import json
import csv
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

# G2 = G.to_undirected()

# dg, dc = dataPreprocessing('data/cooperants_v1.json')
# res = graph_description(dg, dc)