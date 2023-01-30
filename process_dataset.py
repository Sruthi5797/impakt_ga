import streamlit as st
from collect_data import dataPreprocessing

def get_dataset():
    
    rp_data = ['data/cooperants_v1.json','data/impakt_rl_v1.json']
    option = st.sidebar.selectbox('Choose your dataset',("cooperants","impaktv1","impaktv2"))

    if option == "cooperants":
        co_graph,co_encode = dataPreprocessing(rp_data[0])
        return co_graph, co_encode
    
    elif option == "impaktv1":
        imp_graph, imp_encode = dataPreprocessing(rp_data[1])
        return imp_graph, imp_encode

    else:
        st.write("To be updated")



