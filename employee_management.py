import mysql.connector #This loads the MySQL Connector library into your Python program.
#Connect Python to MySQL
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="employee_database"
)
print("Connection to MySQL database established successfully.")
# Check Employee function......................................
#Check whether an employee with a particular ID already exists in the database.
def check_employee(employee_id):
    sql = 'SELECT * FROM employees WHERE employee_id=%s'
    cursor = con.cursor(buffered=True) 
#   A cursor is used by Python to send SQL commands to MySQL and receive results.
# buffered=True makes sure the query results are properly stored so they can be fetched.
# Put the ID into a tuple
    data = (employee_id,)
# Execute the query
    cursor.execute(sql, data) # This sends the SQL query to MySQL.
    employee = cursor.fetchone() 
# fetchone() gets the first matching record.
# If employee 5 exists:
# employee = (5, 'Rahul', 25, 'IT', ...)
# If employee 5 doesn't exist:
# employee = None
    cursor.close()
    return employee is not None # Returns True if the employee exists, False otherwise.
# Add Employee Function...........................................................................................................
def add_employee():
    employee_id = input("Enter Employee ID: ")

    # Check whether employee already exists
    if check_employee(employee_id):
        print("Employee already exists. Please try again.")
        return

    name = input("Enter Employee Name: ")
    age = int(input("Enter Employee Age: "))
    department = input("Enter Department: ")
    designation = input("Enter Designation: ")
    salary = float(input("Enter Salary: "))
    email = input("Enter Email: ")
    joining_date = input("Enter Joining Date (YYYY-MM-DD): ")

    sql = """
    INSERT INTO employees
    (employee_id, name, age, department, designation, salary, email, joining_date)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """

    data = (
        employee_id,
        name,
        age,
        department,
        designation,
        salary,
        email,
        joining_date
    )

    cursor = con.cursor()

    try:
        cursor.execute(sql, data)
        con.commit()

        print("Employee Added Successfully!")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        con.rollback()
# if MySQL gives an error, the program prints it.
# rollback() cancels the unfinished database change.

    finally:
        cursor.close()

# Remove Employee Function.........................................................................................................
def remove_employee():
    employee_id = input("Enter Employee ID: ")

    # Check whether employee exists
    if not check_employee(employee_id):
        print("Employee does not exist. Please try again.")
        return

    sql = "DELETE FROM employees WHERE employee_id=%s"
    data = (employee_id,)

    cursor = con.cursor()

    try:
        # Execute DELETE query
        cursor.execute(sql, data)

        # Save the change
        con.commit()

        print("Employee Removed Successfully!")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        con.rollback()

    finally:
        cursor.close()
# Promote Employee Function...............................................................................................
def promote_employee():
    employee_id = input("Enter Employee ID: ")

    if not check_employee(employee_id):
        print("Employee does not exist. Please try again.")
        return

    cursor = con.cursor()

    try:
        # Get current salary and designation
        sql_select = """
        SELECT salary, designation
        FROM employees
        WHERE employee_id=%s
        """

        cursor.execute(sql_select, (employee_id,))
        employee = cursor.fetchone()

        current_salary = employee[0]
        current_designation = employee[1]

        print("Current Designation:", current_designation)
        print("Current Salary:", current_salary)

        new_designation = input("Enter new designation: ")
        amount = float(input("Enter increase in salary: "))

        new_salary = float(current_salary) + amount

        sql_update = """
        UPDATE employees
        SET designation=%s, salary=%s
        WHERE employee_id=%s
        """

        data = (new_designation, new_salary, employee_id)

        cursor.execute(sql_update, data)
        con.commit()

        print("\nEmployee Promoted Successfully!")
        print("New Designation:", new_designation)
        print("New Salary:", new_salary)

    except (ValueError, mysql.connector.Error) as err:
        print(f"Error: {err}")
        con.rollback()

    finally:
        cursor.close()
# Display Employees Function..............................................................................................
def display_employees():
    try:
        # Query to select all employees
        sql = "SELECT * FROM employees"

        cursor = con.cursor()

        # Execute the SQL query
        cursor.execute(sql)

        # Fetch all employee records
        employees = cursor.fetchall()

        if not employees:
            print("No employees found.")
            return

        # Display each employee
        for employee in employees:
            print("Employee ID     :", employee[0])
            print("Name            :", employee[1])
            print("Age             :", employee[2])
            print("Department      :", employee[3])
            print("Designation     :", employee[4])
            print("Salary          :", employee[5])
            print("Email           :", employee[6])
            print("Joining Date    :", employee[7])
            print("------------------------------------------")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        cursor.close()
