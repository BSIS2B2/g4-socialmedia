import streamlit as st
from core.utils import recommend_friends

def recommend_page():
    st.markdown('<div class="title">🔍 Friend Recommendations</div>', unsafe_allow_html=True)
    if not st.session_state.users:
        st.warning("No users available.")
        return
    user = st.selectbox("Select user", st.session_state.users)
    if st.button("Generate Recommendations", use_container_width=True):
        recs = recommend_friends(user)
        for name, mutual in recs:
            st.success(f"{name} — Mutual Friends: {mutual}")
