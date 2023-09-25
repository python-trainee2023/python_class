def check(n):
    if n<=0:
        return
    else:
        print(n)
        check(n-1)

check(6)