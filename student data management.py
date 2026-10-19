class Student:
    def init(self, name, address, age, grade):
        self.name = name
        self.address = address
        self.age = age
        self.grade = grade

    def save(students):
        file = open("Students.txt", "w")
        file.write(
            f"Name: {students.name}\nAddress: {students.address}\nAge: {students.age}\nGrade: {students.grade}")
