import streamlit as st
def affected_variants():
    av = st.radio("Affected elements",
    ("Variants","Domains/Disciplines"))

    if av == "Variants":
        print("affected variants")

    elif av == "Domains/Disciplines":
        print("impacted domains/disciplines")