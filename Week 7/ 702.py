


import math
from DSC_430_701 import WarAndPeacePseudoRandomNumberGenerator as rand

class Point:

    def __init__(self, x=0.0, y=0.0):
        """ Constructor function for Point class   """

        self.x = x                                              # Set up x coordinate
        self.y = y                                              # Set up y coordinate


    def get_coord(self):
        """ Returns the coordinate for the point."""

        return self.x, self.y

    def distance(self, point2):
        """Calculates the distance between two points."""

        dif_x = point2.x - self.x
        dif_y = point2.y - self.y

        return math.sqrt(dif_x ** 2 + dif_y ** 2)             # Returns Euclidean distance


class Ellipse:

    def __init__(self, EP1=Point(), EP2=Point(), width=4):
        """ Ellipse class that inherits from Point class and sets up points to be used on the ellipses."""

        super().__init__()                                     # Gets the super class of the point
        self.EP1 = EP1
        self.EP2 = EP2
        self.width = width

    def isInside(self, point3):
        """As mentioned in instruction video, a + b has to be < w."""
                                                               # Computed distance of both points and checked
                                                               # if it's less than the width.
        return self.EP1.distance(point3) + self.EP2.distance(point3) < self.width


def rectangle_coord(ellipse1, ellipse2):
    """Computes the coordinates for the rectangle that surrounds the two ellipses."""

    ell1p1 = ellipse1.EP1                                     # Gets the X and Y for Point 1 for Ellipse 1
    el1x1, el1y1 = ell1p1.get_coord()
    ell1p2 = ellipse1.EP2                                     # Gets the X and Y for Point 2 for Ellipse 1
    el1x2, el1y2 = ell1p2.get_coord()
    el1w = ellipse1.width                                     # Gets the W for Ellipse 1

    ell2p1 = ellipse2.EP1                                     # Gets the X and Y for Point 1 for Ellipse 2
    el2x1, el2y1 = ell2p1.get_coord()
    ell2p2 = ellipse2.EP2                                     # Gets the X and Y for Point 2 for Ellipse 2
    el2x2, el2y2 = ell2p2.get_coord()
    el2w = ellipse1.width                                     # Gets the W for Ellipse 2

    if el1w > el2w:                                           # As mentioned in the instruction video we find
        final_w = el1w                                        # the largest width of the two ellipses
    else:
        final_w = el2w

    b_r_x = max(el1x1, el1x2, el2x1, el2x2) + (final_w / 2)   # Bottom Right X
    b_r_y = min(el1y1, el1y2, el2y1, el2y2) - (final_w / 2)   # Bottom Right Y
    b_r_p = Point(b_r_x, b_r_y)                               # Creates the point for the coordinates

    t_r_x = max(el1x1, el1x2, el2x1, el2x2) + (final_w / 2)   # Top Right X
    t_r_y = max(el1y1, el1y2, el2y1, el2y2) + (final_w / 2)   # Top Right Y
    t_r_p = Point(t_r_x, t_r_y)                               # Creates the point for the coordinates

    t_l_x = min(el1x1, el1x2, el2x1, el2x2) - (final_w / 2)   # Top Left X
    t_l_y = max(el1y1, el1y2, el2y1, el2y2) + (final_w / 2)   # Top Left Y
    t_l_p = Point(t_l_x, t_l_y)                               # Creates the point for the coordinates

    b_l_x = min(el1x1, el1x2, el2x1, el2x2) - (final_w / 2)   # Bottom Left X
    b_l_y = min(el1y1, el1y2, el2y1, el2y2) - (final_w / 2)   # Bottom Left Y
    b_l_p = Point(b_l_x, b_l_y)                               # Creates the point for the coordinates

    x_coords = [b_r_x, b_l_x, t_r_x, t_l_x]                   # Stores the list for all the x coordinates
    y_coords = [b_r_y, b_l_y, t_r_y, t_l_y]                   # Stores the list for all the y coordinates

    return b_r_p, t_r_p, t_l_p, b_l_p, x_coords, y_coords


def area_of_ellipse(ellipse1, ellipse2):
    """Computes the area of the ellipse."""
                                                              # Retrieves the rectangular coordinate points
                                                              # along with a list of x & y coordinates
    b_r_p, t_r_p, t_l_p, b_l_p, x_coords, y_coords = rectangle_coord(ellipse1, ellipse2)

    first_x = min(x_coords)                                   # Finds the min & max of the x coordinates
    end_x = max(x_coords)

    first_y = min(y_coords)                                   # Finds the min & max of the y coordinates
    end_y = max(y_coords)

    x_ys = [first_x, end_x, first_y, end_y]                   # Creates a list of the min and max of the x & y's

    len1 = b_l_p.distance(t_l_p)                              # Assigns len 1 for distance from bottom left point to
    len2 = b_l_p.distance(b_r_p)                              # top left point
                                                              # Assigns len 2 for distance from bottom left point to
    area_of_rec = len1 * len2                                 # bottom right point and computes the area of the rec.
    suc_pts = successful_pts(x_ys, ellipse1, ellipse2)        # Retrieves the amount of points that successfully hits
                                                              # inside the two ellipses
    return suc_pts * area_of_rec / 10000


def successful_pts(x_ys, ellipse1, ellipse2):
    """Finds all the successful points that hit the ellipses."""

    count = 0                                                 # Keeps track of successful points
    prng = rand()                                             # Creates a reference to
                                                              # WarAndPeacePseudoRandomNumberGenerator class
    # x_ys = [first_x, end_x, first_y, end_y]
    for i in range(10000):                                    # Loops through 10,000 times
        lenx = x_ys[1] - x_ys[0]                              # Computes the difference between max & min of the x
                                                              # rectangular coordinates
        x = prng.add_em_up(prng.random()) * lenx              # Gets a randomized number based on prng and multiplies
        x += x_ys[0]                                          # it by lenx & adds itself to the min of the x coor.

        leny = x_ys[3] - x_ys[2]                              # Computes the difference between max & min of the y
        y = prng.add_em_up(prng.random()) * leny              # rectangular coordinates
        y += x_ys[2]                                          # Gets a randomized number based on prng and multiplies
                                                              # it by lenx & adds itself to the min of the y coor.
        temp_p = Point(x, y)                                  # Creates a temp. point for the computed x and y
        if ellipse1.isInside(temp_p) and ellipse2.isInside(temp_p):
            count += 1                                        # If the point is inside both ellipses we add to count
    return count


if __name__ == '__main__':
    point1 = Point(2,3)
    point2 = Point(3,5)

    ellipse1 = Ellipse(point1, point2, 3)
    ellipse2 = Ellipse(point1, point2, 6)

    area = area_of_ellipse(ellipse1, ellipse2)
    print(area)
