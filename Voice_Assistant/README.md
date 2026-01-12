# 🤖 Python Voice Assistant

This project is a Python-based Voice Assistant developed as part of an internship task.
It interacts with users through text commands and provides smart responses such as time, date, jokes, and basic calculations.
Voice output is optional and depends on system Text-to-Speech (TTS) support.

--------------------------------------------------

## Project Overview

The Python Voice Assistant is a command-line application designed to demonstrate:
- Python programming fundamentals
- Logical thinking and problem-solving
- Clean and modular code structure
- User interaction handling

The project works perfectly in text mode on all systems and optionally supports voice output.

--------------------------------------------------

## Features

- Interactive command-line interface
- Responds to user commands in real time
- Displays current time and date
- Tells jokes
- Performs basic calculations
- Menu-driven and easy to use
- Optional voice output
- Clean and beginner-friendly code

--------------------------------------------------

## Technologies Used

- Python 3.11
- datetime module
- random module
- os module
- pyttsx3 (optional – for voice output)

--------------------------------------------------

## Project Structure

Voice_Assistant
 ├── voice_assistant.py
 └── README.md

--------------------------------------------------

## How to Run the Project

1. Install Python 3.11 or above
2. Open Command Prompt (CMD)
3. Navigate to the project folder
4. Run the command:

python voice_assistant.py

--------------------------------------------------

## Supported Commands

hello  
time  
date  
joke  
calculate  
your name  
help  
clear  
exit  

--------------------------------------------------

## Sample Interaction

====================================
        PYTHON VOICE ASSISTANT
====================================
Commands you can try:
• hello
• time
• date
• joke
• calculate
• your name
• help
• clear
• exit
====================================


🤖 Assistant: Hello! I am your Python voice assistant. How can I help you?

🧑 You: hello

🤖 Assistant: Hello! Nice to meet you

🧑 You: time

🤖 Assistant: Current time is 01:58 PM

🧑 You: date

🤖 Assistant: Today's date is 12 January 2026

🧑 You: calculate
🧮 Enter calculation (e.g. 5+3): 76+4

🤖 Assistant: The result is 80

🧑 You: calculate
🧮 Enter calculation (e.g. 5+3): 87*7

🤖 Assistant: The result is 609

🧑 You: your name

🤖 Assistant: I am a Python based voice assistant

🧑 You: help

🤖 Assistant: Here are the commands you can use

====================================
        PYTHON VOICE ASSISTANT
====================================
Commands you can try:
• hello
• time
• date
• joke
• calculate
• your name
• help
• clear
• exit
====================================


🧑 You: exit

🤖 Assistant: Thank you for using me. Goodbye!

C:\Users\pranali\Desktop\OIBSIP\Voice_Assistant>

--------------------------------------------------

## Note on Voice Output

Voice output depends on system Text-to-Speech availability.
If voice is not supported, the assistant will still work perfectly using text-based responses.

--------------------------------------------------
