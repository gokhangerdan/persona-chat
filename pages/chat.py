import streamlit as st
from streamlit_chat import message
import openai
import os
openai.api_key = os.environ["OPENAI_API_KEY"]

st.title("Chat with %s" %st.session_state["persona"]["name"] )

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

st.session_state["chat_input"] = st.text_input("Message:")
if st.button("Send") and st.session_state["chat_input"]:
    st.session_state["chat_history"].append({
        "role": "Elon Musk",
        "content": st.session_state["chat_input"]
    })
    with st.spinner():
        with open(st.session_state["persona"]["name"], "r", encoding="utf8") as f:
            prompt = f.read()
        prompt+="\n\n"+"\n".join([x["role"] + ": " + x["content"] for x in st.session_state["chat_history"]])
        prompt+="\n"+st.session_state["persona"]["name"]+":"
        print(prompt)
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            max_tokens=256,
            temperature=1
        )
        result = response["choices"][0]["text"]
        answer = {
            "role": st.session_state["persona"]["name"],
            "content": result
        }
        st.session_state["chat_history"].append(answer)

for i in range(len(st.session_state["chat_history"])-1, -1, -1):
    if st.session_state["chat_history"][i]["role"]=="Elon Musk":
        message(st.session_state["chat_history"][i]["content"], is_user=True, key="msg_"+str(i), logo="https://pbs.twimg.com/profile_images/1590968738358079488/IY9Gx6Ok_400x400.jpg")
    else:
        message(st.session_state["chat_history"][i]["content"], key="msg_"+str(i), logo=st.session_state["persona"]["image"])
