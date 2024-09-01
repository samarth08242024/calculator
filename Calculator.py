def add(number1, number2):
    return (number1+number2)

def subtract(number1, number2):
    return (number1-number2)

def multiply(number1, number2):
    return (number1*number2)

def divide(number1, number2):
    return (number1/number2)


while 1==1:
   
    numb1 = input("Enter first number:  ")
    n1=int(numb1)

    numb2 = input("Enter second number: ")
    n2=int(numb2)
    
    s = input("Enter the following- 1 for add, 2 for Subtract, 3 for multiply,  4 for divide and -100 for quit:  ")
    v=int(s)

    if v==1: 
        result = add(n1,n2)
        print(result)
    elif v==2:
        result = subtract(n1,n2)
        print(result)
    elif v==3:
        result = multiply(n1,n2)
        print(result)
    elif v==4:
        result = divide(n1,n2)
        print(result)

    elif v==-100:
        break
    else:
        print("Invalid Input")




 