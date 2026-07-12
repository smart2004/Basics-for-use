class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print(self.name, self.age)
s1 = Student('Mark', 50)
s1.display()
