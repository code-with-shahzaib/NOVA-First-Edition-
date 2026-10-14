from datetime import datetime
from time import strftime

wake_up_words = ("hi", "hello", "assalam-o-alaikum")
help_text = """
NOVA Commands:
- time  : Show the current time
- date  : Show today's date
- math  : Perform basic calculations
- exit  : Return to waiting mode
"""
is_active = False

def get_current_time() -> str:
    """This Function is used to get current time of the system and represent it in desired format."""
    current_time = datetime.now().time()
    formatted_time = strftime("%I:%M %p")
    return formatted_time



while True:
    user_input = input("What you want to say to NOVA: ").strip().lower()

    if not is_active:
        if user_input in wake_up_words:

            if user_input == "assalam-o-alaikum":
                print("Wa Alaikum Salam Sir. How are you?")

            else:
                print("Hello Sir. How are you?")

            is_active = True

        else:
            print("NOVA waiting for the right wake-up call.")

    else:
        if user_input == "exit":
            print("Allah Hafiz Sir!")
            is_active = False

        elif user_input == "help":
            print(help_text)

        elif user_input == "time":
            print(get_current_time())
        else:
            print("I can't recognize it sir! Please type 'help' for more information.")