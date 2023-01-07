from AI_Jarvis import QNA
from AI_Jarvis import Brain

def main():
    while True:
        query=input("You:- ")
        query = query.lower()
        if "what is" in query or "how" in query:
            replay = QNA.Questions_Answers(query)
            print(replay)
        elif "bye"==query or " bye" in query or "bye " in query:
            replay = Brain.ChatBot_Brain(query)
            print(replay)
            exit()
        elif "exit"==query or "exit()"==query or "q"==query:
            exit()
        else:
            replay = Brain.ChatBot_Brain(query)
            print(replay)
main()