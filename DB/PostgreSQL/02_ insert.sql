INSERT INTO
        clients(full_name, phone_number)
SELECT
first_name || ' ' || last_name,
'(088) 9999' || d.id * 2
        FROM
            drivers AS d
WHERE
    d.id BETWEEN 10 AND 20
;
