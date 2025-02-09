CREATE OR REPLACE FUNCTION udf_classification_items_count(
    classification_name VARCHAR(30)
) RETURNS TEXT
AS
$$
    DECLARE
            count INT;
    BEGIN
        SELECT
            COUNT(i.id) INTO count
        FROM
            items AS i
        JOIN
            classifications AS c
        ON
            i.classification_id = c.id
        WHERE
            c.name = classification_name
        ;

        IF count > 0 THEN RETURN 'Found ' || count || ' items.';
        ELSE RETURN 'No items found.';
        END IF;
    END;
$$
LANGUAGE plpgsql
;

-- Test Code

-- SELECT udf_classification_items_count('Nonexistent') AS message_text;
-- SELECT udf_classification_items_count('Laptops') AS message_text;