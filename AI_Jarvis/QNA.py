Intro = '''
Application Name:- Jarvis
Developer Name:- RISHABH-SAHIL 
'''

import os
try:
    # Create a folder
    os.makedirs("DataBase")
    os.makedirs("Data")
except:
    pass

# ----------------------Modules Name----------------------
import openai
from dotenv import load_dotenv

def Questions_Answers(question,chat_log=None):
    fileopen = open("Data\\Api.txt","r") #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
    API = fileopen.read()
    fileopen.close()
    openai.api_key = API
    load_dotenv()
    completion = openai.Completion()
    FileLog = open("DataBase\\qna_log.txt","r")
    chat_log_template = FileLog.read()
    FileLog.close()

    if chat_log is None:
        chat_log = chat_log_template
    
    prompt = f'{chat_log} Question : {question}\nAnswer : '
    response = completion.create(
        model = "text-davinci-002",
        prompt=prompt,
        temperature = 0,
        max_tokens = 100,
        top_p = 1,
        frequency_penalty = 0,
        presence_penalty = 0)
    answer = response.choices[0].text.strip()
    chat_log_template_update = chat_log_template + f"\nQuestion : {question} \nAnswer : {answer}"
    FileLog = open("DataBase\\qna_log.txt","w")
    FileLog.write(chat_log_template_update)
    FileLog.close()
    if "what is your name"==question:
        answer = "My name is Jarvis."
    return answer


# Questions_Answers("what is your name?")
# while True:
#     query = input(">> ")
#     replay = Questions_Answers(query)
#     print(replay)
