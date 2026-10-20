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
        for s in students:
            file.write(
                f"Name: {s.name}\nAddress: {s.address}\nAge: {s.age}\nGrade: {s.grade}")
        file.close()
        print("Data saved successfully to Students.txt")

    def search(students, name):
        file = open("Students.txt", "r")

        for s in students:
            if s.name == name:
                print(
                    f"Name: {s.name}\nAddress: {s.address}\nAge: {s.age}\nGrade: {s.grade}")
                return
        print("Student not found.")

    name = input("Enter student name: ")
    students = []
    for i in range(name):
        name = input("Enter student name: ")
        address = input("Enter student address: ")
        age = input("Enter student age: ")
        grade = input("Enter student grade: ")
        s = Student(name, address, age, grade)
        students.append(s)

    save(students)


j = input("Do you want to search for a student? (yes/no): ")
if j == "yes":
     search = input("Enter student name to search: ")
     result = search(students, search)
     if result:
         print("Student found.")
    else:
        print("Student not found.")
    
elif j == "no":
    print("Exiting the program. Thank you!")
else:
    print("Please enter correct input")
