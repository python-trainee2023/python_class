# #rashila
# num_list = [2,4,5,6,3,9]
# even=[]
# for i in num_list:
#     if i%2!=0:
#         continue
#     else:
#         even.append(i)
# print(even)
#
# #pema
# number_list = [2, 4, 5, 9, 18, 20]
# filtered_list = [x for x in number_list if x % 2 == 0]
# print(filtered_list)

# #priya
# numbers=[2,4,5,9,18,20]
#
# result_List=[]
# for num in numbers:
#     if num%2 == 0:
#         result_List.append(num)
#         numbers =result_List
# print(numbers)

# #sonal
# num = [2,4,5,9,18,20]
# new=[]
# count = 0
# for i in num:
#     print(i)
#     if (i % 2) == 0:
#         print("hi")
#         # new.append(i)
#         new[count] = i
#         count+=1
# print(new)

num = [2,4,5,9,18,20]
new=[]
count = 0
for i in num:
    if (i % 2) == 0:
        # new.append(i)
        new.insert(count, i)
        count+=1
print(new)