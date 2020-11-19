#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Maharshi Thakkar
# 07/30/2020
# "I have not given or received any unauthorized assistance on this assignment."
# https://youtu.be/sX-QVXBrrXc

"""Looking to create a list of palindrome dates for the 21st century."""

import os.path
from os import path

date = []                                       # Setup empty list to collect dates 

for i in range(2001,2100):                      # Only select the years for 21st century
    stri = ("% s" % i)                          # Convert all the numbers into strings
    together = (stri [::-1] + stri)             # Concatenate each year along with it's reverse for Palindrome
    
    date.append(together)                       # Append all of the strings into the container date
    
x = [i for i in date if int(str(i)[0:2]) < 32]  # Using list comprehension select strings only that start at 0
                                                # and go up to 32 for the days of each month
if path.exists("pando.txt"): 
    f = open("pando.txt","r+")                  # Overwrite the data to the text file pando.txt 
    f.truncate(0)
else:
    f = open("pando.txt", "x")                  # If file does not exist then it is setup here          

x = sorted(x)                                   # Sorts the data by the months of the year 
for y in x:
    print (y[0:2] + "/0" + str(y[3:4]) + "/" + y[4:]) 
    f.writelines(y[0:2] + "/0" + str(y[3:4]) + "/" + y[4:] + "\n") 
f.close()                                       # Prints it so it has the slashes, and includes 0 as python 
                                                # omits this
                                                # Writes all of this data to pando.txt 
    

    
   
    


# In[ ]:


import os.path
from os import path

date = []                                       # Setup empty list to collect dates 

for i in range(2001,2100):                      # Only select the years for 21st century
    stri = ("% s" % i)                          # Convert all the numbers into strings
    together = (stri [::-1] + stri)             # Concatenate each year along with it's reverse for Palindrome
    
    date.append(together)                       # Append all of the strings into the container date
    
print(date)


# In[ ]:


import os.path
from os import path

date = []                                       # Setup empty list to collect dates 

for i in range(2001,2100):                      # Only select the years for 21st century
    stri = ("% s" % i)                          # Convert all the numbers into strings
    together = (stri [::-1] + stri)             # Concatenate each year along with it's reverse for Palindrome
    
    date.append(together)                       # Append all of the strings into the container date
    
x = [i for i in date if int(str(i)[0:2]) < 32]  # Using list comprehension select strings only that start at 0
                                                # and go up to 32 for the days of each month
print (x)
    
   


# In[ ]:




