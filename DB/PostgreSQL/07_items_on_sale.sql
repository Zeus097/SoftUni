SELECT
    i.name,
    CONCAT(UPPER(b.name), '/', LOWER(cl.name)) AS promotion,
    CONCAT('On sale: ', i.description) AS description,
    i.quantity
FROM
    items AS i
LEFT JOIN
        brands AS b
ON
    i.brand_id = b.id
LEFT JOIN
        classifications AS cl
ON
    i.classification_id = cl.id
WHERE i.id NOT IN (
    SELECT item_id
    FROM orders_items
    )
ORDER BY
    i.quantity DESC,
    i.name ASC
;


