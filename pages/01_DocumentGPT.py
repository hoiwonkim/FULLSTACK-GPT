import time
from langchain.document_loaders import UnstructuredFileLoader
from langchain.embeddings import CacheBackedEmbeddings, OpenAIEmbeddings
from langchain.storage import LocalFileStore
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores.faiss import FAISS
import streamlit as st

st.set_page_config(
    page_title="DocumentGPT",
    page_icon="📃",
)

# st.title("DocumentGPT")

# if "messages" not in st.session_state:
#     st.session_state["messages"] = []


# def send_message(message, role, save=True):
#     with st.chat_message(role):
#         st.write(message)
#     if save:
#         st.session_state["messages"].append({"message": message, "role": role}) """

# for message in st.session_state["messages"]:
#     send_message(
#         message["message"],
#         message["role"],
#         save=False,
def embed_file(file):
    file_content = file.read()
    file_path = f"./.cache/files/{file.name}"
    with open(file_path, "wb") as f:
        f.write(file_content)
    cache_dir = LocalFileStore(f"./.cache/embeddings/{file.name}")
    splitter = CharacterTextSplitter.from_tiktoken_encoder(
        separator="\n",
        chunk_size=600,
        chunk_overlap=100,
    )
    loader = UnstructuredFileLoader("./files/chapter_one.txt")
    docs = loader.load_and_split(text_splitter=splitter)
    embeddings = OpenAIEmbeddings()
    cached_embeddings = CacheBackedEmbeddings.from_bytes_store(embeddings, cache_dir)
    vectorstore = FAISS.from_documents(docs, cached_embeddings)
    retriever = vectorstore.as_retriever()
    return retriever

# message = st.chat_input("Send a message to the ai ")
st.title("DocumentGPT")

st.markdown(
    """
Welcome!
            
Use this chatbot to ask questions to an AI about your files!
"""
)

# if message:
#     send_message(message, "human")
#     time.sleep(2)
#     send_message(f"You said: {message}", "ai") 
file = st.file_uploader(
    "Upload a .txt .pdf or .docx file",
    type=["pdf", "txt", "docx"],
)

    # with st.sidebar:
    #     st.write(st.session_state)   
if file:
    retriever = embed_file(file)
    s = retriever.invoke("winston")
    s
