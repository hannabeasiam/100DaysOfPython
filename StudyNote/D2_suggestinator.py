"""
    Treehouse task D2-01
    I've made a function that creates brand new product names using artificial intelligence.
    I have a problem though, people keep on adding product ideas that are too short. It makes the suggestions look bad.
    Can you please raise a ValueError if the product_idea is less than 3 characters long?
"""


def suggest(product_idea):
    if len(product_idea) < 3:
        raise ValueError("Enter at least 3 letter please.")
    return product_idea + " added on idea, Thanks!"


try:
    product_idea = input("Can you suggest your idea please?")
    get_idea = suggest(product_idea)
except ValueError as err:
    print("Oh no! That's too short")
    print("({})".format(err))
else:
    print("Your suggestion is {}".format(get_idea))
