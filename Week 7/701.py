

from statistics import mean


def read_file():
    """Storing all the lines of the file into a list. """

    all_lines = []                                   # Initializing the list
    with open('war-and-peace.txt', 'r') as passage:
        for line in passage.readlines():             # Loop through all lines
            for c in line:                           # Loop through each character and appends to list
                all_lines.append(c)
    all_lines.pop(0)                                 # Popping the first character as it's null
    return all_lines


class WarAndPeacePseudoRandomNumberGenerator:

    def __init__(self, seed=1):
        """Initializes the seed, temp, & calls the read_file and defines the file_lines."""

        self.step = 100
        self.temp = seed
        self.file_lines = read_file()


    def redo_j(self, j):
        """Helper function to step every character."""

        j += self.step                               # As j is an index, step is added to itself
                                                     # ex. so that we can  skip every 100 characters
        if j >= len(self.file_lines):                # If j reaches the end of the file, (end of the list)
            j = j % len(self.file_lines)             # as recommended in discussion, we get the modulo of j
        return j                                     # and the length of the entire list and return j to
                                                     # be used as an index

    def random(self):
        """ Compares two characters together and appends it to a list of bit of 0 and 1s."""

        j = self.temp                               # Iterating through every other character
                                                    # temp is used save the last character for the next
                                                    # iteration
        beets = []                                  # List provided for the 32 bits

        for i in range(32):
            char_1 = self.file_lines[j]             # Grabs the character at index j

            j = self.redo_j(j)                      # Calls the helper function to move j to it's next step

            char_2 = self.file_lines[j]             # Grabs the character at index j


            if char_1 == char_2:                    # Avoid the same characters
                j = self.redo_j(j)                  # Changes value of j to the next step
                char_1 = self.file_lines[j]         # Value is reassigned to char_1
                j = self.redo_j(j)                  # Changes value of j to the next step
                char_2 = self.file_lines[j]         # Value is reassigned to char_2

            j = self.redo_j(j)                      # Changes the value of j for the next bit

            if char_1 > char_2:                     # Appends 1 if the 1st character is bigger than 2nd
                beets.append(1)
            else:
                beets.append(0)                     # Else a 0 is appended

        self.temp = j                               # Temp is assigned j to save the last index
        return beets

    def add_em_up(self, beets):
        """ Here all the values that are true in the list are added."""
        add = 0
        for i in range(32):                         # Loops through 32 times
            if beets[i] == 1:                       # If an entity is one, it passes on the next clause
                add += (1 / 2 ** (i + 1))           # the value is added as it was true

        return add                                  # The sum is computed by the addition of each iteration
                                                    # of 1 over 2 to the power of it's index + 1 in
                                                # the 32 list. (Index starts with 0)


if __name__ == '__main__':
    prng = WarAndPeacePseudoRandomNumberGenerator(0)

    total_bits = []
    for i in range(5):
        bits = prng.random()
        print(prng.add_em_up(bits))
        total_bits.append(prng.add_em_up(bits))

    print("Mean\t" + str(mean(total_bits)))
    print("Max\t" + str(max(total_bits)))
    print("Min\t" + str(min(total_bits)))
