import streamlit as st
import networkx as nx
from pyvis.network import Network
import streamlit.components.v1 as components

def network_page():
    st.markdown('<div class="title">📊 Network</div>', unsafe_allow_html=True)

    G = nx.Graph()
    for u, friends in st.session_state.friendships.items():
        for f in friends:
            G.add_edge(u, f)

    net = Network(height="600px", bgcolor="#A4EDFF")
    net.from_nx(G)
    net.save_graph("network.html")

    components.html(open("network.html").read(), height=650)
