-- Write your PostgreSQL query statement below

/*
find max salary per department
match employees to that
join to department for name

need to learn window function
*/

SELECT d.name AS Department, e.name AS Employee, e.salary as SALARY
FROM Employee e
INNER JOIN Department d
ON e.departmentId = d.id
-- when salary matches highest in that dept, then we output
WHERE e.salary = (
    -- finds max salary within that department
    SELECT MAX(salary)
    FROM Employee e2
    WHERE e.departmentId = e2.departmentId
);
