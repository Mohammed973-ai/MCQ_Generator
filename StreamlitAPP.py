import os
import json
import traceback    
import pandas as pd
# from dotenv import load_dotenv  
from src.MCQ_generator.utils import read_file,get_table_data
import streamlit as st  
from src.MCQ_generator.MCQ_generator import generate_evaluate_chain 
from src.MCQ_generator.logger import logging

# loading json file
with open("/workspaces/MCQ_Generator/response.json") as f:   
    RESPONSE_JSON =  json.load(f)  

st.title("MCQ Generator App")
# creating a form
with st.form("user inputs"):
    uploaded_file = st.file_uploader("Upload a pdf or text file ", type=["pdf", "txt"])  
    mcq_count = st.number_input("Number of MCQs", min_value=1, max_value=10)
    subject = st.text_input("Insert Subject",max_chars=50)
    tone = st.selectbox("Select Tone", ["simple", "medium", "Difficult"])
    submit_button = st.form_submit_button("Generate MCQs")

if submit_button is not None and mcq_count and subject and tone:
    with st.spinner("Generating MCQs..."):
        try:
            text = read_file(uploaded_file)
            response = generate_evaluate_chain( {"text":text,
                "number":mcq_count,
                "subject":subject,
                "tone":tone,
                "response_json":RESPONSE_JSON
                }
            )  
        except Exception as e:
            traceback.print_exception(type(e), e, e.__traceback__)  
            st.error("Error generating MCQs")
        else:
            if isinstance(response,dict):
                quiz = response.get("quiz") 
                if quiz is not None:
                    table_data = get_table_data(quiz)
                    if table_data is not None:
                        df = pd.DataFrame(table_data)
                        df.index = df.index + 1
                        st.success("MCQs generated successfully")
                        st.table(df)
                        st.text_area(label="Review", value=response["review"])
                    else:
                        st.error("Error in Quiz data")
            else:
                st.write(response)

       