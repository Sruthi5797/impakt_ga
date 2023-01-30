import streamlit as st
import networkx as nx
from process_dataset import get_dataset

def requirement_analysis():
    ra = st.radio("Analysis of req",("R12: Which requirements has to be rechecked?","R13: Which verification documents are affected?",
    "R14: Are all functions still offered by the system after the change?"))
    if ra == "R12: Which requirements has to be rechecked?":
        st.write("Requiremenets to be rechecked")
    elif ra == "R13: Which verification documents are affected?":
        st.write("Documents affected")
    elif ra == "R14: Are all functions still offered by the system after the change?":
        choosen_graph, _ = get_dataset()
        #populate graph from database
        G1 = nx.cycle_graph(6)
        G2 = nx.wheel_graph(7)
        gCompare = st.selectbox("Graph from Database",(G1, G2))
        print(gCompare)
        gEdit = nx.graph_edit_distance(choosen_graph, gCompare)
        print(gEdit)
        if gEdit == 0:
            st.write("All functions are offered")
        else:
            st.write("Changes effort needed:",gEdit)

def requirement_extension():
     re = st.radio("Extension",("How is the new requirement quantified?",
     "Is the new requirement a desired requirement or a required requirement?"))
     if re == "How is the new requirement quantified?":
        pass
     elif re == "Is the new requirement a desired requirement or a required requirement?":
        pass

def add_ons():
    ao = st.radio("Add-ons",("Consistency","Change effort","Historical data","Affected domains"))
    if ao == "Consistency":
        st.write("consistent")
    elif ao == "Change effort":
        st.write("effort")
    elif ao == "Historical data":
        st.write("hd")
    elif ao == "Affected domains":
        st.write("ad")