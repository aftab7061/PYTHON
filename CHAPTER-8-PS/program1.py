num1=int(input("enter num1: "))
num2=int(input("enter num2: "))
num3=int(input("enter num3: "))

def great(a,b,c):
    if(a>b and a>c):
        print("greatest number of: ",a)
    elif(b>a and b>c):
        print("greatest number of: ",b)
    else:
        print("greatest number of: ",c)
great(num1,num2,num3)