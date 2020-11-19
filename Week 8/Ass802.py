

from plotGenerator import InteractivePlotGenerator, SimplePlotGenerator, RandomPlotGenerator


class PlotViewer:

    def registerPlotGenerator(self, generator):
        """ Sets up generator to be called upon in next function. """
        self.gen = generator

    def generate(self):
        """Here we have self.gen calling function generate() from previous assignment/code."""
        return self.gen.generate()


if __name__ == '__main__':
    pv = PlotViewer()
    pv.registerPlotGenerator(RandomPlotGenerator())
    print(pv.generate())
    #pv.registerPlotGenerator(InteractivePlotGenerator())
    #print(pv.generate())
