import streamlit as st
import networkx as nx
from process_dataset import get_dataset
import pandas as pd
def impacted_elements():
    choosen_graph, _ = get_dataset()
    ie = st.sidebar.radio("FLP elements",("affected elements",
    "affected stock","framework agreement","purchased elements"))
    if ie == "affected elements":
        #All simple paths between the nodes are computed
        #input: Source, Target, graph, cut-off
        source_node = st.selectbox("source",(choosen_graph.nodes()))
        target_node = st.selectbox("target",(choosen_graph.nodes()))
        cutoff_value = st.slider('distance', 0, 10) #change it to maximum path after loading model
        paths = nx.all_simple_paths(choosen_graph, source=source_node, target=target_node, cutoff=cutoff_value)
        st.write(list(paths))

    elif ie == "affected stock":
        st.warning("Please ensure bi-directional traceability")
        node = st.selectbox("nodes",(choosen_graph.nodes()))
        aStock = nx.node_connected_component(choosen_graph, node)
        st.write(aStock)

    elif ie == "framework agreement":
        fNode = st.text_input('')
        if st.button('Check artifact'):
            choosen_graph.has_node(fNode)
            st.write("Framework agreement found!")
        else:
            st.write("Framework agreement not found!")

    elif ie == "purchased elements":
        st.write("purchased elements")