#Maharshi Thakkar
#07/02/2020
#Honor Statement: “I have not given or received any unauthorized assistance on this assignment.”
#Youtube Link: https://youtu.be/Y27d6VlFw6Q



def gameplay():
    """Asks user if they want to play. """


    gametime = input("\n Hello again, whether this is your first game or you're playing again"
                     "\n we just want to make sure you want to move forward. Please answer either"
                     "\n yes or no. ")                          #Give option to play or quit

    if gametime.upper() != "YES":                               # All inputs are converted to uppercase
        print("\n Awh we're sorry to see you leave. Please come back to play again.")
        return False
    else:
        print("\n Yea buddy! Let's do it :)")                   # Moves forward as the user agrees
        return True


def userinput():
    """Only allows for input of a number between 1 -3. """

    file_num = 0

    while True:
        nombre = input("\n Hello hello, so you have the option of picking between 3 files."
                       "\n So what will it be file 1, 2, or 3.")
                                                                # User picks the from three file options
        try:
            file_num = int(nombre)                              # inputs and converts to an integer
        except:
            print("\n Please input a number!\n")
            continue                                            # Anything but a number is rejected

        if file_num < 1 or file_num > 3:
            print("\n Please input a number between 1 and 3!\n")
            continue                                            # Restrain input to number between 1 and 3
        else:
            break                                               # Break and move forward

    return file_num


def whatfile(file_num):
    """Chooses file depending on what user selects."""

    filename = ''                                               # Preps to include quotes for function

    if file_num == 1:
        filename = 'StemAndLeaf1.txt'

    elif file_num == 2:
        filename = 'StemAndLeaf2.txt'                           # Picks file depending on user input

    else:
        filename = 'StemAndLeaf3.txt'

    print('We will be using the file:\t' + filename)
    return filename


def readfile(filename):
    """Reads the file and starts splits data into main list numlst. """

    infile = open(filename, "r")
    lineList = infile.readlines()
    infile.close()                                              # open, read, close and then return content

    numlst = []                                                 # List is declared
    for i in range(0, len(lineList)):                           # Iterate through file
        x = int(lineList[i].strip())                            # Split each set of numbers apart
        numlst.append(x)                                        # Move into empty list created

    numlst.sort()
    return numlst

def createStem(numlst):
    """ Finds the num of digits in each value and stores them in their appropriate list.
       Stems and leaves are created."""

    len1 = []
    len2 = []                                                   # Create Empty lists for storage
    len3 = []
    len4 = []

    finalStem = []

    for val in numlst:
        if len(str(val)) == 1:
            len1.append(val)
        elif len(str(val)) == 2:                                # Converted to strings and length is
            len2.append(val)                                    # is assessed. Then it is binned into
        elif len(str(val)) == 3:                                # correct list (len1/2/3/4) depending on
            len3.append(val)                                    # length of characters
        elif len(str(val)) == 4:
            len4.append(val)

    #     Checks to see if there are any single digits
    if not len1:
        print("")
    else:
        finalStem.append(0)                                     # Stem 0 is created for single digits
        print("0|", end=" ")
        sorted(len1)
        noDup1Stem = []                                         # Another empty list created
        for val in len1:
            if val not in noDup1Stem:                           # Only one stem is created and duplicates
                noDup1Stem.append(val)                          # are not entered
        for val in sorted(noDup1Stem):
            print(val, end="  ")

    print("")

    len2stem = []
    for val in len2:                                            # Stem is created for values of length 2
        len2stem.append(int(str(val)[:1]))                      # and sliced to obtain just first character

    noDup2Stem = []
    for val in len2stem:                                        # Only one stem is created and duplicates
        if val not in noDup2Stem:                               # are not entered
            noDup2Stem.append(val)

    len3stem = []
    for val in len3:                                            # Stem is created for values of length 3
        len3stem.append(int(str(val)[:2]))                      # and sliced to obtain just two character

    noDup3Stem = []
    for val in len3stem:                                       # Only one stem is created and duplicates
        if val not in noDup3Stem:                              # are not entered
            noDup3Stem.append(val)

    len4stem = []
    for val in len4:                                           # Stem is created for values of length 4
        len4stem.append(int(str(val)[:3]))                     # and sliced to obtain just three character

    noDup4Stem = []
    for val in len4stem:                                       # Only one stem is created and duplicates
        if val not in noDup4Stem:                              # are not entered
            noDup4Stem.append(val)


    #   Starts finding the leaves

    len2leaves = []                                            # Obtain just the remainders as there's only
    for val in len2:                                           # two digits
        len2leaves.append(val % 10)


    len3leaves = []
    for val in len3:                                           # Take the stems and add 0, and again take
        for key in len3stem:                                   # the remainder of them using modulo
            len3leaves.append(val %  int(str(key) + str(0)))

    len4leaves = []
    for val in len4:
        for key in len4stem:
            len4leaves.append(val %  int(str(key) + str(0)))   # Same as above for len3leaves

    for val in sorted(noDup2Stem):
        print(str(val) + "|", end=" ")                         # Print | for stem and use end = "" to make
        for key in sorted(len2leaves):                         # sure it doesn't print to next line by default
            if int(str(val) + str(key)) in len2:
                len2.remove(int(str(val) + str(key)))          # Stop the loop and move onto next numbers
                print(str(key) + " ", end=" ")
        print()

    for val in sorted(noDup3Stem):
        print(str(val) + "|", end=" ")
        for key in sorted(len3leaves):
            if int(str(val) + str(key)) in len3:               # Same as Above
                len3.remove(int(str(val) + str(key)))
                print(str(key) + " ", end=" ")
        print()

    for val in sorted(noDup4Stem):
        print(str(val) + "|", end=" ")
        for key in sorted(len4leaves):                         # Same as Above
            if int(str(val) + str(key)) in len4:
                len4.remove(int(str(val) + str(key)))
                print(str(key) + " ", end=" ")
        print()
    return



if __name__ == '__main__':
    """The main function through which everything routes back and forth to."""

    print("\n Hello friend, I am STLP and I have been designed to help create"
          "\n some stem and leaf plots for you. Lets get started!")

    gameplay()
    if gameplay is False:                                      # Exit if player does not want to play
        exit()

    while True:
        file_num = userinput()
        filename = whatfile(file_num)
        numlst = readfile(filename)
        createStem(numlst)

        ans = input("\nWould you like to do this again?\t")
        if ans.upper() == "NO":                               # Break and exit while loop/game if user chooses
            print("\nBye")
            break
        else:
            continue