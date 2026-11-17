import mysql.connector

# Function to connect database
def connect_database():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="student_db"
        )

        if connection.is_connected():
            print("Database Connected Successfully!")

        return connection

    except mysql.connector.Error as e:
        print("Database Connection Error:", e)
        return None


# Function to add student
def add_student(connection):
    try:
        name = input("Enter Student Name: ")
        age = int(input("Enter Student Age: "))
        course = input("Enter Student Course: ")
        marks = int(input("Enter Student Marks: "))

        cursor = connection.cursor()

        query = "INSERT INTO students (name, age, course, marks) VALUES (%s, %s, %s, %s)"
        values = (name, age, course, marks)

        cursor.execute(query, values)
        connection.commit()

        print("Student Added Successfully!")

        cursor.close()

    except ValueError:
        print("Please enter valid numbers for age and marks.")

    except mysql.connector.Error as e:
        print("Add Student Error:", e)


# Function to create database
def create_database():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root"
        )

        cursor = connection.cursor()

        cursor.execute("CREATE DATABASE IF NOT EXISTS student_db")

        print("Database Created Successfully!")

        cursor.close()
        connection.close()

    except mysql.connector.Error as e:
        print("Database Creation Error:", e)


# Function to create table
def create_table(connection):
    try:
        cursor = connection.cursor()

        query = """
        CREATE TABLE IF NOT EXISTS students (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            age INT NOT NULL,
            course VARCHAR(100) NOT NULL,
            marks INT NOT NULL
        )
        """

        cursor.execute(query)

        print("Table Created Successfully!")

        cursor.close()

    except mysql.connector.Error as e:
        print("Table Creation Error:", e)


# Function to view students
def view_students(connection):
    try:
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM students")

        students = cursor.fetchall()

        if not students:
            print("No students found.")

        else:
            print("\nID\tName\tAge\tCourse\tMarks")
            print("---------------------------------------------")

            for student in students:
                print(student[0], "\t", student[1], "\t", student[2], "\t", student[3], "\t", student[4])

        cursor.close()

    except mysql.connector.Error as e:
        print("View Students Error:", e)


# Function to update student details
def update_student(connection):
    try:
        student_id = int(input("Enter Student ID to update: "))

        name = input("Enter New Name: ")
        age = int(input("Enter New Age: "))
        course = input("Enter New Course: ")
        marks = int(input("Enter New Marks: "))

        cursor = connection.cursor()

        query = """
        UPDATE students
        SET name = %s, age = %s, course = %s, marks = %s
        WHERE id = %s
        """

        values = (name, age, course, marks, student_id)

        cursor.execute(query, values)
        connection.commit()

        if cursor.rowcount > 0:
            print("Student details updated successfully!")
        else:
            print("Student ID not found.")

        cursor.close()

    except ValueError:
        print("Please enter valid numbers for ID, age and marks.")

    except mysql.connector.Error as e:
        print("Update Error:", e)


# Function to delete student
def delete_student(connection):
    try:
        student_id = int(input("Enter Student ID to delete: "))

        cursor = connection.cursor()

        query = "DELETE FROM students WHERE id = %s"

        cursor.execute(query, (student_id,))
        connection.commit()

        if cursor.rowcount > 0:
            print("Student deleted successfully!")
        else:
            print("Student ID not found.")

        cursor.close()

    except ValueError:
        print("Please enter a valid Student ID.")

    except mysql.connector.Error as e:
        print("Delete Error:", e)


# Main program
def main():
    create_database()

    connection = connect_database()

    if connection is None:
        print("Program stopped because database connection failed.")
        return

    create_table(connection)

    while True:
        print("\n======================================")
        print("     STUDENT MANAGEMENT SYSTEM")
        print("======================================")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")
        print("======================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student(connection)

        elif choice == "2":
            view_students(connection)

        elif choice == "3":
            update_student(connection)

        elif choice == "4":
            delete_student(connection)

        elif choice == "5":
            print("Thank you!")
            break

        else:
            print("Invalid choice. Please try again.")

    if connection.is_connected():
        connection.close()
        print("MySQL Connection Closed.")


if __name__ == "__main__":
    main()

