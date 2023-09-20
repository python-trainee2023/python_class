class Student:
    def __init__(self, student_id, name,rank):
        self.student_id = student_id
        self.identify = name
        self.rank=rank

    def introduce(self):
        return f"Hi, I'm {self.identify}, and my student ID is {self.student_id}. MY rank is {self.rank}"


# Creating objects (instances) of the Student class
student1 = Student(501, "A","first")
student2 = Student(502, "B","second")

# Accessing attributes and calling methods on objects
print(student1.introduce())
print(student2.introduce())


