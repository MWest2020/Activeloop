import os
import dotenv

dotenv.load_dotenv()
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.2)

def translate_message():
    while True:  # Loop to keep asking the user
        prompt = "What do you need translated in French? "
        user_input = input(prompt)

        messages = [
            SystemMessage(content="You are a helpful assistant that translates English to French."),
            HumanMessage(content=user_input)
        ]

        chat(messages)
        print("That would be: " + chat(messages).content)

        more_help = input("Can I help with anything else? (Y/N) ")
        if more_help.lower() == 'N':
            print("Okay, have a great day!")
            break  # Exit the loop if the user answers 'no'

translate_message()



