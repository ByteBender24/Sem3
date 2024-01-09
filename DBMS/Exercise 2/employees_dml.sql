SET ECHO ON;

REM| EMPLOYEES.sql DML COMMANDS
REM| Question 2

REM| Author : Harishraj S
REM| Date :15-10-2023

REM| Use the employees.sql to create the database and write the SQL statements for
REM| the following:

REM| 9. Display firsy name, job id and salary of all the employees

SELECT first_name, job_id, salary FROM employees;

REM| 10. Display the id, name(first & last), salary and annual salary of all the employees.
REM| Sort the employees by first name. Label the columns as shown below:
REM|(EMPLOYEE_ID, FULL NAME, MONTHLY SAL, ANNUAL SALARY)

SELECT employee_id as "EMPLOYEE ID", 
(First_name || ' ' ||Last_name) as "FULL NAME", 
SALARY as "MONTHLY SAL", 
SALARY * 12 as "ANNUAL SALARY" 
FROM Employees
ORDER BY First_name;

REM| 11. List the different jobs in which the employees are working for

SELECT DISTINCT job_id 
FROM employees 
ORDER BY job_id;

REM| 12. Display the id, first name, job id, salary and commission of employees who are
REM| earning commissions.

SELECT employee_id, first_name, job_id, salary, commission_pct 
FROM employees
WHERE commission_pct IS NOT NULL;

REM| 13. Display the details (id, first name, job id, salary and dept id) of employees who
REM| are MANAGERS.

SELECT employee_id, first_name, job_id, salary, department_id 
FROM employees
WHERE manager_id IS NOT NULL;

REM| 14. Display the details of employees other than sales representatives (id, first name,
REM| hire date, job id, salary and dept id) who are hired after ‘01-May-1999’ or whose
REM| salary is at least 10000.

SELECT employee_id, first_name, hire_date, job_id, salary, department_id
FROM employees
WHERE job_id != 'SA_REP' and ((hire_date > TO_DATE('01-May-1999','DD-MON-YYYY')) or (salary >= 10000));


REM| 15. Display the employee details (first name, salary, hire date and dept id) whose
REM| salary falls in the range of 5000 to 15000 and his/her name begins with any of
REM| characters (A,J,K,S). Sort the output by first name.

SELECT first_name, salary, hire_date, department_id 
FROM employees
WHERE (salary BETWEEN 5000 and 10000) AND (first_name LIKE 'A%' OR first_name LIKE 'J%' OR first_name LIKE 'K%' OR first_name LIKE 'S%')
ORDER BY first_name;

REM| 16. Display the experience of employees in no. of years and months who were hired
REM| after 1998. Label the columns as: (EMPLOYEE_ID, FIRST_NAME, HIRE_DATE, EXP-YRS,
REM| EXP-MONTHS)

--SELECT
--  employee_id,
--  first_name,
--  hire_date,
--  TRUNC(MONTHS_BETWEEN(SYSDATE, hire_date) / 12) AS years_experience,
--  TRUNC(MOD(MONTHS_BETWEEN(SYSDATE, hire_date), 12)) AS months_experience
--FROM employees
--WHERE hire_date > TO_DATE('01-JAN-1999', 'DD-MON-YYYY');

SELECT employee_id AS "EMPLOYEE_ID",
first_name AS "FIRST_NAME",
hire_date AS "HIRE_DATE",
ABS(EXTRACT(YEAR FROM SYSDATE) - EXTRACT(YEAR FROM hire_date)) AS "EXP-YRS",
ABS(MOD(EXTRACT(MONTH FROM SYSDATE) - EXTRACT(MONTH FROM hire_date), 12)) AS "EXP-MONTHS"
FROM employees
WHERE hire_date > TO_DATE('31-12-1998','DD-MM-YYYY');

-- Error because of the usage of single quotes around column aliases. 
-- In SQL, column aliases should be enclosed in double quotes or square brackets ([]) or simply without any quotes.
-- Single quotes you've used are not the correct syntax for column aliases in SQL.

REM| 17. Display the total number of departments.

SELECT COUNT(DISTINCT department_id) AS "No of Departments"
FROM employees;

REM| 18. Show the number of employees hired by year-wise. Sort the result by year-wise
-- USAGE OF Group by
SELECT COUNT(employee_id) as "No.of Employees", hire_date
FROM employees
GROUP BY hire_date
ORDER BY hire_date;


REM| 19. Display the minimum, maximum and average salary, number of employees for
REM| each department. Exclude the employee(s) who are not in any department.
REM| Include the department(s) with at least 2 employees and the average salary is
REM| more than 10000. Sort the result by minimum salary in descending order.

SELECT MIN(salary), MAX(salary), AVG(salary), COUNT(employee_id), department_id
FROM employees
GROUP BY department_id
HAVING COUNT(employee_id) >= 2 AND AVG(salary) > 10000
ORDER BY MIN(salary) DESC;

REM| ------------------------------END OF SCRIPT FILE--------------------------------------------------------------------------