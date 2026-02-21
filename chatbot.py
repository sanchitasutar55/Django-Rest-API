import requests
import os 
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")
def get_answer(question):

    api_key = "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"

    headers = {
        "Authorization":f"Bearer {api_key}",
        "Accept":"application/json",
    }

    data = {
        "messages":[
            {
                "role": "user",
                "content": question
            }
        ],
        "model": "llama-3.3-70b-versatile"
    }

    res = requests.post("https://api.groq.com/openai/v1/chat/completions"
                        ,headers=headers
                        ,json=data) 

    print("status_code:",res.status_code)

    print("response:",res.json())

    answer=res.json()['choices'][0]['message']['content']
    return answer
print(get_answer("Explain AI"))
print(get_answer("Explain Flask"))





