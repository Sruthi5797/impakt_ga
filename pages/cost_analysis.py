import streamlit as st
import networkx as nx
from process_dataset import get_dataset
import pandas as pd
from networkx.algorithms import community
def cost_analysis():
    choosen_graph, _ = get_dataset()
    ca = st.radio("cost analysis",("cost effort","cost allocation","cost add-on analysis"))
    if ca == "cost effort":
        ce = st.radio("ce",("How high are the costs","fit with offered price","Profitability of the system"))
        if ce == "How high are the costs":
            flowCost, flowDict = nx.network_simplex(choosen_graph)
            st.write("flow cost:",flowCost)
            st.write("flow dict:",flowDict)
        elif ce == "fit with offered price":
            pass
        elif ce == "Profitability of the system":
            pass
    elif ca == "cost allocation":
        cal = st.radio("ca",("covered costs","costs passed on to customer","biggest internal cost drivers","functional cost","volume of ECR"))
        if cal == "covered costs":
            pass
        elif cal == "costs passed on to customer":
            pass
        elif cal == "biggest internal cost drivers":
            pass
        elif cal == "functional cost":
            pass
        elif cal == "volume of ECR":
            pass
    elif ca == "cost add-on analysis":
        caa = st.radio("caa",("most economical solution","most economical variant","solution within budget",
        "Suggested ECO"))

        if caa == "most economical solution":
            pass
        elif caa == "most economical variant":
            pass
        elif caa == "solution within budget":
            pass
        elif caa == "Suggested ECO":
            pass
