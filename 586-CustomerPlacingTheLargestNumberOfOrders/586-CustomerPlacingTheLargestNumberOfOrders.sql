-- Write your PostgreSQL query statement below

-- worst wording of all time

SELECT customer_number
FROM Orders
GROUP BY customer_number
ORDER BY COUNT(order_number) DESC
LIMIT 1;
