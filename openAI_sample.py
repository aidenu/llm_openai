import openai
import os

os.environ["OPENAI_API_KEY"] = "{OPEN_AI_KEY}" 

def chatGpt(openai) :
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Who won the world series in 2020?"},
            {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
            {"role": "user", "content": "Where was it played?"}
        ]
    )

    return response.choices[0].message.content


if __name__ == '__main__' :

    result = chatGpt(openai)
    print(result)