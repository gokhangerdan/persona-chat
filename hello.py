import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from streamlit_card import card

st.title("Select a persona to chat with:")

if 'persona' not in st.session_state:
    st.session_state['persona'] = {}

def select_persona(name, image):
    st.session_state['chat_history'] = []
    st.session_state['persona'] = {"name": name, "image": image}
    switch_page('chat')

personas = [
    {
        "title": "Geralt of Rivia",
        "image": "https://pbs.twimg.com/profile_images/1214274665427935234/OEmo0ORJ_400x400.jpg"
    },
    {
        "title": "Yoda",
        "image": "https://pbs.twimg.com/profile_images/378800000178364430/7057bd6197f8a436006ba6e4bf279564_400x400.jpeg"
    }
]

for i in personas:
    card(
        title=i["title"],
        text="",
        image=i["image"],
        on_click=lambda: select_persona(i["title"], i["image"])
    )
