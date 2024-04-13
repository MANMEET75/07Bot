import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.document_loaders import DirectoryLoader
from langchain.document_loaders import PyPDFLoader
from langchain.vectorstores import Qdrant
from langchain.embeddings import GooglePalmEmbeddings
from langchain.llms import GooglePalm
from langchain_community.embeddings import HuggingFaceEmbeddings
from transformers import AutoTokenizer, AutoModelForCausalLM
# from langchain_nomic.embeddings import NomicEmbeddings

import google.generativeai as palm
from langchain.embeddings import GooglePalmEmbeddings
from langchain.llms import GooglePalm
from langchain_google_genai import GoogleGenerativeAI

os.environ['GOOGLE_API_KEY'] =  'AIzaSyCY-PL2d9WL8qTsNY6jLFT_8EBfl2ezXk4'

embeddings = GooglePalmEmbeddings()

print(embeddings)

loader = DirectoryLoader('data/', glob="**/*.pdf", show_progress=True, loader_cls=PyPDFLoader)
documents = loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
# text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
texts = text_splitter.split_documents(documents)


url = "http://localhost:6333"
qdrant = Qdrant.from_documents(
    texts,
    embeddings,
    url=url,
    prefer_grpc=False,
    collection_name="vector_db"
)

print("Vector DB Successfully Created!")