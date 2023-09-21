input_str = input("Enter multiple integers separated by space: ")
input_list = input_str.split()

int_values = [int(x) for x in input_list]

print("You entered:", int_values)