num=int(input("enter num: "))
# def sumOfNat(a):
#     sum=0
#     i=1
#     for i in range(1,a+1):
#         sum=sum+i
#     print(sum)
# sumOfNat(num)

def sum(num):
    if(num==1):
        return 1
    return sum(num-1)+num
print(sum(num))