import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def ask_gpt(screenshot_base64, html=None, prompt="What should I click?"):
    messages = [
        {"role": "system", "content": "You are a helpful UI assistant."},
        {"role": "user", "content": prompt},
        {"role": "user", "content": {"image": {"data": screenshot_base64, "mime": "image/png"}, "html": html or ""}},
    ]
    response = openai.ChatCompletion.create(
        model="gpt-4-vision-preview",
        messages=messages,
        max_tokens=500
    )
    return response["choices"][0]["message"]["content"]
