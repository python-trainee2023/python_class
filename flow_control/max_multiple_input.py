


# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# num3 = float(input("Enter the third number: "))
#
# largest=max(num1, num2, num3)
# print(f"The largest number is: {largest}")

#rejan
user_input = input('Enter 3 numbers')
input_list = list(user_input.split(','))

num_list = [int(x) for x in input_list]

num_list.sort()


print(num_list[len(num_list)-1])