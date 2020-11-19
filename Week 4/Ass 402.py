


def humanPyramid(row, column):
    """ Recursive function for weight calculation  """
    if row < 0 or column < 0:                                # If row or column value is negative then the value is 0
        return 0
    if column > row:                                         # Cannot have column greater than row because
        return 0                                             # this would not be a pyramid
    return 128 + humanPyramid(row - 1, column - 1)/(2) + humanPyramid(row - 1, column)/(2)
                                                             # The first portion is taking into consideration
                                                             # those in the middle and the weight from that
                                                             # While the last portion in the code gets
                                                             # the value for those on the edges
                                                             #It then sums all the values along with the base of 128
if __name__ == '__main__':
    row = int(input("Enter Row Number: "))
    column = int(input("Enter Column Number: "))
    calc_num = humanPyramid(row, column)                        # Calling the human pyramid function
    print("The weight  is : " + str(calc_num))
