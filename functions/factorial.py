def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


val = int(input("Enter a positive integer: "))
if val < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"The factorial of {val} is {factorial(val)}.")