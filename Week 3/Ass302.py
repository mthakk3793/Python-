

import math


def find_prime(number):
    """Check for whether number inputted is prime or not."""
    if number == 1:                                      # Returns false to ensure user cannot use it
        return False

    for i in range(2, number):                           # If number does not have a remainder it's
        if number % i == 0:                              # after iteration that means it is a prime
            return False                                 # number

    return True


def split_num(number):
    """Take the inputted number and split it into a string and store it in empty list for next step"""
    digit = []                                          # Empty list digit is initiated
    num = str(number)                                   # Number is changed to string so it can be processed
    for val in num:
        digit.append(int(val))                          # Iteration takes the string of numbers and adds them
                                                        # to the list
    return digit


def square_list(digit):
    """Number is taken from last list and iterated through again to square each digit. """

    square_digit = []                                   # Empty list square_digit is initiated
    for val in digit:                                   # Digits from previous list is iterated through
        square_digit.append(int(math.pow(val, 2)))
                                                        # Number is squared and appended into list
    return square_digit


def add_vals(digit):
    """The squared digits are added as required for this exercise."""
    total = 0
    for val in digit:                                   # Added values are returned so that they can be
        total += val                                    # called upon later to store into the master list

    return total


if __name__ == '__main__':

    while True:
        total_list = []                                 # Empty master list is initiated
        total = input("Please select a number:\t")      # Number is selected
        p = int(total)                                  # Number is changed to integer
        if p == 1:
            print("1 is a happy non-prime number so please input another number")
            continue                                    # Doesn't accept 1
        not_happy = False                               # Setting up not_happy to exit for later in the code

        while total != 1:                               # Initiate while loop to keep running as long as
            digit = split_num(total)                    # total is not equal to 1
            print("Dissected List:\t", end="")
            print(digit)
            digit = square_list(digit)
            print("Squared List:\t", end="")            # List are created and printed so it's clear in the
            print(digit)                                # code what list is performing what
            total = add_vals(digit)                     # The numbers are added after they're squared and outputted
            print(total)
            if total in total_list:                     # If number is in list it's going to be a non-happy # as it
                if find_prime(p):                       # will just keep showing up in the list and never get to 1
                    print("It's a non-happy prime")     # Checks previous function and if returned true prints
                else:                                   # it's non-happy prime
                    print("It's a non-happy non-prime") # Else it just prints that it's non-happy non prime
                not_happy = True                        # Boolean created as reflection from previous in code to
                break                                   # allow the break to occur
            else:
                total_list.append(total)                # Added to list to continue moving forward

            print("Total list:\t", end="")
            print(sorted(total_list))

        if not_happy is False:                          # This is the not happy false statement and again
            if find_prime(p):                           # a reflection from when it was initiated in beginning of main
                print("It's a happy prime")             # If function for find_prime is true prints happy prime
            else:
                print("It's a happy non-prime")         # Else returns happy non-prime as it would be false

        ans = input("Do you want to play again?\t")     # Asks user if they'd like to play again

        if ans.upper() == "YES" or ans.isdigit():       # Accepts either yes or a number in case user doesn't read
            continue                                    # properly
        else:
            exit(1)                                     # Any other input including no will just exit


