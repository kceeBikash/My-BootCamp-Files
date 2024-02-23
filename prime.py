#checking prime numbers
def checkprime(num1):
    if num1<=1:
        return False
    for i in range(2, num1):
        if(num1%i==0):
            return False
    return True

#checking the range of prime numbers
def primerange(start,end):
    primenumbers=[]
    for i in range(start,end+1):
        if(checkprime(i)):
            primenumbers.append(i)
    return primenumbers
        
            
            