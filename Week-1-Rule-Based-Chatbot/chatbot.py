from datetime import datetime 
print("=" * 50)
print("        DECODEBOT AI ASSISTANT")
print("=" * 50)

print("Bot: Hello! I am DecodeBot.")
print("Bot: Type 'help' to see available commands.")

while True:

    user = input("\nYou: ").lower().strip()

    # Greetings
    if user in ["hello", "hi", "hey"]:
        print("Bot: Hello! How can I help you?")

    # About Bot 
    elif user == "name":
        print("Bot: My name is DecodeBot.")
    
    elif user == "who created you":
        print("Bot: I was created by Kamlesh Pandey.")

    # Time
    elif user == "time":
        current_time = datetime.now().strftime("%I:%M %p")
        print(f"Bot: current Time is {current_time}")

    # Date 
    elif user == "date":
        current_date = datetime.now().strftime("%d-%m-%Y")
        print(f"Bot: Today's Date is {current_date}")

    # Joke 
    elif user == "joke":
        print("Bot: Why do programmers prefer dark mode?")
        print("Bot: Because light attracts bugs!")

    # Help
    elif user == "help":
        print("\nAvailable Commands:")
        print("hello")
        print("name")
        print("who created you")
        print("time")
        print("date")
        print("joke")
        print("help")
        print("bye")

    # Exit 
    elif user in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! Have a grate day.")
        break

    # Unknown Input
    else:
        print("Bot: Sorry, I didn't understand that.")
        print("Bot: Type 'help' to see available commands.")

        

