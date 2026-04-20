CREATE TABLE employees (
    id INT,
    name VARCHAR(50),
    department VARCHAR(50),
    salary FLOAT
);

-- View all data
SELECT * FROM employees;

-- Only IT employees
SELECT * FROM employees WHERE department = 'IT';

-- Average salary
SELECT AVG(salary) FROM employees;