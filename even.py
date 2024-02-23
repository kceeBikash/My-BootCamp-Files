#checking even numbers
def checkeven(num1):
    if(num1%2==0):
        return "it is even"
    else:
        return "it is not even"
    
#checking even numbers range
def evenrange(start, end):
    result=[]
    for num in range(start, end+1):
        if(num%2==0):
            result.append(num)
    return result


 

    
    