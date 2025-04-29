# Gradebook Management System

A simple gradebook management system built using Python that allows you to add students, record grades, view student records, and delete records. The data is stored in a text file (`gradebook.txt`), and the program provides functionality to manage and interact with student grades.

## Features

- **Add Student**: Allows you to add a new student to the gradebook.
- **Add Grade**: Allows you to add grades for a student in a specific subject.
- **View All Grades**: Displays the grades of all students in the gradebook.
- **View Student Grades**: Displays the grades of a specific student.
- **Delete Student**: Deletes a student from the gradebook.
- **Delete Grade**: Deletes a specific grade for a student in a given subject.
- **Delete Gradebook File**: Deletes the entire gradebook file (`gradebook.txt`), removing all student data.
- **Exit**: Exits the application.

## Technologies Used

- Python 3.x
- File Handling (using text files)

## How It Works

The application is built using Python and employs object-oriented programming principles. It consists of two primary classes:

1. **Student Class**:

   - Represents a student, storing their name and grades.
   - Allows adding grades, calculating average grades, and deleting specific grades.
2. **Gradebook Class**:

   - Manages a collection of students and provides methods for adding, deleting, and viewing students and their grades.
   - Automatically saves data to a file (`gradebook.txt`) to ensure persistence across application runs.
   - Supports loading data from the file upon startup and saving data when changes are made.

## Requirements

- Python 3.x installed.

## Running the Project

1. Clone or download the repository.
2. Open a terminal and navigate to the project directory.
3. Run the script using the following command:

   ```bash
   python3 gradebook.py
   ```
4. Follow the on-screen menu to interact with the gradebook system.

## Example Usage

## Adding a Student

   --- Gradebook ---

1. Add Student
2. Add Grade
3. View All Grades
4. View Student Grades
5. Delete Student
6. Delete Grade
7. Delete Gradebook File
8. Exit
   Select an option: 1
   Enter student's name: John Doe
   Student John Doe has been added.

## Adding a Grade

   --- Gradebook ---

1. Add Student
2. Add Grade
3. View All Grades
4. View Student Grades
5. Delete Student
6. Delete Grade
7. Delete Gradebook File
8. Exit
   Select an option: 2
   Enter student's name: John Doe
   Enter subject: Math
   Enter grade: 95
   Grade for Math added for John Doe.

## Viewing All Grades

   --- Gradebook ---

1. Add Student
2. Add Grade
3. View All Grades
4. View Student Grades
5. Delete Student
6. Delete Grade
7. Delete Gradebook File
8. Exit
   Select an option: 3
   John Doe: {'Math': 95}

## Deleting a Grade

   --- Gradebook ---

1. Add Student
2. Add Grade
3. View All Grades
4. View Student Grades
5. Delete Student
6. Delete Grade
7. Delete Gradebook File
8. Exit
   Select an option: 6
   Enter student's name: John Doe
   Enter subject to delete grade: Math
   Grade for Math deleted.

## Deleting a Student

   --- Gradebook ---

1. Add Student
2. Add Grade
3. View All Grades
4. View Student Grades
5. Delete Student
6. Delete Grade
7. Delete Gradebook File
8. Exit
   Select an option: 5
   Enter student's name to delete: John Doe
   Student John Doe has been deleted.

## File Structure

-**(`gradebook.txt`)**: A text file that stores student data (names and grades). Each line represents a student and their grades in a dictionary format.

## Future Enhancements

   **Graphical User Interface (GUI)**: A GUI using a framework like Tkinter or Flask to make the gradebook more user-friendly.

   **File Format**: Change the file format from plain text to CSV or JSON for better structure and easy parsing.

   **Advanced Features**: Features such as sorting, filtering, and detailed grade reports for students could be added.

## License

This project is open-source and available under the MIT License.
