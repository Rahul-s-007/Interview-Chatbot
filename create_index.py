#------------------------------------
# pytesseract
# pdf2image

import openai
import pinecone

import os
from dotenv import load_dotenv
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_ENVIRONMENT_NAME = os.getenv("PINECONE_ENVIRONMENT_NAME")

# openai.api_key = OPENAI_API_KEY # for open ai
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY # for lang chain

pinecone.init(
    api_key=PINECONE_API_KEY,  # find at app.pinecone.io
    environment=PINECONE_ENVIRONMENT_NAME  # next to api key in console
)

#------------------------------------
from langchain.document_loaders import UnstructuredFileLoader

loader = UnstructuredFileLoader("dataset\Customer service representative.txt")
pages = loader.load_and_split()

from langchain.text_splitter import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap  = 200,
    length_function = len,
)

docs = text_splitter.split_documents(pages)

from langchain.embeddings.openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings()

from langchain.vectorstores import Pinecone

index_name = "customer-service-representative"

#create a new index
docsearch = Pinecone.from_documents(docs, embeddings, index_name=index_name)
print("Index created:",index_name)
