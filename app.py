import os
os.environ["OPENAI_API_KEY"] = "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"

from langchain.llms import OpenAI
import pandas as pd
from langchain.agents import create_csv_agent

df = pd.read_csv('data/knowledge-base.csv')
print(df[0:10])

csv_path = 'data/knowledge-base.csv'

csv_agent = create_csv_agent(OpenAI(temperature=0), csv_path, verbose=True)
output = csv_agent.run("Look for similiar questions in the intent column and find the answer from the response column. Here is the question: What is LSPU?")
print(output)