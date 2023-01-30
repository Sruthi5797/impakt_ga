import streamlit as st
import requests, json
#populate from dataset
option = st.sidebar.selectbox('Choose your dataset',("---",'../data/cooperants_v1.json','../data/impakt_rl_v1.json'))
submitted = st.sidebar.button("GetStats")
infile = {"infile": option}
if submitted:
    dataset_name = option.split('/')[2]
    st.write("Dataset:", dataset_name)
    res = requests.post(url = "http://127.0.0.1:8000/dataPreprocessing", data= json.dumps(infile))
    res_dict = (f"{res.text}")
    st.json(res_dict)

