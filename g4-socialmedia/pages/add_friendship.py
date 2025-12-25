import streamlit as st

def add_friendship_page():
    st.markdown('<div class="title">🔗 Add Friendship</div>', unsafe_allow_html=True)

    users = st.session_state.users
    friendships = st.session_state.friendships

    disabled = len(users) < 2

    if disabled:
        st.warning("Need at least two users to add a friendship.")

    u1 = st.selectbox("User 1", users)
    u2 = st.selectbox(
        "User 2",
        [u for u in users if u != u1] if users else []
    )

    if st.button("Add Friendship", use_container_width=True, disabled=disabled):
        if u2 in friendships[u1]:
            st.info("Friendship already exists.")
        else:
            friendships[u1].append(u2)
            friendships[u2].append(u1)
            st.success(f"Friendship added between {u1} and {u2}!")
