


#1 Import NumPy
import numpy as np

#2 Use arange to create a NumPy array with 100 equally spaced
# values in the range 0 through 100 (not including 100). Name this NumPy array a.
array_a = np.arange(100)

#3  Use arange to create a NumPy array with 10 equally spaced values
# in the range 0 through 100 (not including 100). Name this NumPy array b.

array_b = np.arange(0,100,10)

#4 Use linspace to create a NumPy array in the range 0 through 10 (inclusive) with
# values spaced at 0.1. Call this NumPy array c.
array_c = np.linspace(0,10,101)


#5 Create a random two-dimensional array with the dimensions 10 by 10. Call this NumPy array d.
array_d = np.random.randint(10, size = (10,10))


#6 Reshape a so that it is a two-dimensional array with the dimensions 10 by 10.

array_a_reshaped = array_a.reshape(10,10)


#7 Show the results of “a[4,5]”.
prob_7 = array_a_reshaped[4,5]


#8 Show the results of “a[4]”.
prob_8 = array_a_reshaped[4]

#9 Show the sum of d.
d_summed = array_d.sum()


#10 Show the max of a.
max_of_a = array_a.max()


#11 Show the transpose of b.
b_tranposed = array_b.transpose()



#12 Show the results of adding a and d.
sumAndD = array_a_reshaped + array_d


#13 Show the results of multiplying a and d.
aXd = array_a_reshaped * array_d


#14 Show the results of computing the dot product of a and d.
dot_multiply = np.dot(array_a_reshaped, array_d)



if __name__ == '__main__':

    print("\n Problem 2: Array A \n", array_a, "\n")

    print("Problem 3: Array B \n", array_b, "\n")

    print("Problem 4: Array C \n", array_c, "\n")

    print("Problem 5: Array D \n", array_d, "\n")

    print("Problem 6: Array A Reshaped \n", array_a_reshaped, "\n")

    print("Problem 7: Array A[4,5] \n", prob_7, "\n")

    print("Problem 8: Array A[4] \n", prob_8, "\n")

    print("Problem 9: Array D Sum \n", d_summed, "\n")

    print("Problem 10: Array A Max \n", max_of_a, "\n")

    print("Problem 11: Array B Transposed \n", b_tranposed, "\n")

    print("Problem 12: Array A & D Sum \n", sumAndD, "\n")

    print("Problem 13: Array A & D Multiplied \n", aXd, "\n")

    print("Problem 14: Array A & D Dot Multiply \n", dot_multiply, "\n")





