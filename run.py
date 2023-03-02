import time
# Time.sleep will be used throughout the game after print statements.

# Empty list which items are added and removed from through functions.
inventory = [""]

# Starting health.
health = 100

# Starting time for clock_game
starting_time = 167


def intro():
    """
    Function for intro of the game. Input is required by the user.
    If input is "y" the game starts and if input is "n" the game quits.
    Any other input leads to demand for input from user again.
    """
    print("You wake up and open your eyes but you can't see anything")
    time.sleep(2)
    print("You stretch your arms up to your head and feel something weird.")
    time.sleep(2)
    print("A helmet of some sort is on your head.")
    time.sleep(2)
    print("You try to remove it but you can't.")
    time.sleep(2)
    print("You try to pull it of with all of your strength but it's stuck.\n")
    time.sleep(2)
    print('"... What is this... Where am I... What is going on?"\n')
    time.sleep(2)
    print('"... I do not remember anything... Not even my name..."\n')

    global answer

    answer = str.lower((input("Do you feel your way around? (y/n): \n")))

    if answer == "y":
        box_or_search()
    elif answer == "n":
        print("\nYou give up and accept your fate.")
        time.sleep(2)
        print("Days go by and you finally close your eyes and never wake up.")
        time.sleep(2)
        game_over()
    else:
        print("Incorrect input! Please answer y/n")
        intro()


def game_over():
    """
    Prints game over message to terminal and quits game.
    """
    print("YOU DIED! GAME OVER!")
    quit()


def box_or_search():
    """
    Function that leads user to different places depending on input.
    Demands user input. While loop that runs until user input is "y" or "n".
    In any other case the user will get a message,
    that tells them to input "y" or "n".
    """
    print("\nYou realize you will not get the helmet of.")
    time.sleep(2)
    print("You start using your hands to feel around.")
    time.sleep(2)
    print("Crawling around on your knees, you find what feels like a box.\n")
    time.sleep(2)
    while True:
        answer = input("Do you open the box? (y/n): \n")
        if answer == "y":
            open_box()
            break
        elif answer == "n":
            search()
            break
        else:
            print("Incorrect input! Please answer y/n")


def open_box():
    """
    Function that leads to the following buttons game.
    Print statements and then a function call.
    """

    print("The box seems to be made of metal.")
    time.sleep(2)
    print("You can feel three buttons on the top.")
    time.sleep(2)
    print("Suddenly a voice starts speaking to you from the box.\n")
    time.sleep(2)
    print('"WELCOME TO YOUR FIRST TEST."')
    time.sleep(2)
    print('"PLEASE PRESS THE BUTTONS IN THE RIGHT SEQUENCE!\n')
    time.sleep(2)
    print('"...My first test..?"')
    time.sleep(2)
    print('"...I guess I have to find the right sequence then..?"\n')
    time.sleep(2)
    buttons_game()


def search():
    """
    Function that lets the user search around the room.
    If "key" is in the inventory list the computer_scene function is called.
    If not, the user will have to provide input if they want to
    keep searching or return to the box.
    If they choose the box, the open_box function is called.
    """
    print("\nYou let go of the box and keep feeling your way through the room")
    time.sleep(2)
    print("When moving you feel that something is pulling onto the helmet")
    time.sleep(2)
    print("You touch the back of your head.")
    time.sleep(2)
    print("You can feel a small cord connected to the helmet.\n")
    time.sleep(2)
    print('..."What is this thing..?"\n')
    time.sleep(2)
    print("You keep moving around and bump into something.")
    time.sleep(2)
    print("It seems to be a desk and you can feel a bunch of wires.\n")
    time.sleep(2)
    print('"... It must be a computer..!"\n')
    time.sleep(2)
    print("Blindly feeling around, you some feel some sort of cavity.")
    time.sleep(2)
    print('"A key hole!"\n')
    time.sleep(2)

    while True:
        if "key" in inventory:
            print("You put the key in the key hole.")
            time.sleep(2)
            remove_from_inventory("key")
            print("Key was removed from your inventory\n")
            time.sleep(2)
            computer_scene()
            break
        else:
            print("You have no key.")
            time.sleep(2)
            print("Do you want to explore or go to the box?")
            time.sleep(2)
            answer = input("Explore/box): \n")

            if answer == "explore":
                print("You walk around but can't find anything but the box")
                time.sleep(2)
                answer = input("Do you want to open the box? (y/n): ")
                if answer == "y":
                    open_box()
                    break
                elif answer == "n":
                    search()
                    break

            elif answer == "box":
                open_box()
                break
            else:
                print("Incorrect input! Please answer y/n")


