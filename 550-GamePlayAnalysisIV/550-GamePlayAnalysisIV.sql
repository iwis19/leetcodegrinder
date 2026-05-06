-- Write your PostgreSQL query statement below

-- awesome i learned new things: ROUND(), didnt have to cast to numeric

SELECT
(
    (
        SELECT COUNT(*)
        FROM Activity
        WHERE (player_id, event_date-1) IN (
            SELECT player_id, MIN(event_date) AS first_login
            FROM Activity
            GROUP BY player_id
        )
    ) 
    * 1.0 / 
    (
        SELECT COUNT(DISTINCT player_id)
        FROM Activity
    )
)::NUMERIC(10,2) AS fraction;



    





    

