
st_num = int(input("Enter the start of the range: "))
end_num = int(input("Enter the end of the range: "))

if st_num>end_num:
    print("the start value must be less than the stop value Please enter again")
    st_num = int(input("Enter the start of the range: "))
    end_num = int(input("Enter the end of the range: "))

sum_numbers = lambda start, end, condition: sum(filter(condition, range(start, end + 1)))

even_sum = sum_numbers(st_num, end_num, lambda x: x % 2 == 0)

odd_sum = sum_numbers(st_num, end_num, lambda x: x % 2 != 0)

print(f"Sum of even numbers  {even_sum}")
print(f"Sum of odd numbers  {odd_sum}")