"""
class ContextManager:

    def __init__(self):
        pass

    def __enter__(self):
        pass
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass


with ContextManager("employee.txt", "r") as f:
    f.read()


"""

# class FileManger:
#     def __init__(self, filename, mode):
#         self.filename = filename
#         self.mode = mode
#
#     def __enter__(self):
#         self.file = open (self.filename, self.mode)
#         return self.file
#
#     def __exit__(self, exc_type, exc_value, exc_traceback):
#         self.file.close()


with open("employee.txt", "r") as source_file, open("new_employee.txt", "w") as destination_file:
    lines = source_file.readlines()
    for line in lines:
        destination_file.write(line.upper())

print(source_file.closed)
print(destination_file.closed)

