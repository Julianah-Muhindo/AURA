# ================================
# AURA =Adaptive Universal Resource Assistant
# Version: 0.0.1
# Author: Julianah Muhindo Alinethu 
# ================================

print("===============================")
print("                     AURA")
print("Adaptive Universal Resource Assistant")
print("Version: 0.0.1") 
print("================================") 
print("")

print("Initializing AURA...As you wait, fun fact, AURA started off as model to help the author learn python from scratch")

print("") 

print("Welcome!")

print ("AURA is now running...Enjoy your experience!")
print ("")
first_name = input("Before we proceed, may I know your first name? ")
last_name = input("And your last name? ")
name = f"{first_name} {last_name}".strip().title()

location = input("Where are you from? ")
age = int(input("How old are you? "))

future_age = age + 10

print (f"Welcome, {name} ! ")
print ("")
print ("Iam AURA.")
print ("I am an AI assistant designed to help you with your tasks and provide information.")
print (f" I see you are from {location} and you are {age} years old. I will do my best to tailor your experience according to the information received.")
print(f"First off, in 10 years, you will be {future_age} years old. I hope you are excited about the future!")
print (f"It was nice meeting you, {name} ! ") 
print ("") 

continue_choice = input("Would you like to continue using AURA? (yes/no): ").strip().lower()

if continue_choice == "yes":
    print("Great! Let's continue.")
    print("What would you like to do next?")
    print("1. Get information")
    print("2. Perform a task")  
    choice   = input("Please enter the number corresponding to your choice: ").strip()

    if choice == "1":
        print("You chose to get information.")
        information_type = input("What kind of information are you looking for? (e.g., weather, news, general knowledge): ").strip().lower()

        if information_type == "weather":
            print(f"Fetching weather information for {location}...")
            # Add code to fetch and display weather information here
        elif information_type == "news":
            print("Fetching news information...")
            # Add code to fetch and display news information here
        elif information_type == "general knowledge": 
            print("Fetching general knowledge information...")
            # Add code to fetch and display general knowledge information here
        else:
            print("I'm sorry, I don't have information on that topic.")

    elif choice == "2":
        print("You chose to perform a task.")
        task = input("What task would you like to perform? (e.g., set a reminder, calculate something, etc.): ").strip().lower()

        if task == "set a reminder":
            reminder_time = input("When would you like to set the reminder for? (e.g., in 10 minutes, at 3 PM): ").strip()
            reminder_message = input("What message would you like to be reminded of? ").strip()
            print(f"Setting a reminder for {reminder_time} with the message: '{reminder_message}'")
            # Add code to set the reminder here
        elif task == "calculate":
            calculation = input("Please enter the calculation you would like to perform (e.g., 5 + 3): ").strip()
            print(f"Performing the calculation: {calculation}")
            # Add code to perform the calculation here
        else:
            print("I'm sorry, I don't know how to perform that task.")

    # Add more functionality here as needed
else:
    print("Thank you for using AURA. I will be here whenever you need assistance.")
    print(" Have a great day!")