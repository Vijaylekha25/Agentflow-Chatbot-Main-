import time
import streamlit as st
from langGraph_backend import chatbot
from langchain_core.messages import HumanMessage, SystemMessage

# st.session_state -> dict
CONFIG = {'configurable': {'thread_id': 'thread'}}

if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])

# {'role':'user','content':'Hi'}
# {'role':'assistant','content':'Hello'}

user_input = st.chat_input('Type here')

if user_input:
    # first add the message to message_history
    st.session_state['message_history'].append({'role': 'user', 'content': user_input})
    with st.chat_message('user'):
        st.text(user_input)

    with st.chat_message('assistant'):
        response_placeholder = st.empty()  # Create a placeholder for the response
        full_response = ""
        for message_chunk, metadata in chatbot.stream(
            {'messages':[HumanMessage(content=user_input)]},
            config={'configurable':{'thread_id':'thread-1'}},
            stream_mode='messages'
        ):
            full_response += message_chunk.content
            response_placeholder.markdown(full_response)  # Update the message in place
            time.sleep(0.05)  # Optional: slow down streaming for effect

    st.session_state['message_history'].append({'role':'assistant','content':full_response})
