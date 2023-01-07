# AI_Jarvis

AI_Jarvis_Tool is a machine-learning based conversational dialog engine build in
Python which makes it possible to generate responses based on collections of
known conversations.

## Installation

This package can be installed from [PyPi](https://pypi.org/project/AI-Jarvis/) by running:

```
pip install AI-Jarvis
```

## QNA Function
```
from AI_Jarvis import QNA
print(QNA.Questions_Answers("What is python?"))
```
## Output
> **Question:** What is python? 
> **Answer:**  Python is a programming language.  

## ChatBot Function
```
from AI_Jarvis import Brain
print(Brain.ChatBot_Brain("What is your name?"))
```
## Output
> **You:** What is your name?   
> **Jarvis:** My name is Jarvis. 

## Speak Function
```
from AI_Jatvis import Speak
Speak.Speak("Hi I Am Rishabh...!!")
```
## Output
> **Speak** Hi I Am Rishabh...!!

## Hindi And English Speech-Recognition
```
from AI_Jarvis import Listen
while True:
    print(MicExecution())
```
## Output
> **Listening...**
> **You Speak:**  Hi I am Rishabh.
> **Recognizing...**                                     
> **Speech-To-Text:** Hi I am Rishabh.
> **Listening...**                                        
> **You Speak:**  हाय मेरा नाम ऋषभ है|
> **Recognizing...**                            
> **Speech-To-Text:** Hi, My name is Rishabh.

## Clap Detector
```
from AI_Jarvis import Clap
while True:
    value=Clap.Tester()
    if "True-Mic"==value:
        print("Clap is Detected")
```
## Output
> Clap is Detected


