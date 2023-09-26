# try:
#     source_file= open('teacher.txt','r')
#
#     content=source_file.read()
#
#
#     print(source_file.closed)
# except NameError:
#     print("the name hasn't been defined")
# except FileNotFoundError:
#     print("the file is not present")
# #
# # finally:
# #     source_file.close()

x=-2
if x<0:
    raise ValueError("x can't be less than 0")