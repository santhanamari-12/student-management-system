import mysql.connector

# ---------------- DATABASE CONNECTION ----------------

def connect_database():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="student_db"
        )

        if connection.is_connected():
            print("MySQL Database Connected Successfully!")
            return connection

    except mysql.connector.Error as e:
        print("Database Connection Error:", e)

    return None


# ---------------- ADD STUDENT ----------------

def add_student(connection):

    try:
        name = input("Enter Student Name: ")
        age = int(input("Enter Age: "))
        course = input("Enter Course: ")
        marks = int(input("Enter Marks: "))

        query = """
        INSERT INTO students (name, age, course,marks)
        VALUES (%s, %s, %s, %s)
        """

        values = (name, age, course, marks)

        cursor = connection.cursor()
        cursor.execute(query, values)

        connection.commit()

        print("Student Added Successfully!")

        cursor.close()

    except ValueError:
        print("Please enter valid numbers for Age and Marks.")

    except mysql.connector.Error as e:
        print("Error:", e)

# ---------------- CREATE DATABASE ----------------

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

# ---------------- CREATE TABLE ----------------

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

        print("Students Table Created Successfully!")

        cursor.close()

    except mysql.connector.Error as e:
        print("Table Creation Error:", e)


# ---------------- VIEW STUDENTS ----------------

def view_students(connection):

    try:
        query = "SELECT * FROM students"

        cursor = connection.cursor()
        cursor.execute(query)

        students = cursor.fetchall()

        if not students:
            print("No students found.")

        else:
            print("\n-----------------------------")
            print("ID | Name | Age | Course | Marks")
            print("-----------------------------")

            for student in students:
                print(
                    student[0],
                    "|",
                    student[1],
                    "|",
                    student[2],
                    "|",
                    student[3],
                    "|",
                    student[4]
                )

            print("-----------------------------")

        cursor.close()

    except mysql.connector.Error as e:
        print("Error:", e)


# ---------------- SEARCH STUDENT ----------------

def search_student(connection):

    try:
        student_id = int(input("Enter Student ID: "))

        query = "SELECT * FROM students WHERE id = %s"

        cursor = connection.cursor()
        cursor.execute(query, (student_id,))

        student = cursor.fetchone()

        if student:
            print("\nStudent Details")
            print("----------------------")
            print("ID     :", student[0])
            print("Name   :", student[1])
            print("Age    :", student[2])
            print("Course :", student[3])
            print("Marks  :", student[4])
        else:
            print("Student not found.")

        cursor.close()

    except ValueError:
        print("Please enter a valid Student ID.")

    except mysql.connector.Error as e:
        print("Error:", e)


# ---------------- UPDATE STUDENT ----------------

def update_student(connection):

    try:
        student_id = int(input("Enter Student ID to update: "))

        # Check student exists
        check_query = "SELECT * FROM students WHERE id = %s"

        cursor = connection.cursor()
        cursor.execute(check_query, (student_id,))

        student = cursor.fetchone()

        if not student:
            print("Student not found.")
            cursor.close()
            return

        print("\nEnter New Details")

        name = input("Enter New Name: ")
        age = int(input("Enter New Age: "))
        course = input("Enter New Course: ")
        marks = int(input("Enter New Marks: "))

        update_query = """
        UPDATE students
        SET name = %s,
            age = %s,
            course = %s,
            marks = %s
        WHERE id = %s
        """

        values = (name, age, course, marks, student_id)

        cursor.execute(update_query, values)

        connection.commit()

        print("Student Updated Successfully!")

        cursor.close()

    except ValueError:
        print("Please enter valid numbers.")

    except mysql.connector.Error as e:
        print("Error:", e)


# ---------------- DELETE STUDENT ----------------

def delete_student(connection):

    try:
        student_id = int(input("Enter Student ID to delete: "))

        # Check student exists
        check_query = "SELECT * FROM students WHERE id = %s"

        cursor = connection.cursor()
        cursor.execute(check_query, (student_id,))

        student = cursor.fetchone()

        if not student:
            print("Student not found.")
            cursor.close()
            return

        confirm = input(
            "Are you sure you want to delete this student? (yes/no): "
        )

        if confirm.lower() == "yes":

            delete_query = "DELETE FROM students WHERE id = %s"

            cursor.execute(delete_query, (student_id,))

            connection.commit()

            print("Student Deleted Successfully!")

        else:
            print("Delete operation cancelled.")

        cursor.close()

    except ValueError:
        print("Please enter a valid Student ID.")

    except mysql.connector.Error as e:
        print("Error:", e)


# ---------------- PASSED STUDENTS ----------------

def view_passed_students(connection):

    try:
        query = """
        SELECT * FROM students
        WHERE marks >= 50
        """

        cursor = connection.cursor()
        cursor.execute(query)

        students = cursor.fetchall()

        if len(students) == 0:
            print("No passed students found.")

        else:
            print("\n===== PASSED STUDENTS =====")

            print("-----------------------------------------------")
            print("ID | Name | Age | Course | Marks")
            print("-----------------------------------------------")

            for student in students:
                print(
                    student[0],
                    "|",
                    student[1],
                    "|",
                    student[2],
                    "|",
                    student[3],
                    "|",
                    student[4]
                )

            print("-----------------------------------------------")

        cursor.close()

    except mysql.connector.Error as e:
        print("Error:", e)


# ---------------- MAIN PROGRAM ----------------

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
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. View Passed Students")
        print("7. Exit")
        print("======================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student(connection)

        elif choice == "2":
            view_students(connection)

        elif choice == "3":
            search_student(connection)

        elif choice == "4":
            update_student(connection)

        elif choice == "5":
            delete_student(connection)

        elif choice == "6":
            view_passed_students(connection)

        elif choice == "7":
            print("Thank you!")
            break

        else:
            print("Invalid choice. Please try again.")

    # Close database connection
    if connection.is_connected():
        connection.close()
        print("MySQL Connection Closed.")


# // Main Startiing point
if __name__ == "__main__":
    main()