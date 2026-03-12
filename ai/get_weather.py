import json

import requests
from openai import OpenAI

from env import ARK_API_KEY, ARK_BASE_URL

#  https://api.open-meteo.com/v1/forecast?latitude=40.7128&longitude=-74.0060&current_weather=true

client = OpenAI(
    base_url=ARK_BASE_URL,
    api_key=ARK_API_KEY,
)
model="doubao-seed-1-8-251228"


# 获取天气的函数
def get_weather(city):
    if city.lower() == "new york" or city.lower() == "纽约":
        lat = 40.7128
        lon = -74.0060
    else:
        return "Unknown city"

    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    res = requests.get(url)
    data = res.json()

    weather = data["current_weather"]
    return f"Temperature: {weather['temperature']}°C, Wind Speed: {weather['windspeed']} km/h"


# 用户问题
user_question = "纽约现在天气怎么样？"

# 调用 OpenAI
response = client.responses.create(
    model=model,
    tools=[
        {
            "type": "function",
            "name": "get_weather",
            "description": "Get current weather of a city",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {"type": "string"}
                },
                "required": ["city"]
            }
        }
    ],
    input=user_question
)

function_call = response.output[1]
city = json.loads(function_call.arguments).get('city')

# 调用真实天气 API
weather_result = get_weather(city)

print("Weather result:")
print(weather_result)