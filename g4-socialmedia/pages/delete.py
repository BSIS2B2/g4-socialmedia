import streamlit as st

def delete_page():
    st.markdown('<div class="title">🗑️ Delete</div>', unsafe_allow_html=True)
    try:
        user = st.selectbox("Delete User", st.session_state.users)
        if st.button("Delete User(s)"):
            st.session_state.users.remove(user)
            st.session_state.friendships.pop(user)
            for f in st.session_state.friendships.values():
                if user in f:
                    f.remove(user)
            st.success(f"Deleted user: {user}")
    except Exception as e:
        st.error(f"Error deleting user: {e}")
