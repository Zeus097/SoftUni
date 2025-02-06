CREATE OR REPLACE FUNCTION fn_courses_by_client(phone_num VARCHAR(20))
    RETURNS INT
AS
$$
    DECLARE
        courses_number INT;
    BEGIN
        SELECT
            COUNT(c.phone_number) INTO courses_number
        FROM
            clients AS c
        JOIN
            courses AS co
        ON
            co.client_id = c.id
        WHERE
            c.phone_number = phone_num
        GROUP BY
            c.full_name
        ;
        IF courses_number IS NULL THEN RETURN 0;
        ELSE RETURN courses_number;
        END IF;
    END;
$$
LANGUAGE plpgsql
;