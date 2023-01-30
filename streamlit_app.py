# Contents of ~/my_app/streamlit_app.py
import streamlit as st
import json
import requests
from collect_data import dataPreprocessing, graph_description
from pages.changed_requirements import changed_requirements
from pages.impacted_elements import impacted_elements
from pages.cost_analysis import cost_analysis
from pages.market_analysis import market_analysis
from pages.variant_analysis import affected_variants
from pages.extended_req_analysis import requirement_analysis, requirement_extension, add_ons
from PIL import Image

def main_page():
    st.markdown("# Analysis of dimensions")
    st.markdown('## Graph analysis/analytics')
    image = Image.open('data/logo.png')
    st.image(image, caption='')


def import_data():
    st.sidebar.markdown("# Import data")
    rp_data = ['data/cooperants_v1.json','data/impakt_rl_v1.json']
    option = st.sidebar.selectbox('Choose your dataset',("cooperants","impaktv1","impaktv2"))

    if option == "cooperants":
        co_graph,co_encode = dataPreprocessing(rp_data[0])
        co_result = graph_description(co_graph, co_encode)
        st.write(co_result)
    
    elif option == "impaktv1":
        imp_graph, imp_encode = dataPreprocessing(rp_data[1])
        imp_result = graph_description(imp_graph, imp_encode)
        st.write(imp_result)
    
    else:
        st.write("To be updated")

def dimensions():
    option = st.selectbox('Choose your category',("default","changed_requirement","impacted_elements","requirement_analysis",
    "requirement verification","requirement functions","requirement extension","add-ons","affected variants",
    "market analysis","cost analysis"))
    
    if option == "changed_requirement":
        changed_requirements()
        # opr = st.selectbox("opr",("one","two"))
        # x = st.selectbox("x",(5,10))
        # y = st.selectbox("y",(10,15))
        # inputs = {"opr":opr,"x":x,"y":y}
        # if st.button("Cal"):
        #     res1 = requests.post(url="http://127.0.0.1:8000/cost_analyse", data=json.dumps(inputs))
        #     st.subheader(f"response = {res1.text}")
    elif option == "impacted_elements":
        impacted_elements()
    elif option == "requirement_analysis":
        requirement_analysis()
    elif option == "requirement extension":
        requirement_extension()
    elif option == "add-ons":
        add_ons()
    elif option == "affected variants":
        affected_variants()
    elif option == "market analysis":
        market_analysis()
    elif option == "cost analysis":
        cost_analysis()
    
page_names_to_funcs = {
    "Main Page": main_page,
    "Dimensions": dimensions,
    "Cost analysis": cost_analysis,
    "graph description": import_data
}

selected_page = st.sidebar.selectbox(
    "Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()

