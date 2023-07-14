import os
import openai


class Service():
    def prompt(self, question):
        openai.api_key = os.environ.get('CHATGBT_TOKEN')
        response = openai.ChatCompletion.create(model='gpt-3.5-turbo', messages=[{"role": "user", "content": question}], temperature=0, max_tokens=150)
        answer = response['choices'][0]['message']['content']
        return answer
