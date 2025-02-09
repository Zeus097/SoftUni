UPDATE
    reviews
SET
    rating = 10.0
WHERE
    item_id = customer_id
;

UPDATE
    reviews
SET
    rating = 5.5
WHERE
    customer_id > item_id
;

UPDATE
    reviews
SET
    rating = rating
WHERE
    customer_id < item_id
;