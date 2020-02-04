import math
def sieve(number):
    limit = int(number)
    limit+=1
    prime = []
    for i in range(2,limit):
        prime.append(i)
    i=2
    while(i<=int(math.sqrt(number))):
        if i in prime:
            for j in range(i*2,limit,i):
                if j in prime:
                    prime.remove(j)
        i+=1
    if number in prime:
        return True
    return False
    
def moveDot(pos,string):
    string = string[0:pos] + string[pos+1] + string[pos]+string[pos+2:]
    return string



def isFloatingPrime(buffer):
    for i in range(3):
        pos = buffer.find('.')
        buffer = moveDot(pos,buffer)
        pos = buffer.find('.')
        number = float(buffer[:pos])
        bPrime = sieve(number)
        if(bPrime==True):
            print(True)
            return 0
    print(False)
    
        


def checkdigit(buffer):
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
        if(checkdigit(buffer)==False): # check if the decimal exceeds 12 digits
            buffer=""
            print("The float is allowed up to 12 digits")
            continue
        if(float(buffer)<1 or float(buffer)>10):
            print("Please input 1.0-10.0 only")
            continue

        if(buffer=='0.0'):
            break
        isFloatingPrime(buffer)
    
if __name__ == '__main__':
    main()