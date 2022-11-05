# !/usr/bin/env python3
# Created by: Carolyn Webster Pless
# Created on: 2022/11/03
# Takes the user input of a positive and whole number
# Then uses a FOR loop to calculate the number to the
# Power of 2. Displays the answer.


def main():

    # Title of the program
    print("Power of 2")

    # Counter variable
    counter = 0

    # User Input
    user_string = input("Please enter a positive integer: ")

    # Try Catch statement to make sure the input is an integer
    try:
        user_integer = int(user_string)

    # Exception statement
    except Exception:
        print("Please enter an Integer!!")

    else:
        if user_integer >= 0:
            # FOR loop to calculate the input^2
            for counter in range(user_integer + 1):
                power = counter * counter
                print("{}^2 = {}".format(counter, power))
            print("The answer is {}!".format(power))

        # If the user input is negative
        else:
            print("Please enter a positive number!")


if __name__ == "__main__":
    main()
