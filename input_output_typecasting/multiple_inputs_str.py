# ip_str = input("Enter multiple values separated by space: ")
# input_list = ip_str.split()
#
# int_values = []
# str_values = []
#
# for item in input_list:
#     if item.isdigit():
#         int_values.append(int(item))
#     else:
#         str_values.append(item)
#
# print("Integers:", int_values)
# print("Strings:", str_values)
#
user_input = input("enter mulitple values, separate by commma")
lists = user_input.split(',')
print("Given values:",lists)
strings = [x for x in lists if not x.isdigit()]
integers = [int(x) for x in lists if x.isdigit()]
print("Strings:",strings)
print("Integers:",integers)

# user_input = input("Enter multiple values seperated by a comma: ")
#
# values = user_input.split(",")
#
# int_list = [x for x in values if type(x) == int]
#
# float_list = [y for y in values if type(y) == float]
#
# string_list = [z for z in values if type(z) == str]
#
# print("Integer list: ", int_list)
#
# print("Float list: ", float_list)

# print("String list: ", string_list)