# Search Employee ⭐..................................................................................
def search_employee():
    employee_id = input("Enter Employee ID: ")

    sql = "SELECT * FROM employees WHERE employee_id=%s"
    data = (employee_id,)

    cursor = con.cursor()

    try:
        cursor.execute(sql, data)
        employee = cursor.fetchone()

        if employee:
            print("\n========== Employee Found ==========")
            print("Employee ID  :", employee[0])
            print("Name         :", employee[1])
            print("Age          :", employee[2])
            print("Department   :", employee[3])
            print("Designation  :", employee[4])
            print("Salary       :", employee[5])
            print("Email        :", employee[6])
            print("Joining Date :", employee[7])
        else:
            print("Employee does not exist.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        cursor.close()
# Update Employee ⭐...............................................................................
def update_employee():
    employee_id = input("Enter Employee ID: ")

    # Check whether employee exists
    if not check_employee(employee_id):
        print("Employee does not exist.")
        return

    print("\nWhat do you want to update?")
    print("1. Name")
    print("2. Age")
    print("3. Department")
    print("4. Designation")
    print("5. Salary")
    print("6. Email")
    print("7. Joining Date")

    choice = input("Enter your choice: ")

    cursor = con.cursor()

    try:

        if choice == '1':
            new_value = input("Enter new name: ")
            sql = "UPDATE employees SET name=%s WHERE employee_id=%s"

        elif choice == '2':
            new_value = int(input("Enter new age: "))
            sql = "UPDATE employees SET age=%s WHERE employee_id=%s"

        elif choice == '3':
            new_value = input("Enter new department: ")
            sql = "UPDATE employees SET department=%s WHERE employee_id=%s"

        elif choice == '4':
            new_value = input("Enter new designation: ")
            sql = "UPDATE employees SET designation=%s WHERE employee_id=%s"

        elif choice == '5':
            new_value = float(input("Enter new salary: "))
            sql = "UPDATE employees SET salary=%s WHERE employee_id=%s"

        elif choice == '6':
            new_value = input("Enter new email: ")
            sql = "UPDATE employees SET email=%s WHERE employee_id=%s"

        elif choice == '7':
            new_value = input("Enter new joining date (YYYY-MM-DD): ")
            sql = "UPDATE employees SET joining_date=%s WHERE employee_id=%s"

        else:
            print("Invalid choice.")
            return

        data = (new_value, employee_id)

        cursor.execute(sql, data)
        con.commit()

        print("Employee details updated successfully!")

    except (ValueError, mysql.connector.Error) as err:
        print(f"Error: {err}")
        con.rollback()

    finally:
        cursor.close()
# Employee Count..............................................................................
def employee_count():
    sql = "SELECT COUNT(*) FROM employees"

    cursor = con.cursor()

    try:
        cursor.execute(sql)

        count = cursor.fetchone()[0]

        print("\nTotal Employees:", count)

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        cursor.close()
# Department-wise Employee Count ⭐⭐⭐
def department_employee_count():
    sql = """
    SELECT department, COUNT(*)
    FROM employees
    GROUP BY department
    ORDER BY COUNT(*) DESC
    """

    cursor = con.cursor()

    try:
        cursor.execute(sql)

        results = cursor.fetchall()

        print("\n====== Department-wise Employee Count ======")

        if not results:
            print("No employees found.")
            return

        for department, count in results:
            print(f"{department}: {count}")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        cursor.close()

# Menu Function........................................................................................
def menu():
    while True:
        print("\n========== Employee Management System ==========")
        print("1. Add Employee")
        print("2. Remove Employee")
        print("3. Promote Employee")
        print("4. Display Employees")
        print("5. Search Employee")
        print("6. Update Employee")
        print("7. Employee Count")
        print("8. Department-wise Employee Count")
        print("9. Exit")

        ch = input("Enter your choice: ")

        if ch == '1':
            add_employee()

        elif ch == '2':
            remove_employee()

        elif ch == '3':
            promote_employee()

        elif ch == '4':
            display_employees()

        elif ch == '5':
            search_employee()

        elif ch == '6':
            update_employee()

        elif ch == '7':
            employee_count()

        elif ch == '8':
            department_employee_count()

        elif ch == '9':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    menu()
# "If this file is being run directly, start the Employee Management System by calling menu()."