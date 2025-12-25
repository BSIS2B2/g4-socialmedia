import streamlit as st

def recommend_friends(user):
    friends = st.session_state.friendships
    direct = set(friends.get(user, []))
    recs = {}

    for candidate in st.session_state.users:
        if candidate != user and candidate not in direct:
            mutual = set(friends.get(candidate, [])).intersection(direct)
            recs[candidate] = len(mutual)

    return sorted(recs.items(), key=lambda x: (-x[1], x[0]))

def mutual_friends(u1, u2):
    return list(
        set(st.session_state.friendships.get(u1, [])) &
        set(st.session_state.friendships.get(u2, []))
    )
