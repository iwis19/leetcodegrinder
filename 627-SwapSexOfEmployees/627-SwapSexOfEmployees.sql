-- Write your PostgreSQL query statement below

-- new syntax. added to my notes

UPDATE salary
SET sex = 
CASE 
WHEN sex = 'm' THEN 'f' 
ELSE 'm'
END;
