


import random
from Ass501 import

def Intro():
    """Greet the user and ask their name."""

    print("Hello friend, today we're going to play the Cups and Dice game! ")

    name = str(input('So before we get started please type out your name: '))
                                                                # Ask the user for their name
    return name


def OpeningBal():
    """Provide the user with a balance of 100 dollars."""

    print("To get you started here, we're granting you a starting balance of a $100!")
                                                                # Start them off with starting balance
    balance = 100
    return balance


def PlayGame():
    """Ask them if they would like to play a game."""

    while True:

        play = input("\n Before we move forward, we just want to confirm you"
                     "\n would still like to play. Please answer Yes or No \n ")
                                                                # Ask user if they want to play game
        play = play.upper()                                     # Change input to uppercase

        if play.upper() != "YES" and play.upper() != "NO":      # If answer is not yes or no continue sends
            print("Please only type out Yes or No.")            # back into the loop
            continue
        else:
            break                                               # If answer is yes or no it braeks out of loop
                                                                # and moves forward
    if play == "YES":
        print("Awesome we are happy to have you here, let's play!")
        pass                                                    # Accepts their yes and moves forward

    else:
        print("\n Awh man, we're sorry to see you leave. Please come back"
              "\n to play more Cups and Dice! \n")
                                                                # Accepts their no and ends the game
        exit(0)


def Roulette():
    """Generate a random number between 1 and 100. This number will be called the goal."""

    goal = random.randint(1, 100)                               # Generates an random integer from 1 to 100
    return goal


def Gambling(balance):
    """"Ask the user how much they would like to bet. This money is deducted from their account."""

    bet = 0                                                    # Need to initiate to allow for return later
    while True:
        try:                                                   # Ask user how much money they want to play with
            bet = int(input('How much money would you like to bet: '))

        except ValueError:                                     # Raises error if user enters anything except a number
            print("That is not a valid input, please only type out a number.")
            continue

        if bet <= 0 or bet > balance:                          # Does not allow to move forward if user does not bet
            print(balance)                                     # anything or bets more than their current balance
            print("\n You have either inputted a zero/negative number or you "
                  "\n have insufficient funds. Please try again.\n ")
            continue

        else:
            break                                              # Breaks loop once user enters something correctly

    return bet


def NoOfDice():
    """User gets to select how many dice they will play with."""

    sixdie = 0
    tendie = 0                                                  # Initiating variables to be returned upon later
    twentydie = 0

    while True:
        try:                                                    # Asks how many 6 sided they want to play with
            sixdie = int(input('How much 6 sided dice did you want to use?'))

        except ValueError:                                      # Raises error if user enters anything except a number
            print("That is not a valid input, please only type out a number.")
            continue

        if sixdie < 0:                                          # Raises error if user enters a negative number
            print("You have either inputted a negative number. Please try again.")
            continue

        else:
            print("\n If you select 0 for all three dice,it will default to 1"
                  "\n no matter what. \n")                      # Prints everytime to let user know default is
            break                                               # always going to be one of each type of die
                                                                # Breaks from while loop once valid entry inputted

    while True:
        try:                                                    # Asks how many 10 sided they want to play with
            tendie = int(input('How much 10 sided dice did you want to use? '))

        except ValueError:                                      # Raise error if user enters anything except a number
            print("That is not a valid input, please only type out a number.")
            continue

        if tendie < 0:                                          # Raise error if user enters a negative number
            print("You have either inputted a negative number. Please try again.")
            continue

        else:
            print("\n If you select 0 for all three dice,it will default to 1"
                  "\n no matter what. \n")                      # Prints everytime to let user know default is
            break                                               # always going to be one of each type of die
                                                                # Breaks from while loop once valid entry inputted
    while True:
        try:                                                    # Asks how many 6 sided they want to play with
            twentydie = int(input('How much 20 sided dice did you want to use? '))

        except ValueError:                                      # Raise error if user enters anything except a number
            print("That is not a valid input, please only type out a number.")
            continue

        if twentydie < 0:                                       # Raises error if user enters a negative number
            print("You have either inputted a negative number. Please try again.")
            continue

        else:
            print("\n If you select 0 for all three dice,it will default to 1"
                  "\n no matter what. \n")                      # Prints everytime to let user know default is
            break                                               # always going to be one of each type of die
                                                                # Breaks from while loop once valid entry inputted
    return [sixdie, tendie, twentydie]
                                                                # Returns the 3 types of dice

def SumOfDice(sixdie, tendie, twentydie):
    """All the three kinds of dice will be rolled and the class Cup from prevoius assignment will be called
    to compute the total."""


    cup = Cup(sixdie, tendie, twentydie)                        # Call upon Cup class from previous assignment
                                                                # and inputs the number of dice according to user input
    rolls = cup.roll()                                          # Performs the roll function from the Cup Class
    total = cup.getSum()                                        # Gets the Sum from the Cup Class

    print('\nThe sum of rolls is:', total)                      # Prints the total out

    return total                                                # Returns the total to be called upon later


def Difference(goal, total):
    """Calculates total difference between random generated number and random generated goal."""

    difference = goal - total                                   # Creates difference variable for how much
    print ('The goal was:', goal)                               # user was off by
    print('The difference between goal and sum of rolls is:', difference)
                                                                # The difference is printed for user to see
    return difference                                           # difference is returned to call upon later


def Money(goal, total, bet, balance, name):
    """Calculator for either earnings or deduction."""

    if total == goal:                                           # If the users random generated value is the exact
                                                                # same as the goal they get 10 times their money back
        balance += 10 * bet                                     # Accumulator to run over and over
        print("Great playing {}! You now have a balance of ${}!".format(name, balance))
        return balance                                          # Returns balance after they get prize money


    elif goal - 3 <= total <= goal + 3:
                                                                # If the two numbers are within 3, they get 5 times
        balance += 5 * bet                                      # their bet back
        print("Great playing {}! You now have a balance of ${}!".format(name, balance))
        return balance
                                                                # Returns balance after they get prize money
    elif goal - 10 <= total <= goal + 10:
                                                                # If the two numbrs are within 10, they get 2 times
        balance += 2 * bet                                      # their bet back
        print("Great playing {}! You now have a balance of ${}!".format(name, balance))
        return balance                                          # Returns balance after they get prize money

    else:
                                                                # If they don't win, they have to lose money
        balance -= bet                                          # Accumulator to subtract money every round
        print("Good guess {}! You have a remaining balance of  ${}!".format(name, balance))
        return balance                                          # Returns balance after deductions


if __name__ == '__main__':


    name = Intro()
    print ("")
    balance = OpeningBal()

    while True:
        play = PlayGame()
        goal = Roulette()
        print ("")
        bet = Gambling(balance)
        num_die = NoOfDice()                                # Empty variable created
        total = SumOfDice(num_die[0], num_die[1], num_die[2])   # Allowed me to index the different dice picked
        difference = Difference(goal, total)
        balance = Money(goal, total, bet, balance, name)

        if balance <= 0:                                    # Checks for balance equal to zero after the round
            print("Awh man you're all out of money! Please come back to play again!")
            break                                           # Stops the game if condition is met
