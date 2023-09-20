
count=0

while count<5:
    print(count)
    count+=1
print(" ")


ex_list=["a","b","c"]
for i in ex_list:
    if i=="b":
        continue
    print(i, "is the value printed")
print(" ")

for num in range(5):
    if num==3:
        print("3 number is found")
        break
else:
    print("not found in this range")

