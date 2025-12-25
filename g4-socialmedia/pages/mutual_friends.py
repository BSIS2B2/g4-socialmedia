import streamlit as st
import pandas as pd

def mutual_friends_page():
    st.markdown('<div class="title">🤝 Mutual Friends</div>', unsafe_allow_html=True)

    users = st.session_state.users
    friendships = st.session_state.friendships

    if len(users) < 2:
        st.warning("Need at least two users.")
        return

    u1 = st.selectbox("User 1", users)
    u2 = st.selectbox(
        "User 2",
        [u for u in users if u != u1]
    )

    mutual = sorted(set(friendships[u1]).intersection(friendships[u2]))

    if mutual:
        df = pd.DataFrame(mutual, columns=["Mutual Friends"])
        st.table(df)
    else:
        st.info("No mutual friends found.")
