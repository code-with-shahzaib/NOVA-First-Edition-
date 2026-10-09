wake_up_words = ("hi", "hello", "assalam-o-alaikum")
is_active = False


while True:
    user_input = input("What you want to say to NOVA: ").strip().lower()

    if user_input in wake_up_words:

        if user_input == "assalam-o-alaikum":
            print("Wa alaikum salam sir. How are you?")

        else:
            print("Hello, Sir. How are you?")

    else:
        print("I'm waiting for the right wake-up call.....")

