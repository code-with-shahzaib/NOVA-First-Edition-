wake_up_words = ("hi", "hello", "assalam-o-alaikum")
is_active = False

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
            print(
                "This Tool is created with Python Programming Language. This is the product of DreamTechX. This tool is simply used for asking current date/time and for some MATHS problem (only Addition, Subtraction, Multiplication, Division). This tool keep waiting for the wakeup call after being run when the right wakeup call received it perfrom specific function after the greeting according to the user. when user enter exit this tool then return to it's waiting state.")


        else:
            print("NOVA is active. Command Received")