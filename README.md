# gpt-llama-data

## Environment
You will need to add a .env file in the root of the project and add you OpenAI key.

    OPENAI_API_KEY=[you api key here]


## Data
There is a PDF (United_States.pdf) taken from a wiki page as well as a CSV on car sales data for a dealership. Just unzip the "archive.zip" file.

## Run main.py
In the root of the project run the main.py file.
    
    python main.py

It will prompt you to enter a prompt. By default the response is set to be "verbose" and that setting can be updated in the main.py on line 17...

    car_query_eng = PandasQueryEngine(df=car_df, verbose=True, instruction_str=instruction_str)