def add_to_inventory(item):
    """
    Adds items to inventory list.
    """
    inventory.append(item)


def remove_from_inventory(item):
    """
    Removes items to inventory list.
    """
    inventory.remove(item)


def buttons_game():
    """
    Function that gives the user 10 attempts to get the right sequence.
    If answer is wrong, attempts decreases and if this reaches 0,
    the game_over function is called and game quits.
    If the user gets the right sequence, the attempts is set to 0 to
    quit the while loop and a key is added to players inventory.
    """

    attempts_left = 10
    while attempts_left > 0:
        answer = (input("Enter the button sequence (example 123): \n"))
        if answer != "312":
            attempts_left -= 1
            print(f'"YOU HAVE {attempts_left} ATTEMPTS LEFT"')
            time.sleep(2)
        else:
            attempts_left = 0
            print("\nThe box starts to buzz and then opens with a click!")
            time.sleep(2)
            print("You carefully put your hand inside.")
            time.sleep(2)
            print("You directly recognize the shape of a key!")
            time.sleep(2)

            add_to_inventory("key")
            search()
            computer_scene()
            break

        if attempts_left == 0:
            print("A loud buzz comes from the box.")
            time.sleep(2)
            print("Followed by a slow ticking noice.")
            time.sleep(2)
            print("The ticking intensifies.")
            time.sleep(2)
            print("In a blink of an eye everything around you explodes.")

            game_over()


