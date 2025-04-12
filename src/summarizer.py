# src/summarizer.py

import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# This gets set by runner.py
config = {}

def summarize_file(file_path):
    """
    Reads a file and sends it to OpenAI for summarization.
    Or returns a fake summary if mock mode is enabled.
    """
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    if config.get("mock_ai", False):
        return f"[MOCK SUMMARY] This file contains {len(content)} characters and likely relates to its filename '{os.path.basename(file_path)}'."

    prompt = f"Summarize the purpose and main functions of this code:\n\n{content}"

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes code for developers."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=300,
            temperature=0.3,
        )
        return response.choices[0].message['content']
    except Exception as e:
        print(f"⚠️ API error: {e} — returning fallback summary.")
        return f"Unable to summarize {file_path} due to API error."
