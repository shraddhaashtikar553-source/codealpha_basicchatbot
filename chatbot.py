# CodeAlpha Python Internship
# Project: Basic Chatbot

import datetime

# Welcome message
print("================================")
print("       PYTHON CHATBOT")
print("================================")
print("Hello! Welcome to my chatbot.")
print("Type 'bye' to exit the conversation.")

# Chatbot conversation
while True:

    user_input = input("\nYou: ").lower().strip()

    if user_input in ["hello", "hi", "hey"]:
        print("Bot: Hello! How can I help you?")

    elif user_input in ["how are you", "how are you?"]:
        print("Bot: I am doing great! Thank you for asking.")

    elif user_input in ["what is your name", "what is your name?"]:
        print("Bot: I am a Python chatbot.")

    elif user_input in ["who created you", "who created you?"]:
        print("Bot: I was created using Python.")

    elif user_input in ["what can you do", "what can you do?"]:
        print("Bot: I can answer basic questions and chat with you.")

    elif user_input in ["time", "what is the time", "what time is it?"]:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print("Bot: Current time is", current_time)

    elif user_input in ["date", "what is the date", "what is today's date?"]:
        current_date = datetime.datetime.now().strftime("%d-%m-%Y")
        print("Bot: Today's date is", current_date)

    elif user_input in ["thank you", "thanks"]:
        print("Bot: You're welcome!")

    elif user_input in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand that.")
        print("Bot: Please try asking something else.")

print("\nChatbot session ended.")