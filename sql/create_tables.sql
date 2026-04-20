-- View all data
SELECT * FROM employees;

-- Only IT employees
SELECT * FROM employees WHERE department = 'IT';

-- Average salary
SELECT AVG(salary) FROM employees;