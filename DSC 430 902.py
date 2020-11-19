# Maharshi Thakkar
# 08/20/2020
# "I have not given or received any unauthorized assistance on this assignment."
# https://youtu.be/LeojaFfivBE



import numpy as np
import random


def conway(s, p):
    """Creating a conway board, that sets up a two dimensional NumPy array size s,
    with a probably p for random generation of population."""

    array = np.random.random((s, s))            # Setting up default array that will always have same sized array
    for i in range(s):                          # Iterating through each element in the array s X s
        for j in range(s):
            if random.random() < p:             # Taking account the probability to make sure random # generated
                array[i, j] = 1                 # If the randomly generated # is less than inputted probability
                                                # the array will for that specific index will have a 1 instead of 0
    return array.astype(int)                    # Making sure the value returned is an integer


def advance(b, t):
    """Advances Conway's game based on the rules of the game and time."""

    for time in range(t):                       # Accounting for how many times the iteration should run
        row, col = b.shape                      # Using numpy's shape to use row and columns as the shape
        len_array = len(b[0])                   # Determines  the length of first row, as that will be
                                                # how many columns there will be as well
        new_array = conway(len_array, 0)        # Setting up a new array that is all 0's

        for i in range(-1, row - 1):            # Iteration through each index in array
            for j in range(-1, col - 1):
                totals = np.array([b[i - 1][j - 1], b[i - 1][j], b[i - 1][j + 1],
                                   b[i][j - 1], b[i][j], b[i][j + 1],
                                   b[i + 1][j - 1], b[i + 1][j], b[i + 1][j + 1]])

                                                # Each index is iterated through this particular scheme to check
                                                # how many 0's and 1's there are next to each element
                total = np.sum(totals) - b[i, j]# Sums up the total amount
                if b[i, j] == 1:                # Trigger statement for any indices with value of 1
                    if total < 2 or total > 3:  # If the total number alive next to each index is less than 2 or
                                                # greater than 3, the next statement is triggered
                        new_array[i, j] = 0     # That particular index that triggered the statement get's
                                                # reassigned to the value of 0 instead
                    elif total == 2 or total == 3:
                        new_array[i, j] = 1     # Any index that have neighbors that are 1 equivalent to 2 or 3
                                                # get's to keep it's index at 1

                elif b[i, j] == 0:              # If an index is the value 0, then the next statement is triggered
                    if total == 3:              # If there are 3  total number of neighbors for that index
                        new_array[i, j] = 1     # have a value of 1, that index changed from 0 to 1

        b = new_array                           # New array is established


        return b



if __name__ == '__main__':

    print("Test 1: 0.25 Probability with 5 Iterations\n")
    b = conway(5, 0.25)
    print(b,"\n")
    print ("New Array\n")
    print(advance(b, 5))

    print("\n Test 2: 0.75 Probability with 5 Iterations\n")
    b = conway(5, 0.75)
    print(b,"\n")
    print("New Array\n")
    print(advance(b, 5))

    print("\n Test 3: 0.25 Probability with 10 Iterations\n")
    b = conway(7, 0.25)
    print(b,"\n")
    print("New Array\n")
    print(advance(b, 10))

    print("\n Test 4: 0.75 Probability with 10 Iterations \n")
    b = conway(7, 0.75)
    print(b,"\n")
    print("New Array\n")
    print(advance(b, 10))

