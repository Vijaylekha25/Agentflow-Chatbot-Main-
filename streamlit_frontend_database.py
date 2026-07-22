import time
import streamlit as st
from langgraph_databse import chatbot,retrieve_all_threads
from langchain_core.messages import HumanMessage
import uuid

# ******************Utility Function *****************************#

def generate_thread_id():
    thread_id = uuid.uuid4()
    return thread_id

def reset_chat():
    thread_id = generate_thread_id()
    st.session_state['thread_id'] = thread_id
    add_thread(st.session_state['thread_id'])
    st.session_state['message_history'] = []

def add_thread(thread_id):
    if thread_id not in st.session_state['chat_threads']:
        st.session_state['chat_threads'].append(thread_id)



def load_conversation(thread_id):
    state = chatbot.get_state(config={'configurable': {'thread_id': thread_id}})
    # Check if messages key exists in state values, return empty list if not
    return state.values.get('messages', [])


# *************************** Session Setup ****************************** #
if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

if 'thread_id' not in st.session_state:
    st.session_state['thread_id'] = generate_thread_id()

if 'chat_threads' not in st.session_state:
    st.session_state['chat_threads'] = retrieve_all_threads()

add_thread(st.session_state['thread_id'])

if 'thread_names' not in st.session_state:
    st.session_state['thread_names'] = {}


#CONFIG = {'configurable': {'thread_id': st.session_state['thread_id']}}

CONFIG = {'configurable': {'thread_id': st.session_state['thread_id']},
          'metadata': {
              'thread_id':st.session_state['thread_id']
          },
          "run_name":'chat_run',
}


# *************************** Sidebar UI ****************************** #
st.sidebar.title('LangGraph Chatbot')

if st.sidebar.button('New Chat'):
    reset_chat()

st.sidebar.header('My Conversations')

for thread_id in st.session_state['chat_threads'][::-1]:
    name = st.session_state['thread_names'].get(thread_id, str(thread_id))
    if st.sidebar.button(name):
        st.session_state['thread_id'] = thread_id
        messages = load_conversation(thread_id) or []

        temp_messages = []

        for msg in messages:
            if isinstance(msg,HumanMessage):
                role = 'user'
            else:
                role = 'assistant'
            temp_messages.append({'role':role, 'content':msg.content})

        st.session_state['message_history'] = temp_messages

# *************************** Display Previous Chat Messages *********************#
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])


# ************************ Example Message Format ******************************** #
# [{'role':'user','content':'Hi'}
# {'role':'assistant','content':'Hello'}]


# **************************************** Chat Input Box *********************************** #
user_input = st.chat_input('Type here')


# ************************************ Handle New User Input and Stream Response *************************** #
if user_input:
    # Add user message to history
    thread_id = st.session_state['thread_id']
    st.session_state['message_history'].append({'role': 'user', 'content': user_input})
    if thread_id not in st.session_state['thread_names']:
        st.session_state['thread_names'][thread_id] = user_input[:40]
    with st.chat_message('user'):
        st.text(user_input)

    # Stream assistant response and display it in real time
    with st.chat_message('assistant'):
        response_placeholder = st.empty()  # Placeholder for streaming response
        full_response = ""
        for message_chunk, metadata in chatbot.stream(
            {'messages':[HumanMessage(content=user_input)]},
            config=CONFIG,
            stream_mode='messages'
        ):
            full_response += message_chunk.content
            response_placeholder.markdown(full_response)  # Update response in place
            time.sleep(0.05)  # Slow down streaming for effect like taking .5 sec pause before generating next token.

            # Set topic name for new thread using first user message
            if thread_id not in st.session_state['thread_names'] and len(st.session_state['message_history']) == 1:
                st.session_state['thread_names'][thread_id] = user_input[:40]


    # Save assistant's full response to history
    st.session_state['message_history'].append({'role':'assistant','content':full_response})