def computer_scene():
    """
    The user enters the computer scene.
    Requires user input for choosing one of four alternatives.
    Any other input than the four alternatives gives an error message,
    and the user must try again.


    """
    print("On the display you can see four choices\n")
    time.sleep(2)
    print("LOGIN\n"
          "INFORMATION\n"
          "PLAY\n"
          "LEAVE\n")
    time.sleep(2)
    answer = input("What do you choose? (login/information/play/leave): \n")
    if answer == "login":
        print(f"You choose {answer.upper()}")

        username = "ava"
        password = "EVILCORP"

        username_guess = input("ENTER USERNAME: \n")
        password_guess = input("ENTER PASSWORD: \n")

        if username_guess == username and password_guess.upper() == password:
            print("USERNAME: CORRECT")
            time.sleep(2)
            print("PASSWORD: CORRECT")
            time.sleep(2)
            game_ending()
        elif username_guess != username and password_guess.upper() == password:
            print("USERNAME: INCORRECT")
            time.sleep(2)
            print("PASSWORD: CORRECT")
            time.sleep(2)
        elif username_guess == username and password_guess.upper() != password:
            print("USERNAME: CORRECT")
            time.sleep(2)
            print("PASSWORD: INCORRECT")
            time.sleep(2)
            print("A small hatch opens")
            time.sleep(2)
            print("There is something inside.")
            time.sleep(2)
            print('"...An access card..!"')
            time.sleep(2)
            global access_card
            access_card = {"name": "Ava",
                           "age": "27",
                           "profession": "research scientist"}
            add_to_inventory(access_card)
            print("\nThe access card was added to your inventory.\n")
            time.sleep(2)
            print("At the top of the card there is a picture.")
            time.sleep(2)
            print('\n"...That is... me..."\n')
            time.sleep(2)
            print("You look at the information on the card.\n")
            time.sleep(2)
            for key, value in access_card.items():
                print(key, ' : ', value)
            print('"...My name is... Ava and I am a scientist."')
            time.sleep(2)
            print("Interrupting your thoughts, a door suddenly appears.")
            time.sleep(2)
            computer_scene()
        else:
            print("USERNAME: INCORRECT")
            time.sleep(2)
            print("PASSWORD: INCORRECT")
            time.sleep(2)

    elif answer == "information":
        print("\nYOU HAVE BEEN PUT HERE TO BE TESTED.")
        time.sleep(2)
        print("THE TESTS WILL BE HARD AND CHALLENGING.")
        time.sleep(2)
        print("SOME TESTS MIGHT KILL YOU AT ONCE.")
        time.sleep(2)
        print("SOME TESTS MIGHT JUST HARM YOU.")
        time.sleep(2)
        print("FINAL TEST WILL BE GIVEN WHEN LOGGED IN.\n")
        time.sleep(2)
        print("A sharp pain shoots through your head")
        time.sleep(2)
        print("Some sort of electric chock buzz you through the helmet\n")
        time.sleep(2)
        decrease_health()
        computer_scene()

    elif answer == "play":
        play = True
        while play:
            print("\nYOU CHOSE PLAY, WELCOME TO THE GAME")
            time.sleep(2)
            print("YOU WILL BE ASKED THREE RIDDLES.")
            time.sleep(2)
            print("ANSWER WISELY\n")
            time.sleep(2)
            question_1 = "candle"
            print(" I'M TALL WHEN I'm YOUNG, AND I'M SHORT WHEN I'M OLD.")
            time.sleep(2)
            question_1_guess = input(" WHAT AM I? (candle/mountain/glass): \n")
            if question_1 == question_1_guess:
                print("CORRECT! ANSWER: A candle")
                time.sleep(2)
            elif question_1 == "mountain" or "glass":
                print("INCORRECT!")
                time.sleep(2)
                print("You feel a sharp pain.")
                time.sleep(2)
                decrease_health()
            else:
                print("INCORRECT INPUT")
                time.sleep(2)
                print("You feel a sharp pain.")
                time.sleep(2)
                decrease_health()

            question_2 = "verb"
            print(" I RUN, I WALK, I TALK.")
            time.sleep(2)
            question_2_guess = input("WHAT AM I? (child/verb/ghost): \n")
            if question_2 == question_2_guess:
                print("CORRECT! ANSWER: V erb")
            elif question_2 == "child" or "ghost":
                print("INCORRECT!")
                time.sleep(2)
                print("You feel a sharp pain.")
                time.sleep(2)
                decrease_health()
            else:
                print("INCORRECT INPUT")
                time.sleep(2)
                print("You feel a sharp pain.")
                time.sleep(2)
                decrease_health()

            question_3 = "echo"
            print("WHAT CAN'T TALK BUT WILL REPLY WHEN SPOKEN TO?")
            question_3_guess = input("(echo/mute/scream): \n")
            if question_3 == question_3_guess:
                print("CORRECT! ANSWER: A n echo")
                time.sleep(2)
            elif question_3 == "mute" or "scream":
                print("INCORRECT!")
                time.sleep(2)
                print("You feel a sharp pain.")
                time.sleep(2)
                decrease_health()
            else:
                print("INCORRECT INPUT")
                time.sleep(2)
                print("You feel a sharp pain.")
                time.sleep(2)
                decrease_health()

            if question_1 == question_1_guess and question_2 == question_2_guess and question_3 == question_3_guess:
                print("\nALL RIDDLES WAS ANSWERED CORRECTLY.")
                time.sleep(2)
                print("A small note is printed.")
                time.sleep(2)
                print("On it it says:\n")
                time.sleep(2)
                print(" A candle")
                print("V erb")
                print("A n echo")
                time.sleep(2)
                print('"Hmm... A, V, A... AVA...?"')
                time.sleep(2)
                computer_scene()
                break

            else:
                print("\nONE OR MORE INCORRECT ANSWERS, TRY AGAIN\n")
                time.sleep(2)
    elif answer == "leave":
        if access_card in inventory:
            print("You go over to the door.")
            time.sleep(2)
            print("You put the access card to the monitor.")
            time.sleep(2)
            print("The door opens!\n")
            time.sleep(2)
            print("You go through the door.\n")
            time.sleep(2)
            time_room()
        elif access_card not in inventory:
            print("\nYou walk away from the computer.")
            time.sleep(2)
            print("You realize you have to do something more with it.")
            time.sleep(2)
            print("You go back\n")
            time.sleep(2)
            computer_scene()

        else:
            print("\nYou walk away from the computer.")
            time.sleep(2)
            print("You realize you have to do something more with it.")
            time.sleep(2)
            print("You go back\n")
            time.sleep(2)
            computer_scene()


