from dotenv import load_dotenv
load_dotenv()

import os
import pandas as pd
from llama_index.core.query_engine import PandasQueryEngine
from prompts import instruction_str, new_prompt, context
from note_engine import note_engine
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.agent import ReActAgent
from llama_index.llms.openai import OpenAI
from pdf import pass_car_engine
import matplotlib

car_data = os.path.join("data","car_prices.csv")
car_df = pd.read_csv(car_data)
pd.set_option('display.max_rows', None)

car_query_eng = PandasQueryEngine(df=car_df, instruction_str="Display the results as html.")
# car_query_eng = PandasQueryEngine(df=car_df, verbose=False, instruction_str=instruction_str, synthesize_response=True)
# car_query_eng.update_prompts({
    # 'pandas_prompt': new_prompt
# })

# tools = [
#     note_engine,
#     QueryEngineTool(
#         query_engine=car_query_eng, 
#         metadata=ToolMetadata(
#             name="car_sales_data",
#             description="provides information on car sales data"
#         )
#     ),
#     QueryEngineTool(
#         query_engine=pass_car_engine, 
#         metadata=ToolMetadata(
#             name="passenger_car_data",
#             description="provides detailed information on passenger cars in the United States"
#         )
#     )
# ]

# llm = OpenAI(model="gpt-3.5-turbo-0125")
# agent = ReActAgent.from_tools(tools, llm=llm, verbose=False, context=context)

while (prompt := input("Enter a prompt (q to quit): ")) != "q":
    try:
        result = car_query_eng.query(prompt)
    except ValueError:
        result = print("Oops! There was error with your request. Try again!")
    
    print(result)