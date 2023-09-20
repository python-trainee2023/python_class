def prime(num):
    count=0
    for i in range(1,num):
        if num%i==0:
            count+=1
    return count

n=int(input("please entera number:: "))
if n== 0 or n==1:
    print("please enter any other number than 0 or 1. they are neither prime nor composite:")
    n=int(input("the other number:: "))
pr=prime(n)
if pr>2:
    print(n,"isn't prime")
else:
    print(n,"is prime")

