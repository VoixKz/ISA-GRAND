from django.http import JsonResponse
import requests
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

available = ['general', 'medicine', 'it', 'business', 'law', 'science', 'art', 'engineering', 'agronomy', 'metallurgy', 'oilchemistry', 'vet', 'services', 'carmanufactory', 'mining']

def askChatGPT(userInterests: str, general: str):
    chat_completion = client.chat.completions.create(
        model="gpt-4o",
        max_tokens=800,
        temperature=0.2,
        messages=[
            {
                "role": "system",
                "content": "Пользователь введет две строки. Одна - где есть темы по стандарту, вторая - собственные. Нужно отобрать из стандартных тем те, которые очень схожи с собсвтенными. Выбери наилучший вариант"
            },
            {
                "role": "user",
                "content": f"{general}\n{userInterests}"
            }
        ],
    )
    return chat_completion.choices[0].message.content.strip()

def external_api_view(search: str):
    response = requests.get(f'http://127.0.0.1:8000/call_newsogus') # "News API connection here"
    if response.status_code == 200:
        data = list(response.json()[search])
        return JsonResponse(data, safe=False)
    return JsonResponse({'error': f'Failed to retrieve data {response.json()}'}, status=response.status_code)