# Employee Management System

A database-driven Employee Management System built using **Python and MySQL**. The application allows users to manage employee records through a simple menu-driven interface.

## Features

- Add Employee
- Remove Employee
- Promote Employee
- Display All Employees
- Search Employee
- Update Employee Details
- Count Total Employees
- Department-wise Employee Count
- MySQL database integration
- Error handling and transaction management

## Technologies Used

- Python
- MySQL
- MySQL Connector/Python

## Database Structure

The project uses a MySQL database named `employee_db` with an `employees` table.

### Employee Table

| Column | Description |
|---|---|
| employee_id | Unique employee ID |
| name | Employee name |
| age | Employee age |
| department | Employee department |
| designation | Job designation |
| salary | Employee salary |
| email | Employee email |
| joining_date | Date of joining |

## SQL Database Setup

Create the database:

```sql
CREATE DATABASE employee_db;

Select the database:

USE employee_db;

Create the employee table:

CREATE TABLE employees (
    employee_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    age INT,
    department VARCHAR(50),
    designation VARCHAR(50),
    salary DECIMAL(10,2),
    email VARCHAR(100),
    joining_date DATE
);
Installation

Clone the repository: git clone <your-github-repository-url>

Go to the project folder: cd Employee_Management_System

Install the required Python package:

pip install -r requirements.txt
MySQL Configuration

Update the MySQL connection details in employee_management.py:

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="employee_db"
)

Replace your_password with your MySQL password.

Run the Project

Run:

python employee_management.py

The application will display:

========== Employee Management System ==========


1. Add Employee
2. Remove Employee
3. Promote Employee
4. Display Employees
5. Search Employee
6. Update Employee
7. Employee Count
8. Department-wise Employee Count
9. Exit
SQL Concepts Used

This project demonstrates practical SQL operations including:

INSERT
SELECT
UPDATE
DELETE
COUNT()
GROUP BY
Parameterized SQL queries

Project Structure
Employee_Management_System/
│
├── employee_management.py
├── requirements.txt
├── README.md
└── .gitignore
Learning Outcomes

Through this project, I practiced:

Python functions and control flow
Database connectivity
CRUD operations
SQL queries
Exception handling
Transaction management using commit() and rollback()
Parameterized queries
Working with relational databases
Author

Murari Mohan Das