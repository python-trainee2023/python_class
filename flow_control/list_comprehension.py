numbers=[2,4,5,9,18,20]
res_list=[]
for i in numbers:
    if i % 2 ==0:
        res_list.append(i)
print(res_list)

#pema
number_list = [2, 4, 5, 9, 18, 20]
filtered_list = [x for x in number_list if x % 2 != 0]
print(filtered_list)

num_list=list(range(1,10))
print(num_list)
square=[x ** 2 for x in num_list]
print(square)

fruits=["apple","kiwi", "banana"]
upper_case_fruits=[x.upper() for x in fruits ]
print(upper_case_fruits)

