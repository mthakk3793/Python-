#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Maharshi Thakkar
# 06/21/2020
#"I have not given or received any unauthorized assistance on this assignment."
#https://youtu.be/C0VJCqnH6Q0

def location():
    """So in this function we attempt to determine where the file is located.
    By asking where it is we can then parse the input from the user to search for 
    specifically ".py." If this is located the user is able to move forward, 
    and if not they just get 0."""
    
    
    file_loc = input ("\n Hello, friend. I am your interactive grader. "
    "\n I will be asking you some questions to assess the grade for this assignment."
    "\n So first off, where is your file located?\n")           
                                                                #Asking for location of file
                                                                #and searcing for .py extension

    if '.py' not in file_loc: 
        print ("\n Your score for this assignment is 0.")       #Searching for .py, if not score
        return False                                            #is 0
    else:
        print ("\n You have passed the first problem!")         #Moves forward as .py was identified
        return True



def name():
    """For the name function we work with the user to admit if the assignment turned in
    has the author's name and date commented out at the top. If the user answers "yes" 
    they are able to move forward, and if not they just get 0."""
    
    nombre = input ("\n Next, you will assist me in informing me if this assignment has the"
    "\n author's name and submission date at the top. Is the authors name and submission"
    "\n date commented out at the top? (Yes or No)\n")          
                                                                #Asks user to identify author's name
                                                                #and date and then answer either 
                                                                #"yes" or "no"
    if nombre.upper() != "YES":
        print ("\n Your score for this assignment is 0.")       #All inputs are converted to uppercase
        return False                                            #Anything but "YES" gets a 0
    else: 
        print ("\n You have passed the second problem! Well done!")
        return True                                             
                                                                #Moves forward as the first condition
                                                                #was met

def statement():
    """For the name function we work with the user to admit if the assignment turned in
    has the honor code commented out at the top. If the user answers "yes" 
    they are able to move forward, and if not they just get 0."""
    
    honor_code = input('\n Is the honor code "I have not given or received any'
    '\n unauthorized assistance on this assignment;" commented out at the top'
    '\n of the assignment?(Yes or No)\n')                       
                                                                #Asks user to check if honor code
                                                                #answer either yes or no
        
    if honor_code.upper() != "YES":
        print ("\n Your score for this assignment is 0.")       #All inputs are converted to uppercase
        return False                                            #Anything but "YES" gets a 0
    else: 
        print ("\n You're a rockstar! Keep it up!")             #Moves forward as the first condition
        return True                                             #was met


def video():
    """For the name function we work with the user to admit if the assignment turned in
    has the youtube link commented out at the top. If the user answers "yes" 
    they are able to move forward, and if not they just get 0."""
    
    link = input ("\n So now, is there a youtube link commented out towards the top of"
    "\n assignment? (Yes or No)\n")                             
                                                                #Asks user to check if there is a 
                                                                #youtube link commented out at top
                                                                #and then to answer either "Yes" or "No"
    if link.upper() != "YES":
        print ("\n Your score for this assignment is 0.")       #All inputs are converted to uppercase
        return False                                            #Anything but "YES" gets a 0
    else: 
        print ("\n Congrats! We are just about halfway through!")
        return True                                             
                                                                #Moves forward as the first condition
                                                                #was met
        
        
