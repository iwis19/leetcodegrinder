-- Write your PostgreSQL query statement below

/*
1. learned that i could subtract dates simply like integers in postgresql, because its stored like a number, its like a day on a timeline since epoch
*/

SELECT today.id
FROM Weather today
CROSS JOIN Weather yesterday
WHERE today.recordDate - yesterday.recordDate = 1 AND today.temperature > yesterday.temperature;
