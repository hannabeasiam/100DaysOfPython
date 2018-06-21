
""" snake_case use variable all lower case with underscore """


first_name = input("What is your first name? ")
print("Hello,", first_name)
if first_name == "Craig":
    print(first_name, "is learning Python")
elif first_name == "Hanna":
    print(first_name, "is learning this course.")
else:
    # This is just child info protection
    age = int(input("How old are you? "))
    if age <= 13:
        print("Wow you're {}! Too Young".format(age))
    print("You should totally learn Python, {}!".format(first_name))
print("Have a great day {}!".format(first_name))

def yell(text):
    text = text.upper()
    number_of_characters = len(text)
    result = text + "!" * (number_of_characters // 2)  # always keep as integer
    print(result)

yell("You are doing great")
yell("Don't forget to ask for help")

