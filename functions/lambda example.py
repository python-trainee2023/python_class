# num=[1,2,3,4,5,6]
#
# even=list(filter(lambda x : x%2==0, num))
# print(even)
#
# square=list(map(lambda x : x**2, num))
# print(square)
#

operations= [lambda x,y:x+y , lambda x,y: x-y]

val1= operations[0](3,4)
val2=operations[1](4,3)
print(val1, val2)
