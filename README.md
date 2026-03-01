# VAIVIDYA – Library Management System

## Overview

**VAIVIDYA** is a Python-based Library Management System with a graphical user interface built using **Tkinter**.  
The system allows users to browse books by genre, issue books, view issued books, and return them.  
It also includes an **Admin panel** where administrators can view the history of books issued by customers.

The application uses **MySQL** as the backend database to store book issue records and user data.

Computer Final Project - Copy

---

# Features

## Customer Features

- Enter name to access the system
- Browse books by genre
- Issue multiple books
- View issued books
- Return books
- See pending books to return

### Available Genres

- Science Fiction  
- Mythology  
- Drama  
- Mystery  
- True Crime  
- Adventure Fiction  
- Thriller  
- Fairy Tales  

---

## Admin Features

- Secure login page
- View customer book issue history
- See which books were issued and on which date

---

# Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Core programming language |
| Tkinter | GUI development |
| MySQL | Database storage |
| mysql-connector | Python–MySQL connectivity |
| PIL (Pillow) | Image handling |

---

# Database Structure

## Database Name

db1
---

## Table: entries

Stores admin credentials.

| Field | Description |
|------|-------------|
| id | Primary key |
| password | Admin password |

---

## Table: T1

Stores issued books.

| Field | Description |
|------|-------------|
| UNAME | Customer name |
| Name | Book name |
| Date | Issue date |

---

## How to Run the Project

### 1. Install Required Libraries
pip install mysql-connector-python  
pip install pillow

### 2. Setup MySQL Database

Create database:
CREATE DATABASE db1;
USE db1;

Create tables:
CREATE TABLE entries(
id INT PRIMARY KEY AUTO_INCREMENT,
password VARCHAR(50)
);

CREATE TABLE T1(
UNAME VARCHAR(50),
Name VARCHAR(100),
Date DATE
);

Insert admin password:
INSERT INTO entries(password) VALUES('admin123');

### 3. Update Database Credentials

Update the database connection in the Python file:

con = mysql.connector.connect(
    host='localhost',
    user='root',
    password='your_password',
    database='db1'
)

### 4. Run the Program
python project.py


## Project Workflow

### Customer Flow
1. Enter name on introduction page  
2. Go to Home  
3. Choose a genre  
4. Select books  
5. Click "Issue the selected books"  
6. View issued books in Bag  
7. Return books from Return tab  

### Admin Flow
1. Enter admin username and password  
2. Access the History tab  
3. View list of issued books by customers  


## Folder Structure

Library-System  
│  
├── project.py  
├── images/  
│   ├── Logo.png  
│   ├── SF pic.png  
│   ├── M1.png  
│   └── ...  
└── README.md  
