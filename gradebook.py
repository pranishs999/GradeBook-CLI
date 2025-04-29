import os

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = {}

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def get_average_grade(self):
        if self.grades:
            return sum(self.grades.values()) / len(self.grades)
        return 0

    def __str__(self):
        return f"{self.name}: {self.grades}"

    def delete_grade(self, subject):
        if subject in self.grades:
            del self.grades[subject]
        else:
            print(f"No grade found for {subject}.")

class Gradebook:
    def __init__(self):
        self.students = {}
        self.filename = "gradebook.txt"

    def add_student(self, name):
        if name not in self.students:
            self.students[name] = Student(name)
            self.save_to_file()  # Auto-save after adding a student
        else:
            print(f"Student {name} already exists.")

    def add_grade(self, name, subject, grade):
        if name in self.students:
            self.students[name].add_grade(subject, grade)
            self.save_to_file()  # Auto-save after adding a grade
        else:
            print(f"Student {name} does not exist.")

    def delete_student(self, name):
        if name in self.students:
            del self.students[name]
            self.save_to_file()  # Auto-save after deleting a student
            print(f"Student {name} has been deleted.")
        else:
            print(f"Student {name} not found.")

    def delete_grade(self, name, subject):
        if name in self.students:
            self.students[name].delete_grade(subject)
            self.save_to_file()  # Auto-save after deleting a grade
            print(f"Grade for {subject} deleted.")
        else:
            print(f"Student {name} not found.")

    def view_grades(self):
        if not self.students:
            print("No students in the gradebook.")
        for student in self.students.values():
            print(student)

    def view_student(self, name):
        if name in self.students:
            print(self.students[name])
        else:
            print(f"Student {name} not found.")

    def save_to_file(self):
        with open(self.filename, "w") as file:
            for student in self.students.values():
                file.write(f"{student.name}: {student.grades}\n")

    def load_from_file(self):
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    if not line.strip():
                        continue
                    
                    try:
                        name, grades_str = line.strip().split(": ")
                        name = name.strip()
                        grades = eval(grades_str)
                        
                        if isinstance(grades, dict):
                            student = Student(name)
                            for subject, grade in grades.items():
                                student.add_grade(subject, grade)
                            self.students[name] = student
                        else:
                            print(f"Invalid grades format for student {name}. Skipping this line.")
                    except ValueError:
                        print(f"Skipping malformed line: {line.strip()}")
        except FileNotFoundError:
            print(f"{self.filename} not found. Starting with an empty gradebook.")

    def delete_file(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)
            print(f"{self.filename} has been deleted.")
        else:
            print(f"{self.filename} not found.")

def main():
    gradebook = Gradebook()
    gradebook.load_from_file()  # Load previous data from the file

    while True:
        print("\n--- Gradebook ---")
        print("1. Add Student")
        print("2. Add Grade")
        print("3. View All Grades")
        print("4. View Student Grades")
        print("5. Delete Student")
        print("6. Delete Grade")
        print("7. Delete Gradebook File")
        print("8. Exit")
        
        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter student's name: ")
            gradebook.add_student(name)
        
        elif choice == "2":
            name = input("Enter student's name: ")
            subject = input("Enter subject: ")
            try:
                grade = float(input("Enter grade: "))
                gradebook.add_grade(name, subject, grade)
            except ValueError:
                print("Invalid grade. Please enter a numeric value.")
        
        elif choice == "3":
            gradebook.view_grades()
        
        elif choice == "4":
            name = input("Enter student's name: ")
            gradebook.view_student(name)
        
        elif choice == "5":
            name = input("Enter student's name to delete: ")
            gradebook.delete_student(name)
        
        elif choice == "6":
            name = input("Enter student's name: ")
            subject = input("Enter subject to delete grade: ")
            gradebook.delete_grade(name, subject)
        
        elif choice == "7":
            gradebook.delete_file()
        
        elif choice == "8":
            print("Exiting...")
            break
        
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
