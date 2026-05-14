-- Write your PostgreSQL query statement below

WITH base AS (
    SELECT id, COUNT(*) AS freq
    FROM (
        SELECT requester_id AS id
        FROM RequestAccepted
        UNION ALL
        SELECT accepter_id
        FROM RequestAccepted
    ) 
    GROUP BY id
)

SELECT id, freq AS num
FROM base 
WHERE freq = ( -- checks if the frequency is equal to max freq
    SELECT MAX(freq)
    FROM base
);



