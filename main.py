import streamlit as st
from streamlit_chat import message
from streamlit import session_state

st.session_state["messages"] = []
#----------------------------------------------------------------#
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain import OpenAI, VectorDBQA
from langchain.document_loaders import DirectoryLoader
# import magic
import nltk
#----------------------------------------------------------------#
import openai

import os
from dotenv import load_dotenv
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

openai.api_key = OPENAI_API_KEY # for open ai
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY # for lang chain
#----------------------------------------------------------------#
st.set_page_config(page_icon=":computer:", layout = "wide")
st.write("<div style='text-align: center'><h1><em style='text-align: center; color:#00FFFF;'>Interview Practice</em></h1></div>", unsafe_allow_html=True)
#----------------------------------------------------------------#
def chat():
    pass

#----------------------------------------------------------------#
def chat_software_developer():
    pass

#----------------------------------------------------------------#
def chat_sales_representative():
    pass

#----------------------------------------------------------------#
def chat_marketing_manager():
    pass

#----------------------------------------------------------------#
def chat_data_scientist():
    pass

#----------------------------------------------------------------#
def chat_human_resources_manager():
    pass

#----------------------------------------------------------------#
def chat_project_manager():
    pass

#----------------------------------------------------------------#
def chat_financial_analyst():
    pass

#----------------------------------------------------------------#
def chat_customer_service_representative():
    pass

#----------------------------------------------------------------#
def chat_graphic_designer():
    pass

#----------------------------------------------------------------#
def chat_healthcare_administrator():
    pass

#----------------------------------------------------------------#
def chat_lawyer():
    pass

#----------------------------------------------------------------#
def chat_teacher():
    pass

#----------------------------------------------------------------#
def chat_web_developer():
    pass

#----------------------------------------------------------------#
job_roles = ["Software Developer",
             "Sales Representative",
             "Marketing Manager", 
             "Data Scientist", 
             "Human Resources Manager",
             "Project Manager",
             "Financial Analyst",
             "Customer Service Representative",
             "Graphic Designer",
             "Healthcare Administrator",
             "Lawyer",
             "Teacher",
             "Web Developer"]
#----------------------------------------------------------------#
def main():
    st.sidebar.write("Choose a role to be interviewed for:")
    options = st.sidebar.radio("Select Role",job_roles,label_visibility="collapsed")
    if options == "Software Developer":
        chat_software_developer()

    if options == "Sales Representative":
        chat_sales_representative()

    if options == "Marketing Manager":
        chat_marketing_manager()
        
    if options == "Data Scientist":
        chat_data_scientist()

    if options == "Human Resources Manager":
        chat_human_resources_manager()
 
    if options == "Project Manager":
        chat_project_manager()

    if options == "Financial Analyst":
        chat_financial_analyst()

    if options == "Customer Service Representative":
        chat_customer_service_representative()

    if options == "Graphic Designer":
        chat_graphic_designer()

    if options == "Healthcare Administrator":
        chat_healthcare_administrator()
        
    if options == "Lawyer":
        chat_lawyer()

    if options == "Teacher":
        chat_teacher()

    if options == "Web Developer":
        chat_web_developer()

    if st.sidebar.button("Clear Chat"):
        st.session_state["messages"] = []

#----------------------------------------------------------------#
if __name__ == "__main__":
    main()