import streamlit as st
import networkx as nx
from process_dataset import get_dataset
import pandas as pd
from networkx.algorithms import community
# from process_dataset import import_data

def changed_requirements():
    choosen_graph, encoded = get_dataset()
    reults_dict = []
    cr = st.sidebar.radio("Focus on a changed requirement",("unfullfiled requirements",
    "priority requirements","category of affected requirements",
    "fulfilled requirements","fit with physical requirement"))

    if cr == "unfullfiled requirements":
        unReq = list(nx.isolates(choosen_graph))
        if len(unReq) == 0:
            st.write("No unfulfilled requirements found!")
        else:
            st.write(unReq) 

    elif cr == "priority requirements":
        degree_centrality = nx.degree_centrality(choosen_graph)
        closeness_centrality = nx.closeness_centrality(choosen_graph)
        betweenness_centrality = nx.betweenness_centrality(choosen_graph)

        df_degree_centrality = pd.DataFrame(data={'Degree centrality': degree_centrality})
        df_degree_centrality.sort_values(by='Degree centrality', ascending=False, inplace=True)

        reults_dict.append(df_degree_centrality)
        df_closeness_centrality = pd.DataFrame(data={'Closeness centrality': closeness_centrality})
        df_closeness_centrality.sort_values(by='Closeness centrality', ascending=False, inplace=True)
        reults_dict.append(df_closeness_centrality)
        df_betweenness_centrality = pd.DataFrame(data={'Betweenness centrality': betweenness_centrality})
        df_betweenness_centrality.sort_values(by='Betweenness centrality', ascending=False, inplace=True)
        reults_dict.append(df_betweenness_centrality)

        st.write("Based on degree...")
        st.dataframe(df_degree_centrality)

        st.write("Based on closeness...")
        st.dataframe(df_closeness_centrality)

        st.write("Based on betweenness...")
        st.dataframe(df_betweenness_centrality)

    #Need to draw conclusions on how different categories exist - delegate the work    
    elif cr == "category of affected requirements":
        categoryVar = st.sidebar.selectbox("Category",("User defined","Label propogation","Label spreading",
        "Topic modelled","Local clustering","girvan_newman"))
        
        if categoryVar == "User defined":
            st.write("User defined Categories")

        elif categoryVar == "Label propogation":
            communities_generator = community.asyn_lpa_communities(choosen_graph)
            st.write(list(communities_generator))

        elif categoryVar == "Label spreading":
            st.write("TBD")

        elif categoryVar == "Topic modelled":
            st.write("TBD")

        elif categoryVar == "Local clustering":
            local_clustering = nx.clustering(choosen_graph)
            df_local_clustering = pd.DataFrame(data={'Local clustering': local_clustering})
            df_local_clustering.sort_values(by='Local clustering', ascending=False, inplace=True)
            st.dataframe(df_local_clustering)
        elif categoryVar == "girvan_newman":
            communities_generator = community.girvan_newman(choosen_graph)
            next_level_communities = next(communities_generator)
            st.write(sorted(map(sorted, next_level_communities)))


    #Verify different types of connectedness in a graph
    elif cr == "fulfilled requirements":
        st.warning("Please ensure Bidirectional traceability")
        st.write(list(nx.connected_components(choosen_graph)))

    elif cr == "fit with physical requirement":
        st.write("physical reqs")


    



        
# changed_rquirements()