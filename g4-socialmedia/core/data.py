import streamlit as st

def init_state():
    if "users" not in st.session_state:
        st.session_state.users = []

    if "friendships" not in st.session_state:
        st.session_state.friendships = {}
