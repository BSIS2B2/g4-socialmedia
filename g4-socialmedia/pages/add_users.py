import streamlit as st

def add_users_page():
    st.markdown('<div class="title">➕ Add Users</div>', unsafe_allow_html=True)

    st.write("Enter multiple user names separated by commas:")
    user_input = st.text_area(
        "Example:Juan, Pedro, Jose, Antonio, Fernando" ,
        height=100
    )

    if st.button("Add User(s)", use_container_width=True):
        if not user_input.strip():
            st.warning("Please enter at least one user name.")
            return

        names = [name.strip() for name in user_input.split(",") if name.strip()]
        added, skipped = [], []

        for name in names:
            if name not in st.session_state.users:
                st.session_state.users.append(name)
                st.session_state.friendships[name] = []
                added.append(name)
            else:
                skipped.append(name)

        if added:
            st.success(f"Added userss: {', '.join(added)}")
        if skipped:
            st.info(f"Skipped (already exist): {', '.join(skipped)}")
