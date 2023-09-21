


input_str = input("Enter multiple integers separated by comma: ")
input_list = input_str.split(',')

int_values = [float(x) for x in input_list]
max_val=max(int_values)
print(max_val)