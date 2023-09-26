def sum_e_o(start,end):
    sum_even=0
    sum_odd=0
    for n in range(start,end+1):
        if n%2==0:
            sum_even+=n
        else:
            sum_odd+=n
    return  sum_odd,sum_even

start_range=int(input("Enter the start of the range: "))
stop_range=int(input("Enter the end of the range: "))

if start_range>stop_range:
    print("the start value must be less than the stop value Please enter again")
    start_range = int(input("Enter the start of the range: "))
    stop_range = int(input("Enter the end of the range: "))

odd_sum, even_sum = sum_e_o(start_range,stop_range)
print(" the values are ",odd_sum,"for odd and ", even_sum, "for even")

# 1 2 3 4 5 ,,,, 1 ,3 ,5 =9 ,,, 2,4=6
#1  2 3 4     5