def decrease_health():
    """
    Decreases player health. Prints the health to the terminal.
    If health reaches 0 the game_over function is called.
    """
    global health
    health -= 10
    print(f"Your health: {health}\n")
    time.sleep(2)

    if health == 0:
        print("The pain is so sharp.")
        time.sleep(2)
        print("You feel panicked and fall to the ground.")
        time.sleep(2)
        print("Everything goes dark.")
        time.sleep(2)
        game_over()


def time_room():
    """
    Function that takes user input to start the minigame.
    Inside a while loop the user input leads to differen scenarios.
    A for loop creates a count down.
    """
    print("\nA voice speaks through a speaker")
    time.sleep(2)
    print("\nWELCOME TO THE TIME ROOM.")
    time.sleep(2)
    print("HERE, TIME IS OF THE ESSENCE.")
    time.sleep(2)
    print("DO YOU WISH TO START THE TEST?\n")
    time.sleep(2)

    answer = input("Start test? (y/n): \n")
    while True:
        if answer == "y":
            print("YOU CHOSE TO START THE TEST.")
            time.sleep(2)
            print("A ticking sound starts.")
            time.sleep(2)
            print("Then it changes into a robotic voice")
            time.sleep(2)
            print("\nCOUNTDOWN STARTING. YOU HAVE 180 SECONDS\n")
            time.sleep(2)

            for x in range(180, 177, -1):
                print(str(x) + " SECONDS REMAINING")
                time.sleep(1)

            print('\n"...What am I supposed to do..?"\n')
            time.sleep(2)
            print("You desperately look around.")
            time.sleep(2)
            print("You see a table with something on it.")
            time.sleep(2)
            print("You run over to see what it is and realize it is a clock.")
            time.sleep(2)
            print("As you do, you hear the voice in the background.\n")
            time.sleep(2)

            for x in range(170, 166, -1):
                print(str(x) + " SECONDS REMAINING")
                time.sleep(1)
            clock_game()
            break
        elif answer == "n":
            print("You had enough")
            time.sleep(2)
            print('\n"I don\'t want to do this anymore!"\n')
            time.sleep(2)
            decrease_health()
            time_room()
        else:
            print("Please enter one of the options!")
            time.sleep(2)


