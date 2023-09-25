def fib(items):
    if items<=0:
        print("enter a positive number")
        items=int(input("enter the positive number here:: "))
    else:
        print(f"displaying  {items} number of terms for the sequence")

    fib_seq=[0,1]
    while len(fib_seq)<items:
        next_term=fib_seq[-2]+fib_seq[-1]
        fib_seq.append(next_term)
    return fib_seq

n=int(input("enter the number of fibonacci terms to be displayed  "))
series=fib(n)
print("the sequence is :: ")
print(series)