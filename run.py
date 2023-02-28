def intro():
    """
    Function for intro of the game. Input is required by the user. 
    If input is "y" the game starts and if input is "n" the game quits.
    Any other input leads to demand for input from user again.
    """
    print("You wake up and open your eyes but you can't see anything")
    print("You stretch your arms up to your head and feel something weird.")
    print("A helmet of some sort is on your head.")
    print("You try to remove it but you can't.")
    print("You try to pull it of with all of your strength but it's stuck.\n")
    print('"... What is this... Where am I... What is going on?"\n')
    print('"... I do not remember anything... Not even my name..."\n')

    global answer

    answer = str.lower((input("Do you want to start to feel your way around? (y/n): ")))

    if answer == "y":
        choices()
    elif answer == "n":
        print("\nYou give up and accept your fate.")
        print("Days go by and you finally close your eyes and never wake up.")
        game_over()
    else:
        print("Incorrect input! Please answer y/n")
        intro()
