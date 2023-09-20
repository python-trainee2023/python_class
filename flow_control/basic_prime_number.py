n= int(input("please enter a number:: "))
if n == 0 or n == 1:
    print("please enter any other number than 0 or 1. they are neither prime nor composite:")
    n = int(input("the other number:: "))
count = 0
for i in range(1, n):
    if n % i == 0:
        count += 1
if count > 2:
    print(n, "isn't prime")
else:
    print(n, "is prime")
