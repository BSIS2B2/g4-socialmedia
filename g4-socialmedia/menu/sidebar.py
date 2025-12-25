import streamlit as st

def sidebar_menu():
    st.sidebar.title("⚙️ Menu")
    return st.sidebar.radio(
        "Navigate",
        [
            "🏠 Home",
            "🔍 Recommend Friends",
            "➕ Add Users",
            "🔗 Add Friendship",
            "🤝 Mutual Friend Table",
            "🗑️ Delete Users / Friendships",
            "📊 View Network"
        ]
    )
