import openai
import pinecone

import os
from dotenv import load_dotenv
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_ENVIRONMENT_NAME = os.getenv("PINECONE_ENVIRONMENT_NAME")

openai.api_key = OPENAI_API_KEY # for open ai
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY # for lang chain

pinecone.init(
    api_key=PINECONE_API_KEY,  # find at app.pinecone.io
    environment=PINECONE_ENVIRONMENT_NAME  # next to api key in console
)
# ------------------------------------------------------------------------------------
from langchain.embeddings.openai import OpenAIEmbeddings
embeddings = OpenAIEmbeddings()
from langchain.vectorstores import Pinecone

index_name = "customer-service-representative"
docsearch = Pinecone.from_existing_index(index_name, embeddings)
#----------------------------------------------------------
from langchain.chains import RetrievalQA
from langchain import OpenAI

#defining LLM
llm = OpenAI(temperature=0,max_tokens=4096)

# qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=docsearch.as_retriever(search_kwargs={"k": 2}))
qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=docsearch.as_retriever())

asked_questions = """Below are already asked questions, dont use them again:"""
prev_template = """Answer given by user for the above question is:"""
question_answer_pair = []

first_question = "What is your name?"
print(first_question)
first_ans = str(input("Enter your answer:"))

asked_questions += "\n" + first_question
prev_ans = prev_template + "\n" + first_ans
question_answer_pair.append([first_question, first_ans])

option = 0
while(option != 2):
    print("\n")
    print("1. Ask next question")
    print("2. Exit")
    option = int(input("Enter your choice: "))
    print("\n")
    if option == 1:
        query_template = f"""Give any one of the questions the Interviewer asked or cross question based on the users previous answer.
Also if user does not know the answer of a certain question move on to next question: {asked_questions} {prev_ans}"""
        
        result_1 = qa({"query": query_template})
        question = result_1['result']
        print(question)
        answer = str(input("Enter your answer: "))
        
        asked_questions += "\n" + question
        prev_ans = prev_template + "\n" + answer
        question_answer_pair.append([question, answer])
        
    if option == 2:
        report = "Below given are the questions asked by you and the answers given by the user:"
        
        for i in question_answer_pair:
            report += f"\nQuestion:{i[0]}\nAnswer:{i[1]}\n"

        report += "\nNow for each question and answer pair,give a score to on a scale of 1 to 10 for each of them based on how good the answer was and then also give suggestions on how to improve each of their answers."
        print(report)
        
        result_2 = qa({"query": report})
        suggestions_report = result_2['result']
        print("\n")
        print(f"Your report is:\n{suggestions_report}")
        print("\n")
        break