-- Write your PostgreSQL query statement below

-- starting to get the hang of it. i originally used an inner join though but realized this is also a way to go. minimal performance diff.

SELECT name
FROM Employee
WHERE id IN (
    SELECT managerId
    FROM Employee
    GROUP BY managerId
    HAVING COUNT(managerId) >= 5
);
