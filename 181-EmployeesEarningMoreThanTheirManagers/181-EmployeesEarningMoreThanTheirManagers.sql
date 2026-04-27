# Write your MySQL query statement below

/*
  need to get better at thinking about different types of methods / keywords ive learned, in sql, you cant loop around or anything besides the basic methods, so comparisons are done by joining tables!
*/

SELECT one.name as Employee -- renames the output table col to Employee since there is no Employee column in original table
FROM Employee one
INNER JOIN Employee two
ON one.managerId = two.id
WHERE one.salary > two.salary;
