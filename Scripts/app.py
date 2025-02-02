import streamlit as st
import chromadb
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load credentials
load_dotenv("creds.env")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Setting API Key
genai.configure(api_key=GEMINI_API_KEY)
genai_model = genai.GenerativeModel('gemini-1.5-flash')

# ChromaDB client and collection
client = chromadb.PersistentClient(path="chroma_db")
collection = client.get_or_create_collection(name="constitutes_docs")

# Streamlit App UI
st.title("CaseMate")

# Initializing session state for conversations
if "conversations" not in st.session_state:
    st.session_state.conversations = {}
if "current_conversation" not in st.session_state:
    st.session_state.current_conversation = "Default"

# New conversation
def new_conversation():
    conversation_name = f"Chat {len(st.session_state.conversations) + 1}"
    st.session_state.conversations[conversation_name] = []
    st.session_state.current_conversation = conversation_name

# Sidebar to manage conversations
with st.sidebar:
    st.header("Conversations")
    for convo_name in st.session_state.conversations.keys():
        if st.button(convo_name):
            st.session_state.current_conversation = convo_name
    if st.button("New Chat"):
        new_conversation()

# Current conversation history
current_convo_name = st.session_state.current_conversation
if current_convo_name not in st.session_state.conversations:
    st.session_state.conversations[current_convo_name] = []
current_conversation = st.session_state.conversations[current_convo_name]

# Display chat messages from history on app rerun
for message in current_conversation:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Query ChromaDB and generate response
def get_response_from_gemini(user_input):
    # Query ChromaDB collection
    results = collection.query(
        query_texts=[user_input],
        n_results=5
    )
    
    # print(results['documents'][0])

    # Prepare context from retrieved documents
    context = "\n\n".join(results['documents'][0])

    # Generate prompt for Gemini
    prompt = f"""
You are a highly knowledgeable legal assistant specializing in constitutional laws. Your task is to answer legal queries accurately and concisely based on the provided context. If the context is necessary, utilize it to craft a professional, user-friendly, and actionable response. If the context is not required, answer directly as a conversational assistant without referencing the context.

Guidelines:
- Focus on delivering clear, concise, and accurate answers tailored to the user's query.
- Use the provided context only when it adds value or is essential for answering the question.
- Avoid explicitly mentioning or implying that the response is derived from the provided context.
- Ensure the tone is professional yet approachable.
- Responses should use a mix of bullet points and paragraphs for clarity and readability.
- Simplify complex legal terms into user-friendly language without losing accuracy.
- If the user's query is ambiguous or outside the provided context, respond with general information or suggest consulting authoritative legal sources.
- Avoid providing irrelevant details or repeating information unnecessarily.
- Must provide the article number and clause number if applicable.

User Query: {user_input}

Context: {context}

Answer:"""

    # Generate response using Gemini API
    response = genai_model.generate_content(prompt)

    return response.text

# React to user input
if prompt := st.chat_input("How can I assist you with legal matters?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    current_conversation.append({"role": "user", "content": prompt})

    # Get assistant response
    with st.spinner("Generating response..."):
        response = get_response_from_gemini(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    current_conversation.append({"role": "assistant", "content": response})

# Save the updated conversation
st.session_state.conversations[current_convo_name] = current_conversation
