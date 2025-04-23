import pandas as pd
import os
from dotenv import load_dotenv
from src.MCQ_generator.utils import read_file,get_table_data
from src.MCQ_generator.logger import logging    
## Langchain imports
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain

# load environment variables from .env file
load_dotenv()
# Set the Chatgrq API key   
my_key =  os.getenv("GROQ_API_KEY")
llm = ChatGroq(model = "llama3-70b-8192", api_key = my_key,temperature = 0.0)
# Define the prompt template   
TEMPLATE="""
Text:{text}
You are an expert MCQ maker. Given the above text, it is your job to \
create a quiz  of {number} multiple choice questions for {subject} students in {tone} tone. 
Make sure the questions are not repeated and check all the questions to be conforming the text as well.
Make sure to format your response like  RESPONSE_JSON below  and use it as a guide. \
Ensure to make {number} MCQs
### RESPONSE_JSON
{response_json}
respond only with the   quiz without saying here is the quiz or something like this
and make sure the response that the keyand values in the json like format is double quoted not single quoted 
"""
prompt = PromptTemplate(
 input_variables=["text", "number", "subject", "tone", "response_json"],
 template = TEMPLATE
)
quiz_chain=LLMChain(llm=llm, prompt=prompt, output_key="quiz", verbose=True)
TEMPLATE2="""
You are an expert english grammarian and writer. Given a Multiple Choice Quiz for {subject} students.\
You need to evaluate the complexity of the question and give a complete analysis of the quiz. Only use at max 50 words for complexity analysis. 
if the quiz is not at per with the cognitive and analytical abilities of the students,\
update the quiz questions which needs to be changed and change the tone such that it perfectly fits the student abilities
Quiz_MCQs:
{quiz}

Check from an expert English Writer of the above quiz:
"""

quiz_evaluation_prompt=PromptTemplate(input_variables=["subject", "quiz"], template=TEMPLATE2)
review_chain=LLMChain(llm=llm, prompt=quiz_evaluation_prompt, output_key="review", verbose=True)

generate_evaluate_chain=SequentialChain(chains=[quiz_chain, review_chain], input_variables=["text", "number", "subject", "tone", "response_json"],
                                        output_variables=["quiz", "review"], verbose=True)


