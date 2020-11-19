



from random import randrange


def find_num(list, sum):
    """Finds the numbers in the list, and recursively goes through the list from front to end."""

    small = 0                                                 # Initiate for beginning of list
    high = len(list) - 1                                      # Initiate for end of list
    while True:
        if small == high:
            print("No sum found with list:\t", end="")        # If each index in the list has been exhausted
            print(list)                                       # following the code at the bottom, this would mean
            return ""                                         # there is no combination of numbers for the sum

        add = list[small] + list[high]                        # Adds value at first and last indices
        if add < sum:                                         # If value at first index is less than target number
            small += 1                                        # index onto second number for combo in list
        elif add > sum:                                       # If value at last index is greater than target number
            high -= 1                                         # index onto the the second to last number in index
        else:
            print(list)
            return "Found a sum with the nums:\t" + str(list[small]) + " and " + str(list[high])


if __name__ == '__main__':
    while True:

        length = int(input("How long do you want the list to be?"))
        new_list = []                                        # Initiate empty list for random numbers to be put in
        for i in range(0, length):                           # Allow user to pick how long list will be from input
            new_list.append(randrange(100))                  # Append all random numbers into list for check

        sum = int(input("What do you want the sum to be?"))
        print(find_num(sorted(new_list), sum))
