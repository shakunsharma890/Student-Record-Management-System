Student Record Management System

Project Description
A beginner-friendly Python terminal application for storing and managing student records. It supports adding, viewing, searching, updating, and deleting students. Student records are saved locally in a JSON file so they remain available after the program closes.
Features
- Add student records with a unique student ID
- View all saved students
- Search for a student by ID
- Update student information
- Delete a record after confirmation
- Calculate a student's grade from their marks
- Calculate average marks across all saved students
- Save and load records using JSON
- Handle common invalid input and missing-file situations

Technologies Used
- Python 3
- JSON
- Built-in os module

Python Concepts Used
- Variables, data types, input/output, operators, and type conversion
- Conditional statements and loops
- Functions and methods
- Lists and dictionaries
- File handling and JSON
- Exception handling
- Classes and objects
- Constructors and inheritance
- Encapsulation through properties
- Method overriding (polymorphism)

Installation / Setup
1. Install Python 3.
2. Download or clone this repository.
3. Open the project folder in a terminal or VS Code.
No third-party packages are required.

How to Run
Run this command from the project folder:
python3 main.py
The program creates students.json in the working folder when student records are saved.

Project Workflow
1. Start the program and select an option from the menu.
2. Enter the requested student details.
3. The program validates the input and checks for duplicate IDs.
4. Records are saved to students.json.
5. Existing records are loaded the next time the program starts.

Future Improvements
- Store separate subject marks and calculate an overall average
- Add sorting and filtering options
- Export records to CSV
- Add a graphical user interface
- Add user login and access permissions
- Improve data validation and add automated tests

Author
Shakun Sharma

GitHub Repository
https://github.com/shakunsharma890/Student-Record-Management-System
