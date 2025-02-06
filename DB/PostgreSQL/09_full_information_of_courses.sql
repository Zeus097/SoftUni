SELECT
    a.name,
    CASE
        WHEN EXTRACT(HOUR FROM co.start) >= 6
            AND EXTRACT(HOUR FROM co.start) <= 20
                THEN 'Day'
        ELSE 'Night'
    END AS day_time,
    co.bill,
    cl.full_name,
    cr.make,
    cr.model,
    ct.name AS category_name
FROM
    addresses AS a
JOIN
    courses AS co
ON
    a.id = co.from_address_id
JOIN
    clients AS cl
ON
    cl.id = co.client_id
JOIN
    cars AS cr
ON
    cr.id = co.car_id
JOIN
    categories AS ct
ON
    ct.id = cr.category_id
ORDER BY
    co.id
;


