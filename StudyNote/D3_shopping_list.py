"""
    this app will prompt user to add shopping list. Display "DONE" & "HELP" options for user
    if user enter DONE, exit the app, if user enter HELP display help message and back in to the proceed
    create a new empty list named shopping_list
    create a function named add_to_list that declares a parameter named item
    add item to the list
    call add_to_list with new_item as an argument
    as a user, should know total length of
"""
shopping_list = []


def show_help():
    print("What should we pick up at the store?")
    print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' for this help.
Enter 'SHOW' to see shopping list
    """)


def add_to_list(item):
    shopping_list.append(item)
    print("Added! Your shopping list has {} items.".format(len(shopping_list)))


# Define a function named show_list that prints all the items in the list
def show_list():
    print("Here's your list: ")
    for item in shopping_list:
        print(item)


show_help()
while True:
    new_item = input("> ")

    if new_item.upper() == "DONE":
        break
    elif new_item.upper() == "HELP":
        show_help()
        continue
    # Enable the Show command to show the list.
    elif new_item.upper() == "SHOW":
        show_list()
        continue

    add_to_list(new_item)

show_list()