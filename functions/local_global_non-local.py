
def o_func():
    o_var=54

    def i_func():
        nonlocal o_var
        o_var+=6

    i_func()
    print(o_var)
o_func()

# user input cube