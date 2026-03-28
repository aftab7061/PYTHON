num=int(input("enter number: "))

for i in range(2,num):
    if(num % i == 0):
        print("This number is not prime number: ",num)
        break
else:
    print("This number is prime number: ",num)