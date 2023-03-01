inventory = [""]

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
        box_or_search()
    elif answer == "n":
        print("\nYou give up and accept your fate.")
        print("Days go by and you finally close your eyes and never wake up.")
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
    print("You start using your hands to feel around.")
    print("Crawling around on your knees, you find what feels like a box.\n")
    while True:
        answer = input("Do you open the box? (y/n): ")
        if answer == "y":
            open_box()
            break
        elif answer == "n":
            print("search")
            break
        else:
            print("Incorrect input! Please answer y/n")


def open_box():
    """
    Function that leads to the following buttons game. 
    Print statements and then a function call. 
    """

    print("The box seems to be made of metal.")
    print("You can feel three buttons on the top.")
    print("You press one and suddenly a voice starts speaking to you from the box.\n")
    print('"WELCOME TO YOUR FIRST TEST."')
    print('"PLEASE ENTER PRESS THE BUTTONS IN THE RIGHT SEQUENCE!\n')
    print('"...My first test..?"')
    print('"...I guess I have to find the right sequence then..?"\n')
    print("Buttons game")


def search():


def add_to_inventory(item):


def remove_from_inventory(item):

    


def main():
    """
    Main fuction to run the other functions.
    """
    intro()


main()