def score():
    """The whole purpose of this function is to award points based on certain criteria. 
    As seen, a While loop is used for each grading criteria. As per the instructions in 
    the previous problems, if certain criteria didn't match they grader just gives a 0.
    In this case, there was no such criteria, and so a While Loop is neccessary to make
    sure the user continues to answer in some correct way to move forward. 
    Essentially if anything but a valid number (0-10) is put in the program will continue
    to harass the user to use something valid. A count is started at 0 to initiate it.
    Final grade is added at end to give a total score out of 40."""
    
    
    grade = 0                                                   #Initiating grade to be used and 
                                                                #called throughout the function
    while True:
        
        Q1 = input("\n You have done great so far. By passing the other 4 questions now"
        "\n we can move forward with computing your grade! “Out of ten points, how would"
        "\n you evaluate the correctness of the code?\n")
                                                                #Asks user to evaluate correctness
                                                                #out of 10 points 
        try:
            grade = int(Q1)                                     #Has grade equal to whatever user
        except:                                                 #inputs and converts to an integer      
            print("\n Please input a number!\n")                 
            continue                                            #Anything but a number is rejected
                                     
        
        if grade < 0 or grade > 10:
            print("\n Please input a number less than  or equal 10!\n")
            grade = 0 
            continue                                            #Restrain input to number between 0 and 10
        else:     
            break                                               #Break and move forward 
        
    while True:
        
        Q2 = input("\n This next question also worth 10 points. From a score of 0 to 10,"
        "\n How elegant is the code (data structure selection, algorithm efficiency, function"
        "\n implementation, etc.\n")
                                                                #Asks user to evaluate elegance of
                                                                #the code and award out of 10 points 
        
        try:                                                    #Has new_grade equal to whatever user
            new_grade = int(Q2)                                 #inputs and converts to an integer
        except:                                                 
            print("\n Please input a number!\n")                
            continue                                            #Anything but a number is rejected
        
        if new_grade < 0 or new_grade > 10:
            print("\n Please input a number between 0 and 10!\n")
            continue                                            #Restrain input to number between 0 and 10
        else:
            grade += new_grade                                  #Sums up input from original grade and
            break                                               #new_grade from this second While loop
            
                                                                #Break and move forward 
    
    while True:
        
        Q3 = input("\n Again out of 10, how would you rate the code hygiene"
        "\n white space, docstrings, etc.)\n")
                                                                #Asks user to rate code hygiene 
                                                                #out of 10 points
        
        try:
            new_grade = int(Q3)                                 #Has new_grade equal to whatever user
        except:                                                 #inputs and converts to an integer
            print("\n Please input a number!\n")
            continue                                            #Anything but a number is rejected
        
        if new_grade < 0 or new_grade > 10:
            print("\n Please input a number between 0 and 10!\n")
            continue                                            #Restrain input to number between 0 and 10
        else:
            grade += new_grade                                  #Sums up input from original grade and
            break                                               #new_grade from this second While loop
    
                                                                #Break and move forward 
    
    
    while True:
        
        Q4 = input("\n Lastly, what was the quality of the youtube video submitted"
        "\n out of 10 points? \n")
                                                                #Asks user to rate code hygiene
                                                                #out of 10 points
        try:                                               
            new_grade = int(Q4)                                 #Has new_grade equal to whatever user
        except:                                                 #inputs and converts to an integer
            print("\n Please input a number!\n")                 
            continue                                            #Anything but a number is rejected
        
        if new_grade < 0 or new_grade > 10:
            print("\n Please input a number between 0 and 10!\n")
            continue                                            #Restrain input to number between 0 and 10
        else:
            grade += new_grade                                  #Sums up input from original grade and
            break                                               #new_grade from this second While loop
    
    print("Total Points:\t" + str(grade))
    return grade                                                #Break and move forward 




def LateHW(grade): 
    """This last function takes points awareded from the last function, and then determines 
    how many points to cut off for a late assignment. Since total amount of points a user 
    can award is 40, and grading criteria is 1% loss per hour, that equates to 0.4 points 
    per hour. Again a while loop is used until user inputs a valid number. If user is to input 
    a number greater than or equal to 100 they automatically get 0. The final grade is then given 
    after any last deductions. """
    
    final_grade = 0                                             #Initiating final_grade to be used
                                                                #and called throughout the function 
    while True: 
        
        Q5 = input("\n Allright, you have made it to the end! This very last question"
        "\n is going to be regarding deductions of points based on late assignments."
        "\n How many hours late was your assignment turned in?\n")
                                                            
                                                                #Asks user to input # regarding how
        try:                                                    #late assignment was turned in
            Hours_late = int(Q5)
        except:
            print("\n Please input a whole number!\n")          #Only accepts whole numbers. No words or 
            continue                                            #partial credit on minutes
        if Hours_late >= 100:
            print("\n I'm sorry this assignment is too late to be turned in. Or there are "
                  "\n no points available for redemption. Your grade is 0. \n")
            return False 
        else:                                                   #Ends the loop is assignment is too late
            final_grade = float(grade) - 0.4*(float(Hours_late))        #or no available points left 
            if final_grade < 0:
                print ("\n There are no points available for redemption."
                "\n Your grade is 0.")
                return False                                    #Makes sure that program cannot output
            else:                                               #a negative grade 
                break
    print ("\nFinal grade:\t" + str(final_grade))
    return True                                                 #Takes grade calculated earlier and
                                                                #subtracts 0.4 points per hour late 

if __name__ == '__main__':
                                                                #Setting up entry point for main function
    if location() is False:
        exit()
    if name() is False:
        exit()                                                  #Exits loop if condition is not met 
    if statement() is False:
        exit()
    if video() is False:
        exit()
    
    grade = score()                                             #Score receives an integer and assigns it 
                                                                #to grade 
    if grade is False:
        exit()
        
    if LateHW(grade) is False:                                  #The Value in grade in line 240 gets passed 
        exit()                                                  #into the function LateHW
    
    exit()



# In[ ]:





# In[ ]:




