"""
r: open an existing file for a read operation.
r+:  To read and write data into the file. The previous data in the file will be overridden.
"""

emp_file = open("employee.txt", "r")  # opens the file in read mode

print(emp_file.readable())  # prints True

content = emp_file.read()  # reads the content in the file
print(content)  # prints out all the content in the file

content = emp_file.read(3)
print(content)  # prints out 3 characters from a file

# To read line by line

print(emp_file.readline())  # reads individual line in the file.
print(emp_file.readlines())  # take all the lines inside a file and put them in a list
print(emp_file.readlines()[0])

# to print all the lines in a file
for employee in emp_file.readlines():
    print(employee)

# When you open a file, make sure to close the file.
emp_file.close()