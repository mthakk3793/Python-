

import random


class SimplePlotGenerator:

    def __init__(self):
        """Constructor function to setup for all the empty lists needed."""
        self.names = []
        self.adjs = []
        self.prof = []                                     # All the empty lists are created to be used
        self.verbs = []                                    # throughout the program
        self.adj_evil = []
        self.vil_job = []
        self.vils = []


    def read_file(self):
        """Read into each .txt file provided and split each individual's name into a separate string."""

        with open("plot_names.txt", "r") as f:
            self.names = [line.strip() for line in f]

        with open("plot_adjectives.txt", "r") as f:
            self.adjs = [line.strip() for line in f]

        with open("plot_profesions.txt", "r") as f:
            self.prof = [line.strip() for line in f]

        with open("plot_verbs.txt", "r") as f:                  # All the files contents are split into different
            self.verbs = [line.strip() for line in f]           # strings

        with open("plot_adjectives_evil.txt", "r") as f:
            self.adj_evil = [line.strip() for line in f]

        with open("plot_adjectives_evil.txt", "r") as f:
            self.adj_evil = [line.strip() for line in f]

        with open("plot_villian_job.txt", "r") as f:
            self.vil_job = [line.strip() for line in f]

        with open("plot_villains.txt", "r") as f:
            self.vils = [line.strip() for line in f]

    def generate(self):
        self.read_file()
        return "Something happens"


class RandomPlotGenerator(SimplePlotGenerator):

    def generate(self):
        """Having the SimplePlotGenerator used in the class RandomPlotGenerator, function
        read_file is returned all the possible values along with the verbiage & proper punctuation needed."""

        self.read_file()
        return random.choice(self.names) + ", a " + random.choice(self.adjs) + " " + \
               random.choice(self.prof) + ", must " + random.choice(self.verbs) + " the " + \
               random.choice(self.adj_evil) + " " + random.choice(self.vil_job) + ", " + random.choice(self.vils) + "."
                                                        # Everything returned in proper order to print sentence
                                                        # required
class InteractivePlotGenerator(SimplePlotGenerator):

    def queryUser(self, list, question):

        five = []                                       # Initiate empty list to add to
        for i in range(5):                              # Select 5 different words from the different .txt files
            five.append(random.choice(list))            # Append randomly those 5 words into "list"

        count = 0                                       # Initiate count to 0
        for n in five:
            question += str(count) + ".\t" + str(n) + "\n"
            count += 1                                  # Returns 5 different words from the list in the indexed order

        while True:
                                                        # Loop runs over and over until valid answer is given
            intake = int(input(question + "Input here:\t"))

            if intake >= len(five) or intake < 0:       # If the number is greater than the list generated, in this
                                                        # case 5 it loops again, or less than 0
                print("Please input a valid number [0-4]")
                continue
            else:
                return five[intake]                     # Returns the indexed from the list that the user selected


    def generate(self):
        """All of the unique values are queried here and returned with the result."""

        self.read_file()
        return self.queryUser(self.names, "1) Choose a Protagonist:\t\n") + ", a " + \
               self.queryUser(self.adjs, "2) Choose an Adjective:\t\n") + " " + \
               self.queryUser(self.prof, "3) Choose a Profession:\t\n") + ", must " + \
               self.queryUser(self.verbs, "4) Choose a Verb:\t\n") + " the " + \
               self.queryUser(self.adj_evil, "5) Choose an Adjective for the Antagonist:\t\n") + " " + \
               self.queryUser(self.vil_job, "6) Choose the Antagonist's Job:\t\n") + ", " + \
               self.queryUser(self.vils, "7) Choose a Antagonist:\t\n") + "."

                                                        # Each unique value is selected upon

if __name__ == '__main__':
    ipg = InteractivePlotGenerator()
    print(ipg.generate())

