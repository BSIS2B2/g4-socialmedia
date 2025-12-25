import streamlit as st
from pathlib import Path
from core.data import init_state

from pages.home import home_page
from pages.recommend import recommend_page
from pages.add_users import add_users_page
from pages.add_friendship import add_friendship_page
from pages.mutual_friends import mutual_friends_page
from pages.delete import delete_page
from pages.network import network_page


# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Friend Recommendation System",
    page_icon="👥",
    layout="wide"
)

# --------------------------------------------------
# LOAD CSS
# --------------------------------------------------
css_path = Path(__file__).parent / "assets" / "style.css"
if css_path.exists():
    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --------------------------------------------------
# INIT SESSION STATE (IMPORTANT)
# --------------------------------------------------
init_state()

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------
menu_items = [
    "🏠 Home",
    "🔍 Recommend Friends",
    "➕ Add Users",
    "🔗 Add Friendship",
    "🤝 Mutual Friend Table",
    "🗑️ Delete Users / Friendships",
    "📊 View Network"
]

with st.sidebar:
    st.markdown("<h2>Menu</h2>", unsafe_allow_html=True)
    page = st.radio("Navigation", menu_items, label_visibility="collapsed")

# --------------------------------------------------
# ROUTER
# --------------------------------------------------
st.markdown('<div class="main-content">', unsafe_allow_html=True)

if page == "🏠 Home":
    home_page()

elif page == "🔍 Recommend Friends":
    recommend_page()

elif page == "➕ Add Users":
    add_users_page()

elif page == "🔗 Add Friendship":
    add_friendship_page()

elif page == "🤝 Mutual Friend Table":
    mutual_friends_page()

elif page == "🗑️ Delete Users / Friendships":
    delete_page()

elif page == "📊 View Network":
    network_page()

st.markdown("</div>", unsafe_allow_html=True)