def clock_game():
    """
    Function that use two nested functions to play the clock game.
    See nested function for information about these.
    """

    def countdown():
        """
        Countdown to simulate a timer. If the player gets the time wrong,
        in the following time_input function, the timer goes down.
        The function uses a starting time which is a global variable.
        Using the time.sleep(1) the print statements that prints the time,
        goes down one second at the time.
        """
        global starting_time
        starting_time -= 3
        for x in range(starting_time, starting_time - 3, -1):
            print(str(x) + " SECONDS REMAINING")
            time.sleep(1)

        if time == 0:
            print("YOUR TIME IS UP")
            time.sleep(2)
            print("EVERYTHING GOES DARK.")
            time.sleep(2)
            print("DEATH WILL BE FAST.")
            time.sleep(2)
            print("THE SHARP PAIN CONSUMES YOU UNTIL YOU ARE NO MORE.")
            time.sleep(2)
            game_over()


    def time_input():
        """
        Function that takes input from the player.
        The player gets to guess what time it is, entering input for,
        hour hand and minute hand.
        In a while loop there is a try that turns the input into an integer.
        If this doesn't work the user gets an error message,
        and have to try again.
        In another while loop the program checks if the user guess,
        is the same as the computer guess.
        If not, the timer goes down using the countdown function.
        """
        hour_hand = 3
        minute_hand = 15

        while True:
            try:
                hour_hand_guess = int(input("HOUR HAND: \n"))
                if 0 < int(hour_hand_guess) <= 12:
                    break
                else:
                    print("\nPLEASE ENTER NUMBERS BETWEEN 1-12 FOR HOURS.\n")
            except ValueError:
                print("\nPLEASE ENTER NUMBERS BETWEEN 1-12 FOR HOURS.\n")

        while True:
            try:
                minute_hand_guess = int(input("MINUTE HAND: \n"))
                if 0 <= int(minute_hand_guess) < 60:
                    break
                else:
                    print("\nPLEASE ENTER NUMBERS BETWEEN 0-59 FOR MINUTES.\n")
            except ValueError:
                print("\nPLEASE ENTER NUMBERS BETWEEN 0-59 FOR MINUTES\n")

        while True:
            try:
                green_button = input("Is this the time? (y/n): \n")
                if green_button == "y":

                    # Code to check answer
                    if hour_hand_guess == hour_hand and minute_hand_guess == minute_hand:
                        print("AH! THE TIME IS A QUARTER PAST THREE.")
                        time.sleep(2)
                        print("THANK YOU.")
                        time.sleep(2)
                        print("PLEASE TAKE THIS GIFT")
                        time.sleep(2)
                        read_article()
                        break
                    elif hour_hand_guess == hour_hand and minute_hand_guess != minute_hand:
                        print("\nTHAT IS THE RIGHT HOUR. BUT WHAT IS THE MINUTE?")
                        time.sleep(2)
                        print("PLEASE TRY AGAIN\n")
                        time.sleep(2)
                        countdown()
                        time_input()
                    elif hour_hand_guess != hour_hand and minute_hand_guess == minute_hand:
                        print("\nTHAT IS THE RIGHT MINUTE. BUT WHAT IS THE HOUR?")
                        time.sleep(2)
                        print("PLEASE TRY AGAIN\n")
                        time.sleep(2)
                        countdown()
                        time_input()
                    elif hour_hand_guess != hour_hand and minute_hand_guess != minute_hand:
                        print("\nTHAT IS NOT THE TIME.")
                        time.sleep(2)
                        print("PLEASE TRY AGAIN\n")
                        time.sleep(2)
                        countdown()
                        time_input()
                    else:
                        time_input()
                else:
                    countdown()
                    time_input()
            except ValueError:
                print("\nPLEASE ENTER y or n.\n")
    print("From a speaker in the clock a voice speaks to you.")
    time.sleep(2)
    print("WELCOME TO THE CLOCK GAME.")
    time.sleep(2)
    print("WHAT AN AFTERNOON DELIGHT TO SEE YOU HERE.")
    time.sleep(2)
    print("WHAT TIME IS IT?")
    time.sleep(2)
    print("BELOW THE CLOCK IS A GREEN BUTTON TO PUSH.")
    time.sleep(2)
    print("DO THIS WHEN YOU HAVE DECIDED WHAT TIME TO ENTER.")
    time.sleep(2)
    time_input()


def read_article():
    """
    Function where the player gets an article.
    From this the user can figure out the password to the computer.
    """
    print("\nA hatch in the clock opens.")
    time.sleep(2)
    print("Out pops an article from an old newspaper.")
    time.sleep(2)
    print("The artilcle headline says:")
    time.sleep(2)
    print("\n EVILCORP opens a new laboratory./n")
    print('"EVILCORP... It sounds so familiar."')
    print("You get an overwhelming thought to go back to the computer.")
    print('"Maybe this is the password..."')
    time.sleep(2)
    computer_scene()


def game_ending():
    """
    Final function that lets the user make a final decision.
    """
    print("A door opens.")
    time.sleep(2)
    print("A woman in a lab coat steps in.")
    time.sleep(2)
    print('"Hello Ava." She says.')
    time.sleep(2)
    print("...Hello...?")
    time.sleep(2)
    print('"I am here to inform you that you passed your jobb application!"')
    time.sleep(2)
    print('"You are now qualified to come work for us at EVILCORP!"')
    time.sleep(2)

    while True:
        answer = input("Do you accept this offer? (y/n): \n")

        if answer == 'y':
            print('"Welcome to EVILCORP!"')
            time.sleep(2)
            print("\nYou accepted the offer!")
            time.sleep(2)
            print("You live out your days doing evil things for EVILCORP.")
            time.sleep(2)
            win_game()
        elif answer == 'n':
            print("The helmet starts to buzz.")
            time.sleep(2)
            game_over()
        else:
            print("Please answer y/n!")


def win_game():
    """
    Print statement for winning the game.
    """
    print("Congratulations! You won the game!")
    quit()


def main():
    """
    Main fuction to run the other functions.
    """
    intro()


main()
