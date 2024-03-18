from dotenv import load_dotenv
import os
import pandas as pd
from llama_index.core.query_engine import PandasQueryEngine
from prompts import instruction_str, new_prompt

load_dotenv()

car_data = os.path.join("data","car_prices.csv")
car_df = pd.read_csv(car_data)

car_query_eng = PandasQueryEngine(df=car_df, verbose=True, instruction_str=instruction_str)
car_query_eng.update_prompts({
    'pandas_prompt': new_prompt
})
car_query_eng.query("What was the top selling make and model car in the year 2001")

# print(car_df.head())