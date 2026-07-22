from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Literal, Annotated
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage,BaseMessage
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import InMemorySaver


load_dotenv()

llm = ChatOpenAI()

class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]


def chat_node(state: ChatState):
    #take user's query from state
    messages = state['messages']
    #send to llm
    response = llm.invoke(messages)
    #response store state
    return {'messages':messages+[response]}

#checkpointer
checkpointer = InMemorySaver()

graph = StateGraph(ChatState)
#add nodes
graph.add_node('chat_node',chat_node)
#add edge
graph.add_edge(START, 'chat_node')
graph.add_edge('chat_node',END)

chatbot = graph.compile(checkpointer=checkpointer)



