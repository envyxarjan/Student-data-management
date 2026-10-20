
class Student:
    def __init__(self, name, address, age, grade):
        self.name = name
        self.address = address
        self.age = age
        self.grade = grade


def save_students(students):
    with open("Students.txt", "w") as file:
        for s in students:
            file.write(
                f"Name: {s.name}\nAddress: {s.address}\nAge: {s.age}\nGrade: {s.grade}")

    print("Data saved successfully to Students.txt")


def search_student(students, name):
    for s in students:
        if s.name.lower() == name.lower():
            print("\nStudent found!")
            print(f"Name: {s.name}")
            print(f"Address: {s.address}")
            print(f"Age: {s.age}")
            print(f"Grade: {s.grade}")
            return True

    print("Student not found.")
    return False


students = []

number = int(input("How many students do you want to add? "))

for i in range(number):
    print(f"\nEnter details for student {i + 1}")

    name = input("Enter student name: ")
    address = input("Enter student address: ")
    age = input("Enter student age: ")
    grade = input("Enter student grade: ")

    s = Student(name, address, age, grade)
    students.append(s)

save_students(students)

choice = input(
    "\nDo you want to search for a student? (yes/no): ").strip().lower()

if choice == "yes":
    search_name = input("Enter student name to search: ")
    search_student(students, search_name)

elif choice == "no":
    print("Exiting the program. Thank you!")

else:
    print("Please enter correct input.")
