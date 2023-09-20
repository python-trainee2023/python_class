a = {1, 2, 4}

b = {6, 7, 9}

union_ex = a | b
print(union_ex)

a.add(10)
a.add(30)
print(a)
a.remove(10)
print(a)

values_to_be_added = {12,10}
a.update(values_to_be_added)
print(a)