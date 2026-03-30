print("-------- recursion function ----------")
num=int(input("enetr number: "))

# def fact(a):
#     factorial =1
#     for i in range(1,a+1):
#         factorial=factorial*i
#     print(factorial)
# fact(num)


def fact(num):
    if(num==1 or num==0):
        return 1
    return num* fact(num-1)
print(f"factorial of {num} is : {fact(num)}")