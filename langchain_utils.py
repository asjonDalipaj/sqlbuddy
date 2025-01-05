import os
from dotenv import load_dotenv

load_dotenv()

db_user = os.getenv("db_user")
db_password = os.getenv("db_password")
db_host = os.getenv("db_host")
db_name = os.getenv("db_name")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
LANGCHAIN_TRACING_V2 = os.getenv("LANGCHAIN_TRACING_V2")
LANGCHAIN_API_KEY = os.getenv("LANGCHAIN_API_KEY")

from langchain_community.utilities.sql_database import SQLDatabase
from langchain.chains import create_sql_query_chain
from langchain_openai import ChatOpenAI
from langchain_community.tools.sql_database.tool import QuerySQLDataBaseTool
from langchain.memory import ChatMessageHistory

from operator import itemgetter

from langchain_core.output_parsers import StrOutputParser

from langchain_core.runnables import RunnablePassthrough, RunnableLambda
from langchain_openai import ChatOpenAI


from table_details import table_chain as select_table, get_tables, get_table_details, get_parser
from prompts import final_prompt, answer_prompt

import streamlit as st
@st.cache_resource
def get_chain():
    print("Creating chain")
    db = SQLDatabase.from_uri(f"postgresql://{db_user}:{db_password}@{db_host}:5432/{db_name}")    
    llm = ChatOpenAI(model="gpt-4", temperature=0) 
    generate_query = create_sql_query_chain(llm, db,final_prompt) 
    execute_query = QuerySQLDataBaseTool(db=db)
    rephrase_answer = answer_prompt | llm | StrOutputParser()
    # chain = generate_query | execute_query
    chain = (
    RunnablePassthrough.assign(parsed_tables=select_table)
        | RunnableLambda(lambda x: {
        "table_names_to_use": get_tables(x["parsed_tables"]),
        "question": x["question"],  # Include "question" for downstream use
        "messages": x["messages"]
        })
        | RunnablePassthrough.assign(query=generate_query)
        .assign(result=itemgetter("query") | execute_query)
        | rephrase_answer
)

    return chain

def create_history(messages):
    history = ChatMessageHistory()
    for message in messages:
        if message["role"] == "user":
            history.add_user_message(message["content"])
        else:
            history.add_ai_message(message["content"])
    return history

def invoke_chain(question,messages):
    chain = get_chain()
    history = create_history(messages)
    response = chain.invoke({
        "question": question,
        "table_details": get_table_details(),
        "format_instructions": get_parser().get_format_instructions(),
        "messages":history.messages
    })
    history.add_user_message(question)
    history.add_ai_message(response)
    return response


