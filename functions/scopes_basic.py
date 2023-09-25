# # o_var=43
# def first_func():
#     i_var=87
#     # print(o_var)
#     print(i_var)
#
# first_func()

o_var=87
def o_func():
    o_var=43 #enclosing scope
    def i_func():

        print(o_var)
    i_func()

o_func()

# LEGB rule