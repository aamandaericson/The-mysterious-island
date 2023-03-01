#Empty list which items are added and removed from through functions. 
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
    """
    Function that lets the user search around the room. 
    If "key" is in the inventory list the computer_scene function is called. 
    If not, the user will have to provide input if they want to
    keep searching or return to the box.
    If they choose the box, the open_box function is called.  
    """
    print("\nYou let go of the box and keep feeling your way through the room")
    print("When moving around you feel that something is pulling lightly onto the helmet")
    print("You touch the back of your head and you can feel a small cord connected to the helmet.\n")
    print('..."What is this thing..?"\n')
    print("You keep moving around and bump into something.")
    print("It seems to be a desk and you can feel a bunch of wires.\n")
    print('"... It must be a computer..!"\n')
    print("Blindly feeling around, you some feel some sort of cavity.")
    print('"A key hole!"\n')

    while True:
        if "key" in inventory:
            print("You put the key in the key hole.")
            remove_from_inventory("key")
            print("Key was removed from your inventory\n")
            print("computerscene")
            break
        else:
            answer = input("You have no key, Do you want to keep exploring or go to the box? (explore/box): ")

            if answer == "explore":
                print("You walk around but can't find anything but the box")
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


    

def main():
    """
    Main fuction to run the other functions.
    """
    intro()


main()
