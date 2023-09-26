with open('student.txt','r') as source_file, open('new_student.txt','a') as dest_file:

    # content=source_file.read()
    # lines=source_file.readlines()
    for line in source_file:
        content_upper=line.upper()
        dest_file.write(content_upper)
print("data copied")
print(source_file.closed)