from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()

car_data = os.path.join("data","car_prices.csv")
car_df = pd.read_csv(car_data)