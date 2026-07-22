
<span style="font-size:12pt"><b>AgentFlow Chatbot</b></span>

<span style="font-size:12pt"><b>Overview</b></span>
<span style="font-size:11pt">
AgentFlow Chatbot is a professional, multi-threaded conversational AI platform built with Python, LangGraph, LangChain, and Streamlit. It is designed for advanced, context-aware interactions, supporting multiple chat sessions, persistent history, and logical topic management. The backend leverages agent graphs for reasoning and planning, while the frontend offers a modern, user-friendly interface with real-time streaming and database-backed session management.
</span>

<span style="font-size:12pt"><b>Core Concepts & Architecture</b></span>
<span style="font-size:11pt">
<b>LangGraph Agent Backend:</b>
- Utilizes LangGraph to build a stateful agent graph, with nodes and edges representing the flow of conversation and reasoning steps.
- Integrates LangChain and OpenAI for LLM-powered responses, supporting multi-turn, tool-augmented conversations.
- Implements session and thread management, allowing users to maintain multiple, persistent chat sessions.
- Supports checkpointing and restoring conversations using in-memory or database storage (SQLite).

<b>Streamlit Frontend:</b>
- Sidebar UI for managing multiple chat threads, starting new chats, and switching between topics.
- Real-time streaming of LLM responses for a natural, engaging chat experience.
- Displays full conversation history and supports logical topic naming (first user message as topic).
- Database integration for persistent thread and message storage, enabling long-term retrieval and organization.
</span>

<span style="font-size:12pt"><b>Key Features</b></span>
<span style="font-size:11pt">
- Agent-based intelligence: Flexible, modular agent workflows for reasoning, planning, and tool use.
- Multi-threaded chat: Manage multiple conversations, each with its own topic and history.
- Logical topic naming: Automatically assigns a topic name to each chat based on the first user message.
- Persistent history: Stores chat threads and messages in a database for future retrieval.
- Real-time streaming: LLM responses are streamed word-by-word for a smooth, interactive experience.
- OpenAI integration: High-quality, context-aware answers powered by OpenAI models.
- Session management: Easily switch between chats, start new sessions, and revisit previous conversations.
</span>
<span style="font-size:11pt">
- <b>LangSmith (LangChain Tracing) integration:</b> Enables advanced tracing, debugging, and experiment tracking for all LLM and agent runs via LangChain's Smith platform.
</span>

<span style="font-size:12pt"><b>Tech Stack</b></span>
<span style="font-size:11pt">
- Python 3.10
- Streamlit (frontend)
- LangGraph (agent graph backend)
- LangChain (LLM and tool integration)
- OpenAI API (LLM)
- SQLite (chat history database)
- python-dotenv (environment variable management)
</span>
<span style="font-size:11pt">
- LangSmith (LangChain Tracing) for experiment tracking and debugging
</span>

<span style="font-size:12pt"><b>Getting Started</b></span>
<span style="font-size:11pt">
1. <b>Clone this repository</b>
   <pre>
   git clone https://github.com/SM0311/agentflow-chatbot.git
   cd agentflow-chatbot
   </pre>
2. <b>Set up your Python environment</b>
   <pre>
   python -m venv venv
   .\venv\Scripts\activate
   </pre>
3. <b>Install dependencies</b>
   <pre>
   pip install -r requirements.txt
   </pre>
4. <b>Add your OpenAI API key</b>
   - Create a <code>.env</code> file in the project folder and add:
     <pre>
     OPENAI_API_KEY=your_openai_api_key
     </pre>
</span>
<span style="font-size:11pt">
5. <b>LangSmith (LangChain Tracing) setup (optional but recommended)</b>
   - To enable advanced tracing and experiment tracking, add the following to your <code>.env</code> file:
     <pre>
     LANGCHAIN_TRACING="true"
     LANGCHAIN_ENDPOINT='https://api.smith.langchain.com'
     LANGCHAIN_API_KEY='your_langsmith_api_key'
     LANGCHAIN_PROJECT='your_project_name'
     </pre>
   - Get your API key and project name from <a href="https://smith.langchain.com">smith.langchain.com</a>.
6. <b>Database setup</b>
   - The chatbot will automatically create and use a SQLite database (<code>chatbot.db</code>) for chat history.
</span>

<span style="font-size:12pt"><b>How to Use</b></span>
<span style="font-size:11pt">
1. <b>Start the chatbot</b>
   <pre>
   streamlit run app.py
   </pre>
   or for database-enabled frontend:
   <pre>
   streamlit run streamlit_frontend_database.py
   </pre>
2. <b>Open your browser</b>
   - Go to the local URL Streamlit provides (usually <code>http://localhost:8501</code>).
3. <b>Start chatting!</b>
   - Type your message and see the bot respond in real time. Use the sidebar to switch between conversations, start new chats, and view chat history.
</span>

<span style="font-size:12pt"><b>Project Structure</b></span>
<span style="font-size:11pt">
- <code>app.py</code>: Main Streamlit app for chat UI.
- <code>streamlit_frontend_database.py</code>: Streamlit frontend with database support for chat threads.
- <code>langGraph_backend.py</code>: LangGraph agent logic, state graph, and LLM integration.
- <code>langgraph_databse.py</code>: Backend/database logic for chat history and thread retrieval.
- <code>requirements.txt</code>: Python dependencies.
- <code>.gitignore</code>: Files and folders excluded from version control.
- <code>README.md</code>: Project documentation.
- <code>chatbot.db</code>: SQLite database for chat history (auto-generated).
</span>

<span style="font-size:12pt"><b>Customizing & Extending</b></span>
<span style="font-size:11pt">
- <b>Agent logic:</b> Edit <code>langGraph_backend.py</code> to change agent nodes, edges, and LLM configuration.
- <b>Database features:</b> Modify <code>langgraph_databse.py</code> and <code>streamlit_frontend_database.py</code> for advanced thread management and persistent storage.
- <b>Frontend UI:</b> Update <code>app.py</code> or <code>streamlit_frontend_database.py</code> to customize chat appearance and sidebar features.
- <b>Session/thread logic:</b> Enhance session management, topic naming, and chat retrieval as needed.
</span>
<span style="font-size:11pt">
- <b>LangSmith/Tracing:</b> For advanced debugging and experiment tracking, use the LangSmith dashboard to view traces and results of all LLM and agent runs.
</span>

<span style="font-size:12pt"><b>License</b></span>
<span style="font-size:11pt">
MIT License—free to use, modify, and share.
</span>

<span style="font-size:12pt"><b>Thanks & Credits</b></span>
<span style="font-size:11pt">
- <a href="https://github.com/langchain-ai/langgraph">LangGraph</a>
- <a href="https://github.com/langchain-ai/langchain">LangChain</a>
- <a href="https://streamlit.io/">Streamlit</a>
- <a href="https://openai.com/">OpenAI</a>
</span>

<span style="font-size:12pt"><b>Questions?</b></span>
<span style="font-size:11pt">
If you have any questions or need help, feel free to open an issue on GitHub or contact <b>SM0311</b> directly.
</span>
