import pandas as pd
import streamlit as st
from operator import itemgetter
from langchain.chains.openai_tools import create_extraction_chain_pydantic
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI
from langchain.output_parsers import PydanticOutputParser
from langchain_core.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
)


llm = ChatOpenAI(model="gpt-4", temperature=0) 
from typing import List

@st.cache_data
def get_table_details():
    # Read the CSV file into a DataFrame
    table_description = pd.read_csv("dvdrental_table_descriptions.csv")
    # Iterate over the DataFrame rows to create Document objects
    table_details = ""
    for index, row in table_description.iterrows():
        table_details = table_details + "Table Name:" + row['Table'] + "\n" + "Table Description:" + row['Description'] + "\n\n"

    return table_details

def get_parser():
    return PydanticOutputParser(pydantic_object=ListTable)

class Table(BaseModel):
    """Table in SQL database."""

    name: str = Field(description="Name of table in SQL database.")

class ListTable(BaseModel):
    tables: List[Table] = Field(description="List of tables in the database.")

def get_tables(parsed_tables: ListTable) -> List[str]:
    return [table.name for table in parsed_tables.tables]


# table_names = "\n".join(db.get_usable_table_names())
table_details = get_table_details()
table_details_prompt = """Return the names of all of tables that MIGHT be relevant to the user question.\
The tables are:

{table_details}
Question is: {question}
You must follow the following format instructions:
{format_instructions}
Remember to include ALL POTENTIALLY RELEVANT tables, even if you're not sure that they're needed.
"""

parser = get_parser()
system_message_prompt = SystemMessagePromptTemplate.from_template(table_details_prompt)
chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt])
table_chain = chat_prompt | llm | parser