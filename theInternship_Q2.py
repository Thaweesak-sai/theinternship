"""
Floating Prime, The Internship Program 2020 second question
Created By Thaweesak Saiwongse (Note) 04/02/2020
"""

import math

def sieve(number):
    """ sieve function. A function to find all prime number from 1 to number
    implemented based on Sieve of Eratosthenes Algorithm
    Args:
        number (string) the string of number before the dot in float
    Returns:
        True if the number is a prime number
        False if not.
    """
    limit = int(number)
    limit+=1
    prime = []
    for i in range(2,limit):
        prime.append(i) #put all number from 2 to the limit to the array
    i=2
    while(i<=int(math.sqrt(number))):
        if i in prime:
            for j in range(i*2,limit,i):
                if j in prime:
                    prime.remove(j) #remove from the array if not a prime number
        i+=1
    if number in prime: #check if 
        return True
    return False
    
def moveDot(pos,string):
    """ moveDot function. A function to move the dot for 1 position
    Args:
        pos - Index of the dot in float
        string - the string of input from user
    Returns:
        string - the string after moving the dot backward one position
    """
    string = string[0:pos] + string[pos+1] + string[pos]+string[pos+2:]
    return string



def isFloatingPrime(buffer):
     """ isFloatingPrime. A function to control the process of checking floating prime

    Args:
        buffer - the whole string from user
    Returns:
        True if the input is a floating prime
        False if not
    """
    for i in range(3):
        pos = buffer.find('.') 
        buffer = moveDot(pos,buffer)
        pos = buffer.find('.')
        number = float(buffer[:pos])  #cut out only the digit in front of dot
        bPrime = sieve(number)
        if(bPrime==True):
            print(True)
            return 0
    print(False)

def checkDigit(buffer):
        """ checkDifit. A function to check the len of input string
        to be in the range up to 13 characters(12 numbers, 1 dot)

    Args:
        buffer - the whole string from user
    Returns:
        True if the input is in the range
        False if not
    """
    if(len(buffer)>13 or len(buffer)<=0):
        return False
    return True

def main():
    while True:
        buffer = input("Enter your number: ")
        if(buffer.find('.')==-1): #check if the input is float
            buffer=""
            print("Please enter only float number")
            continue
        if(checkDigit(buffer)==False): # check if the decimal exceeds 12 digits
            buffer=""
            print("The float is allowed up to 12 digits")
            continue
        if(float(buffer)<1 or float(buffer)>10): # check if input is in 1.0-10.0
            print("Please input 1.0-10.0 only")
            continue
        if len(buffer)<5: # if the input has the place value less than 3 digits
            buffer=buffer+"000" # to help index slicing works
        if(buffer=='0.0'):
            break
        isFloatingPrime(buffer)
    
if __name__ == '__main__':
    main()