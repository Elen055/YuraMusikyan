
create database yura;
use yura;
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    department TEXT NOT NULL,
    role TEXT NOT NULL,
    salary REAL NOT NULL,
    hire_date TEXT NOT NULL
);


INSERT INTO employees (first_name, last_name, department, role, salary, hire_date) VALUES 
('John', 'Doe', 'Engineering', 'Software Engineer', 85000.00, '2021-03-15'),
('Jane', 'Smith', 'Human Resources', 'HR Manager', 75000.00, '2019-07-22'),
('Alice', 'Johnson', 'Engineering', 'Data Scientist', 95000.00, '2022-01-10'),
('Bob', 'Williams', 'Marketing', 'Marketing Specialist', 65000.00, '2020-11-05'),
('Charlie', 'Brown', 'Finance', 'Financial Analyst', 80000.00, '2018-05-30'),
('Diana', 'Prince', 'Engineering', 'Project Manager', 92000.00, '2020-08-14'),
('Evan', 'Wright', 'Sales', 'Account Executive', 70000.00, '2023-02-01');

