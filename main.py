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

        else:
            print("NOVA is active. Command Received")



