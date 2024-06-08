import openai
import os

# Lade den API-Schlüssel aus der .env Datei
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

def load_prompt(template_name, keywords):
    with open(f'backend/prompts/{template_name}', 'r') as file:
        prompt = file.read()
    return prompt.replace('{keywords}', keywords)

def generate_case(keywords):
    prompt = load_prompt('scenario_prompt.txt', keywords)

    response = openai.chat.completions.create(
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
        ],
        model="gpt-4o",
    )   
    return  response.choices[0].message.content.strip()