# from src.MCQ_generator.logger import logging

# logging.info("I am working on the web")
# import json
# with open("/workspaces/MCQ_Generator/response.json") as f:
#        RESPONSE_JSON = json.load(f)
# print(RESPONSE_JSON)
from src.MCQ_generator.utils import read_file
from src.MCQ_generator.MCQ_generator import generate_evaluate_chain 
import json
import traceback
import pandas as pd 
with open("/workspaces/MCQ_Generator/response.json") as f:   
    RESPONSE_JSON =  json.load(f)
with open("/workspaces/MCQ_Generator/experiment/data.txt","r") as file : 
    text = file.read()    
response = generate_evaluate_chain( {"text":text,
                "number":5,
                "subject":"Machine Learning",
                "tone":"simple",
                "response_json":RESPONSE_JSON
                }
            ) 

# quiz = response.get("quiz")
# print(type(json.loads(quiz)))
# def get_table_data(quiz_str):
#     try:
#         # convert the quiz from a str to dict
#         quiz_dict=json.loads(quiz_str)
#         print(quiz_dict)
#         quiz_table_data=[]
        
#         # iterate over the quiz dictionary and extract the required information
#         for key,value in quiz_dict.items():
#             mcq=value["mcq"]
#             options=" || ".join(
#                 [
#                     f"{option}-> {option_value}" for option, option_value in value["options"].items()
                 
#                  ]
#             )
            
#             correct=value["correct"]
#             quiz_table_data.append({"MCQ": mcq,"Choices": options, "Correct": correct})
        
#         return quiz_table_data
        
#     except Exception as e:
#         traceback.print_exception(type(e), e, e.__traceback__)
#         return False
# table_data = get_table_data(quiz)
