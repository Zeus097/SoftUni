SELECT
    cl.full_name,
    COUNT(cl.id) AS count_of_cars,
    SUM(co.bill) AS total_sum
FROM
    clients AS cl
JOIN
    courses AS co
ON
    cl.id = co.client_id
WHERE
    cl.full_name
LIKE
    '_a%'
GROUP BY
    cl.full_name
HAVING
    COUNT(cl.id) > 1
ORDER BY
    cl.full_name
;

