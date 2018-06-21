TICKET_PRICE = 10
SERVICE_CHARGE = 2

tickets_remaining = 100


# create the calculate price function. It takes number of tickets and returns (num_of_tickets * TICKET_PRICE)
# Run this code continuously until we run out of tickets


def calculate_price(num_tickets):
    # Create a new constant for 3 dollar service charge, Add the service charge to our result
    return (num_tickets * TICKET_PRICE) + SERVICE_CHARGE


while tickets_remaining > 0:

    # Output how many tickets are remaining using the tickets_remaining variable
    print("There are {} of tickets remaining.".format(tickets_remaining))

    # Gather the user's name and assign it to a new variable
    user_name = input("Enter your name please. ")

    # Prompt the user by name and ask how many tickets they would like
    number_of_tickets = int(input("How many tickets do you want to purchase {}? ".format(user_name)))

    # Expect a ValueError to happen and handle it appropriately..
    try:
        number_of_tickets = int(number_of_tickets)

        if number_of_tickets > tickets_remaining:
            # Raise error if input number is more than remaining tickets
            raise ValueError("Sorry, remaining tickets are only {}".format(tickets_remaining))

    except ValueError as err:
        print("Oh no, we ran into an issue. {}".format(err))
    else:
        # Calculate the price, use calculate function
        total_price = calculate_price(number_of_tickets)

        # Output the price to the screen
        print("Total Price : ${}".format(total_price))

        # Prompt user if they want to proceed. Y/N?
        confirm_purchase = input("Do you want to proceed? Y/N ")
        confirm_purchase = confirm_purchase.upper()
        # If they want to proceed
        if confirm_purchase == "Y":
            # print out to the screen "SOLD!" to confirm purchase
            # TODO: Gather credit card information and process it.
            print("SOLD!")

            # and then decrement the tickets remaining by the number of tickets purchased
            tickets_remaining -= number_of_tickets

        # Other wise ...
        else:
            # Thanks them by name
            print("Thanks, {}.".format(user_name))

# Notify user that tickets are sold out
print("Sorry the tickets are sold out!! ")
