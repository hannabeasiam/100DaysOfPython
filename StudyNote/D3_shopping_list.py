"""
    this app will prompt user to add shopping list. Display "DONE" & "HELP" options for user
    if user enter DONE, exit the app, if user enter HELP display help message and back in to the proceed
    create a new empty list named shopping_list
    create a function named add_to_list that declares a parameter named item
    add item to the list
    call add_to_list with new_item as an argument
    as a user, should know total length of
"""
import os


shopping_list = []


"""
    os.system name check tell you if you are on window or not
    nt : all modern version of windows, run cls
    if not window, run clear
"""


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def show_help():
    clear_screen()
    print("What should we pick up at the store?")
    print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' for this help.
Enter 'SHOW' to see shopping list
Enter 'REMOVE' to delete item in the item list
    """)


def add_to_list(item):
    if len(shopping_list):
        position = input("Where should I add {}?\n"
                         "Press ENTER to add to the end of the list\n"
                         "> ".format(item))
    else:
        position = 0

    try:
        position = abs(int(position))
    except ValueError:
        position = None
    if position is not None:
        shopping_list.insert(position-1, item)
    else:
        shopping_list.append(item)

    show_list()


# Define a function named show_list that prints all the items in the list
def show_list():
    clear_screen()

    print("Here's your list: ")

    index = 1
    for item in shopping_list:
        print("{}. {}".format(index, item))
        index += 1

    print("-"*10)


def remove_from_list():
    show_list()
    what_to_remove = input("What would you like to remove?\n > ")
    try:
        shopping_list.remove(what_to_remove)
    except ValueError:
        pass
    show_list()


show_help()

while True:
    new_item = input("> ")

    if new_item.upper() == "DONE" or new_item.upper() == "QUIT":
        break
    elif new_item.upper() == "HELP":
        show_help()
        continue
    # Enable the Show command to show the list.
    elif new_item.upper() == "SHOW":
        show_list()
        continue
    elif new_item.upper() == 'REMOVE':
        remove_from_list()
    else:
        add_to_list(new_item)

show_list()
