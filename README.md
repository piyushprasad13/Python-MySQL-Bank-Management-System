# Python MySQL Bank Management System

A console-based Bank Management System developed using Python and MySQL for basic account and banking operations.

## Features

- Create a new bank account
- Store customer information in MySQL
- Deposit money
- Withdraw money
- Check account balance
- Display customer details
- Delete an account
- Validate account numbers
- Prevent withdrawals when the balance is insufficient
- Persistent data storage using MySQL

## Technologies Used

- Python
- MySQL
- mysql-connector-python

## Project Structure

```text
Python-MySQL-Bank-Management-System/
├── bank_management.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Database Structure

### account table

| Column | Description |
|---|---|
| name | Customer name |
| accno | Account number |
| address | Customer address |
| phno | Phone number |
| openingbalance | Opening balance |

### amount table

| Column | Description |
|---|---|
| name | Customer name |
| accno | Account number |
| balance | Current account balance |

## MySQL Setup

Create the database:

```sql
CREATE DATABASE bank1;
USE bank1;
```

Create the `account` table:

```sql
CREATE TABLE account (
    name VARCHAR(50),
    accno VARCHAR(20) PRIMARY KEY,
    address VARCHAR(100),
    phno VARCHAR(15),
    openingbalance INT
);
```

Create the `amount` table:

```sql
CREATE TABLE amount (
    name VARCHAR(50),
    accno VARCHAR(20) PRIMARY KEY,
    balance INT
);
```

## Installation

Install the required Python package:

```bash
pip install -r requirements.txt
```

## MySQL Configuration

Open `bank_management.py` and replace:

```python
password='YOUR_MYSQL_PASSWORD'
```

with your own local MySQL password.

Do not commit real passwords or other credentials to GitHub.

## Running the Project

Run:

```bash
python bank_management.py
```

The application provides:

1. Open New Account
2. Deposit Amount
3. Withdraw Amount
4. Balance Enquiry
5. Display Customer Details
6. Delete an Account
7. Exit

## SQL Operations Demonstrated

The project uses parameterized SQL queries with:

- INSERT
- SELECT
- UPDATE
- DELETE

## Learning Outcomes

This project demonstrates:

- Python functions and control flow
- MySQL database connectivity
- CRUD operations
- Parameterized SQL queries
- Exception handling
- Basic transaction handling with commit and rollback
- Database-driven application development

## Author

**Piyush Prasad**

B.Tech Electronics and Communication Engineering
