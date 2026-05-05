-- Write your PostgreSQL query statement below

/*
starting to remember the use of searching and correlated subquerise

only beats 5% so i should use join / window function after i learn it better, since this uses subquery for every single row in s1
*/

SELECT product_id, year AS first_year, quantity, price
FROM Sales s1
WHERE s1.year = (
    SELECT MIN(s2.year)
    FROM Sales s2
    WHERE s1.product_id = s2.product_id
);


