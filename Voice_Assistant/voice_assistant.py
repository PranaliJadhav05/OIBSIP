import datetime
import random
import os

try:
    import pyttsx3
    engine = pyttsx3.init()
    engine.setProperty("rate", 165)
    VOICE = True
except:
    VOICE = False


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def speak(text):
    print(f"\n🤖 Assistant: {text}")
    if VOICE:
        try:
            engine.say(text)
            engine.runAndWait()
        except:
            pass


def show_menu():
    print("""
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
""")


def get_time():
    return datetime.datetime.now().strftime("%I:%M %p")


def get_date():
    return datetime.datetime.now().strftime("%d %B %Y")


def tell_joke():
    jokes = [
        "Why do programmers love Python? Because it's easy to understand.",
        "Why was the computer cold? It forgot to close Windows.",
        "Debugging is like being a detective in a crime movie."
    ]
    return random.choice(jokes)


def calculator():
    try:
        exp = input("🧮 Enter calculation (e.g. 5+3): ")
        result = eval(exp)
        speak(f"The result is {result}")
    except:
        speak("Invalid calculation")


def start_assistant():
    clear_screen()
    show_menu()
    speak("Hello! I am your Python voice assistant. How can I help you?")

    while True:
        user = input("\n🧑 You: ").lower().strip()

        if user in ["hello", "hi"]:
            speak("Hello! Nice to meet you")

        elif "time" in user:
            speak(f"Current time is {get_time()}")

        elif "date" in user:
            speak(f"Today's date is {get_date()}")

        elif "joke" in user:
            speak(tell_joke())

        elif "calculate" in user:
            calculator()

        elif "your name" in user:
            speak("I am a Python based voice assistant")

        elif "help" in user:
            speak("Here are the commands you can use")
            show_menu()

        elif "clear" in user:
            clear_screen()
            show_menu()

        elif user in ["exit", "quit", "bye"]:
            speak("Thank you for using me. Goodbye!")
            break

        else:
            speak("Sorry, I did not understand that command")


if __name__ == "__main__":
    start_assistant()
