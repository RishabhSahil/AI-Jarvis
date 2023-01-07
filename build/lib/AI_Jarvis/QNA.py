Intro = '''
Application Name:- Jarvis
Developer Name:- RISHABH-SAHIL 
'''
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
try:
    f = open("Data\\Api.txt", "w")
    # Write to the file
    f.write('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')

    # Close the file
    f.close()
except:
    pass

# ----------------------Modules Name----------------------
import openai
from dotenv import load_dotenv

def Questions_Answers(question,chat_log=None):
    try:
        fileopen = open("Data\\Api.txt","r")
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
    except:
        try:
            f = open("DataBase\\qna_log.txt", "w")
            # Write to the file
            f.write('')
            # Close the file
            f.close()
        except:
            pass

Questions_Answers("what is your name?")
# while True:
#     query = input(">> ")
#     replay = Questions_Answers(query)
#     print(replay)
