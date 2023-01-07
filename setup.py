from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'AI Jarvis Tools'
LONG_DESCRIPTION = '''
This Package Features ML ChatBot, Speak, Listing, ML QNA Bot Adding New Features
'''

# Setting up
setup(
    name="AI_Jarvis",
    version=VERSION,
    author="RISHABH-SAHIL (-R-S-)",
    author_email="githubsahil4@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=["SpeechRecognition","googletrans==3.1.0a0","pyttsx3==2.90","openai==0.25.0","python-dotenv==0.21.0"],
    keywords=['AI Jarvis Tools','Rishabh Tools','Jarvis Tools','AI Jarvis', 'Jarvis 0.2', 'AI Robot Tools', 'Jarvis', 'Rishabh','Rishabh Sahil','ML Jarvis','Self learning Jarvis'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)