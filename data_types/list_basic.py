mx_list = [1, "RAM", 78.4]
empty_ls = []
test_list = [10, 3, 20, 55, 30]
st_list = ["string", "list", "pyton"]
print(test_list[1])

empty_ls.append("first")
print(empty_ls)
empty_ls.remove("first")
print(empty_ls)


original_list=[10,20,30,60]
original_list.insert(3,33) #adds 33 to the 3rd index place will give [10, 20, 30, 33, 60]
print(original_list)
extend_val=[1,4,2]
original_list.extend(extend_val)
print(original_list)