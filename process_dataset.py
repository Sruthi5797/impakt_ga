import streamlit as st
from collect_data import dataPreprocessing

def get_dataset():
    
    rp_data = ['data/cooperants_v1.json','data/impakt_rl_v1.json','data/hoffman_v1_rflp.csv']
    option = st.sidebar.selectbox('Choose your dataset',("cooperants","impaktv1","impaktv2"))

    if option == "cooperants":
        co_graph,co_encode = dataPreprocessing(rp_data[0], "json")
        return co_graph, co_encode
    
    elif option == "impaktv1":
        imp_graph, imp_encode = dataPreprocessing(rp_data[1], "json")
        return imp_graph, imp_encode

    elif option == "impaktv2":
        imp_graph_2, imp_encode_2 = dataPreprocessing(rp_data[2], "csv")
        return imp_graph_2, imp_encode_2
        



