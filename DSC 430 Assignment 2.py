#!/usr/bin/env python
# coding: utf-8

# In[14]:


#Maharshi Thakkar
# 06/25/2020
#"I have not given or received any unauthorized assistance on this assignment."
#https://youtu.be/SSXEBeTpXSk



def coprime(a,b):            
    """So for this function we are basically checking to see if numbers are coprime. This is done having the 
    formula caluculate if the two numbers are able to ever obtain remainders and if so that means they're 
    clearly divisable. Two coprime number would not be work properly and therefore qualify to return False."""   
    
    for cp in range(2, min(a,b)+ 1):                        #Starts at range of 2 and goes up to the smallest 
        if a % cp == 0:                                     #available between the two. The 1 is of course 
            if b % cp == 0:                                 #because range needs to include the number itself. 
                return False                                #Then both numbers check to see if they they return
    return True                                             #a remainder of 0 which would mean at some point 
                                                            #the number are divisable by something other than 1
                                                            #and therefore it would return false (not coprime)


def coprime_test_loop(): 
    """Testing to see if two numbers user inputs are coprime or not. User has the option to 
    stop after the first round or keep playing if they so choose."""
    
                                                            #Initalizes a and b for to be referenecd 
    a = int(input("Please enter your first #"))             #throughout the program
        
    b = int(input("Please enter your second #"))    
        
    
    
    while True:   
                                                            #Calls the coprime function with the input of 
                                                            #a and b and checks if its either true or false
        if coprime(a,b) is True:                    
            print("You have selected two numbers that are coprime!")
        else:
            print("You have selected two numbers that are not coprime!")
                                                            
        Coprime_game = ""                                   #Initalizes the coprime game with an empty string
                                                            #to be used outside of the nested while loop 
                                                            #in order to be referenced outside of its declaration,
                                                            #and the input will be of type string
        while True:
                                                            
            Coprime_game = input("Is this fun?! Want to play again? (Yes or no) ")
            Coprime_game = Coprime_game.upper()            
                                                            #Check to make sure either yes or no is picked
            if Coprime_game.upper() != "YES" and Coprime_game.upper() != "NO":
                print("Please select either YES or NO")
                continue                                    #Continues on and goes from the start 
            else:                                           #of the nested while loop
                break
                                                            #we have reached a valid answer of yes or 
                                                            #no and break out of the nested loop
                
                
        if Coprime_game == "YES":                           #Runs the game again, and since a and b are
                                                            #declared outside of the while loop and in line 21
                                                            #we call coprime(a, b), we don't have to call coprime
                                                            #once again as it would be redundant and useless.
            
            a = int(input("Please enter your first #"))    
            
            b = int(input("Please enter your second #"))        
                                                            #Initalizes a and b for to be reference
                                                            #throughout the program
                
            continue                                                                
        else:        
            
            print("Awh so sad to see you leave. Thanks for playing COPRIME!!")                                          
            return 
           
                                                            #Terminates the program if it's NO
            

if __name__ == '__main__':
    coprime_test_loop()
    
    
    
    
    


# In[12]:


13%12


# In[ ]:





# In[ ]:




