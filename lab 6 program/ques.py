import sqlite3


# Create a new database (or connect to an existing one)
conn = sqlite3.connect('student.db')
cursor = conn.cursor()

# Create a student table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        grade REAL
    )
''')

# Commit and close the connection


# Function to add a student to the database
def add_student(name, age, grade):
    conn = sqlite3.connect('student.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO students (name, age, grade) VALUES (?, ?, ?)', (name, age, grade))
    conn.commit()
    conn.close()

# Function to list all students in the database
def list_students():
    conn = sqlite3.connect('student.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM students')
    students = cursor.fetchall()
    conn.close()
    return students

# Function to search for students by name
def search_student_by_name(name):
    conn = sqlite3.connect('student.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM students WHERE name LIKE ?', ('%' + name + '%',))
    students = cursor.fetchall()
    conn.close()
    return students


while True:
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. List Students")
    print("3. Search Students by Name")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        grade = float(input("Enter student grade: "))
        add_student(name, age, grade)
        print("Student added successfully.")

    elif choice == '2':
        students = list_students()
        if students:
            print("\nList of Students:")
            for student in students:
                print(f"ID: {student[0]}, Name: {student[1]}, Age: {student[2]}, Grade: {student[3]}")
        else:
            print("No students found.")

    elif choice == '3':
        search_name = input("Enter student name to search: ")
        students = search_student_by_name(search_name)
        if students:
            print("\nSearch Results:")
            for student in students:
                print(f"ID: {student[0]}, Name: {student[1]}, Age: {student[2]}, Grade: {student[3]}")
        else:
            print("No matching students found.")

    elif choice == '4':
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please select a valid option.")

conn.commit()
conn.close()
