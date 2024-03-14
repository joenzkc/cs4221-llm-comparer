from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')  # Use getenv instead of environ.get

client = OpenAI(api_key=api_key)

# Setup base prompt
base_prompt = {"role": "system", "content": "You are an SQL Expert. You are asked to write SQL queries based on the prompts given to you. Your response should be a valid SQL query."}

def generate_ai_response(prompt):
    messages = [base_prompt]
    messages.append({"role": "user", "content": prompt})
    response = client.chat.completions.create(model="gpt-3.5-turbo", messages=messages)  # Use ChatCompletion.create
    return response.choices[0].message.content
