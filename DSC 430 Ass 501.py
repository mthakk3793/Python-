# Maharshi Thakkar
# 07/23/2020
# "I have not given or received any unauthorized assistance on this assignment."
# https://youtu.be/H1Ui4k5PjBU


import random


class SixSidedDie():
    """A class to obtain an integer from a 6 headed die."""
    number = 6                                          # Setting the standard for this class at 6

    def roll(self):
        """Generates a random integer from 1-6."""
        self.num = random.randint(1, self.number)       # Selects random number from 1-6 and assigns it to self.num
        return self.num

    def getFaceValue(self):
        """Returns the face value of the die"""         # Returns value just generated
        return self.num

    def __repr__(self):
        """Returns the canonical string representation for the die"""
        return 'SixSidedDie({})'.format(self.num)       # Printed in the shell appropriately using repr


class TenSidedDie(SixSidedDie):
    """A class to obtain an integer from a 10 headed die"""
    number = 10                                         # Setting the standard for this class at 10
                                                        # All the other methods were inherited
    def __repr__(self):
        return 'TenSidedDie({})'.format(self.num)       # This was not inherited as a it's particular
                                                        # for the way it needs to be printed in the shell

class TwentySidedDie(SixSidedDie):
    """A class to obtain an integer from a 20 headed die"""
    number = 20                                         # Setting the standard for this class at 20
                                                        # All the other methods were inherited
    def __repr__(self):
        return "TwentySidedDie({})".format(self.num)    # This was not inherited as it's particular
                                                        # for the way it needs to be printed in the shell

class Cup:
    """A class to take the 3 dice and compute a total sum from them."""

    def __init__(self, six=1, ten=1, twenty=1):         # By standard the cup must have at least one die in them
        """Constructor for class Cup."""                # from 6/10/20 sided

        self.six = six
        self.ten = ten                                  # Names established with self to be called for later
        self.twenty = twenty

        self.NSideDice = []                             # Container for each type of dice (6,10,20)
        self.CupOfDice = []                             # Container for all the dice together regardless of
                                                        # what kind or quantity


    def roll(self):
        """Roll function is performed using the classes created earlier to generate values. """

        for i in range(self.six):                       # Number of times dice will be used is established
            d = SixSidedDie()                           # Pulling from class from earlier
            self.NSideDice.append(d)                    # Roll is performed for 6 sided dice and appended into list
            self.CupOfDice.append(d.roll())             # The value is then appended into the cup list


        for i in range(self.ten):                       # Number of times dice will be used is established
            d = TenSidedDie()                           # Pulling from class from earlier
            self.NSideDice.append(d)                    # Roll is performed for 10 sided dice and appended into list
            self.CupOfDice.append(d.roll())             # The value is then appended into the cup list


        for i in range(self.twenty):                    # Number of times dice will be used is established
            d = TwentySidedDie()                        # Pulling from class from earlier
            self.NSideDice.append(d)                    # Roll is performed for 20 sided dice and appended into list
            self.CupOfDice.append(d.roll())             # The value is then appended into the cup list


        return self.CupOfDice                           # All the values generated are returned to be used later


    def getSum(self):
        """ All of the dice are put together and summed. """

        total = 0                                       # Initiator
        for val in self.CupOfDice:                      # Iterated through the list generated earlier
            total += val                                # Each value is added to total

        return total                                    # Total value is returned to be printed after

    def __repr__(self):
        return "Cup({})".format(self.NSideDice)         # Returns canonical string that user can understand


def main():  # display test cases
    """Perform test cases assigned."""

    cup = Cup()

    print('All Rolls: ', cup.roll())
    print('Sum of Rolls: ', cup.getSum())
    print('Cup Contains: ', cup)
    print('')

    cup1 = Cup(3, 0, 0)
    print('All Rolls ', cup1.roll())                    # Prints the list of all rolls performed
    print('Sum of Rolls: ', cup1.getSum())              # The sum is printed that was computed from function getSum()
    print('Cup Contains: ', cup1)                       # The final result from repr is printed to show which
    print('')                                           # dice produced which number

    cup2 = Cup(1, 2, 1)
    print('All Rolls ', cup2.roll())
    print('Sum of Rolls: ', cup2.getSum())
    print('Cup Contains: ', cup2)


if __name__ == '__main__':
    main()
