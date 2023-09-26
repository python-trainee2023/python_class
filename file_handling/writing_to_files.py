"""
w: open an existing file for a write operation. If the file already contains some data then it will be overridden
    but if the file is not present then it creates the file as well.
a:  open an existing file for append operation. It won’t override existing data.
w+: To write and read data. It will override existing data.
a+: To append and read data from the file. It won’t override existing data.
"""

emp_file = open("employee1.txt", "a")
emp_file.write("\nThis is an append command")

emp_file.close()