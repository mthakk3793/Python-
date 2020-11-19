# Maharshi Thakkar
# 07/09/2020
# Honor Statement : “I have not given or received any unauthorized assistance on this assignment.”
# Youtube Link: https://youtu.be/7EzMwbwb0Bk

def allprimes():
    """In this function we obtain all the possible values for prime numbers from 2 to 100."""

    key = []                                          # The empty list is initiated

    for val in range(2, 101):                         # Set to obtain all prime values from 2 to 100
        if val >= 2:                                  # They are then stored into the list
            for n in range(2, val):                   # The values have to be greater than 2 as 1 cannot
                if not (val % n):                     # be included
                    break                             # Pulls all prime numbers by iterating through them
            else:                                     # If a number does not obtain a remainder that means
                key.append(val)                       # it cannot be divisable by anything but it's own
                                                      # number it is appended as a prime number
    return key


def getNums():
    """Here the actual calculation is performed. """
    key = allprimes()                                 # Empty list for key is created

                                                      # Runs code endlessly as no instruction was
    while True:                                       # given to end the code
        num = input("Please enter a number:")         # Changed number to integer as it's outputted
        try:                                          # as a string from input
            selected_num = int(num)                   # Asked for number with try function
        except:
            print("\n Please input only a number!")   # Only accepts a number
            continue
        if selected_num > 100:                        # Limits number to 100 as that was limit
            print("Please only select a number up to 100.")
            continue
        if selected_num in key:
            print("You have picked a prime number please select another number.")
            continue
        for i, number in enumerate(key):              # Iterator function to run through key
            complementary = selected_num - number     # Initiated formula
            if complementary in key[i:]:              # Obtained complimentary number if available
                print(str(selected_num) + " = {} + {}".format(number, complementary))
                break                                 # Printed values as requested for assignment


if __name__ == '__main__':
    getNums()
