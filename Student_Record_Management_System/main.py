import json
import os


DATA_FILE = "students.json"


class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def show_details(self):
        print(f"Name: {self._name}")
        print(f"Age: {self._age}")


class Student(Person):
    def __init__(self, student_id, name, age, course, marks):
        super().__init__(name, age)
        self.student_id = student_id
        self.course = course
        self._marks = marks

    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self, new_marks):
        if 0 <= new_marks <= 100:
            self._marks = new_marks
        else:
            raise ValueError("Marks must be between 0 and 100.")

    def calculate_grade(self):
        if self._marks >= 90:
            return "A"
        elif self._marks >= 80:
            return "B"
        elif self._marks >= 70:
            return "C"
        elif self._marks >= 60:
            return "D"
        else:
            return "F"

    def show_details(self):
        super().show_details()
        print(f"Student ID: {self.student_id}")
        print(f"Course: {self.course}")
        print(f"Marks: {self._marks}")
        print(f"Grade: {self.calculate_grade()}")


class StudentRecordSystem:
    def __init__(self):
        self.students = []
        self.load_students()

    def load_students(self):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as file:
                saved_students = json.load(file)

            for item in saved_students:
                student = Student(
                    item["student_id"],
                    item["name"],
                    item["age"],
                    item["course"],
                    item["marks"]
                )
                self.students.append(student)

        except FileNotFoundError:
            self.students = []
        except json.JSONDecodeError:
            print("The saved student file is empty or damaged. Starting with no records.")
            self.students = []
        except (KeyError, TypeError, ValueError) as error:
            print(f"Some saved student data could not be loaded: {error}")
            self.students = []

    def save_students(self):
        saved_students = []

        for student in self.students:
            saved_students.append({
                "student_id": student.student_id,
                "name": student._name,
                "age": student._age,
                "course": student.course,
                "marks": student.marks
            })

        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(saved_students, file, indent=4)

    def find_student(self, student_id):
        for student in self.students:
            if student.student_id.lower() == student_id.lower():
                return student
        return None

    def add_student(self):
        print("\n--- Add Student ---")
        student_id = input("Enter student ID: ").strip()

        if not student_id:
            print("Student ID cannot be empty.")
            return

        if self.find_student(student_id):
            print("That student ID already exists.")
            return

        name = input("Enter student name: ").strip()
        if not name:
            print("Student name cannot be empty.")
            return

        course = input("Enter course or class: ").strip()
        if not course:
            print("Course cannot be empty.")
            return

        try:
            age = int(input("Enter age: "))
            marks = float(input("Enter marks (0-100): "))

            if age <= 0:
                print("Age must be a positive number.")
                return

            if not 0 <= marks <= 100:
                print("Marks must be between 0 and 100.")
                return

            student = Student(student_id, name, age, course, marks)
            self.students.append(student)
            self.save_students()
            print("Student added successfully.")

        except ValueError:
            print("Please enter a valid number for age and marks.")

    def view_students(self):
        print("\n--- All Students ---")

        if not self.students:
            print("No student records found.")
            return

        for student in self.students:
            print("\n--------------------")
            student.show_details()

    def search_student(self):
        print("\n--- Search Student ---")
        student_id = input("Enter the student ID: ").strip()
        student = self.find_student(student_id)

        if student:
            student.show_details()
        else:
            print("Student not found.")

    def update_student(self):
        print("\n--- Update Student ---")
        student_id = input("Enter the student ID to update: ").strip()
        student = self.find_student(student_id)

        if not student:
            print("Student not found.")
            return

        print("Press Enter to keep the current value.")
        new_name = input(f"Name [{student._name}]: ").strip()
        new_course = input(f"Course [{student.course}]: ").strip()
        new_age = input(f"Age [{student._age}]: ").strip()
        new_marks = input(f"Marks [{student.marks}]: ").strip()

        try:
            if new_name:
                student._name = new_name

            if new_course:
                student.course = new_course

            if new_age:
                age = int(new_age)
                if age <= 0:
                    print("Age must be positive. Age was not changed.")
                else:
                    student._age = age

            if new_marks:
                student.marks = float(new_marks)

            self.save_students()
            print("Student record updated.")

        except ValueError:
            print("Invalid age or marks. Please check the values and try again.")

    def delete_student(self):
        print("\n--- Delete Student ---")
        student_id = input("Enter the student ID to delete: ").strip()
        student = self.find_student(student_id)

        if not student:
            print("Student not found.")
            return

        confirm = input(
            f"Delete {student._name} ({student.student_id})? Enter y to confirm: "
        ).strip().lower()

        if confirm == "y":
            self.students.remove(student)
            self.save_students()
            print("Student deleted.")
        else:
            print("Deletion cancelled.")

    def show_average_marks(self):
        if not self.students:
            print("No student records available.")
            return

        average = sum(student.marks for student in self.students) / len(self.students)
        print(f"Average marks of all students: {average:.2f}")

    def run(self):
        while True:
            print("\n===== Student Record Management System =====")
            print("1. Add Student")
            print("2. View All Students")
            print("3. Search Student")
            print("4. Update Student")
            print("5. Delete Student")
            print("6. Show Average Marks")
            print("7. Exit")

            choice = input("Choose an option (1-7): ").strip()

            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.view_students()
            elif choice == "3":
                self.search_student()
            elif choice == "4":
                self.update_student()
            elif choice == "5":
                self.delete_student()
            elif choice == "6":
                self.show_average_marks()
            elif choice == "7":
                print("Thank you for using the Student Record Management System.")
                break
            else:
                print("Invalid choice. Please select a number from 1 to 7.")


if __name__ == "__main__":
    system = StudentRecordSystem()
    system.run()

        