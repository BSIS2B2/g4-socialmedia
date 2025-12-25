import streamlit as st

def home_page():
    st.title("👥 Friend Recommendation System")
    st.subheader("Discover & Build Connections")
    st.divider()

    st.markdown("### 🌐 Overview")
    st.markdown("""
    **Discover and Build Connections:** Easily explore and strengthen friendships with users on the platform.
    
    **Smart Friend Recommendations:** Get personalized suggestions using our powerful friends-of-friends algorithm.

    **See Mutual Connections:** Find common friends between users and discover new ways to connect.

    **Manage Users and Friendships:** Effortlessly add, delete, and manage users and connections on the platform.
    """)
    st.image("https://media.giphy.com/media/ftAyb0CG1FNAIZt4SO/giphy.gif")
