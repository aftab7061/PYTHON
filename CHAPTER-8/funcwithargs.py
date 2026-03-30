print("-------- function with arguments----------")
a=int(input("enetr num1: "))
b=int(input("enetr num2: "))

def add(num1,num2):
    sum=num1*num2
    print("addition: ",sum)

def sub(num1,num2):
    subt=num1-num2
    print("subtraction: ",subt)

def mult(num1,num2):
    mul=num1*num2
    print("multiplication: ",mul)   
    
add(a,b)
sub(a,b)
mult(a,b)