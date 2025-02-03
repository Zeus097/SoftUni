UPDATE
    animals
SET
    owner_id = (
        SELECT id FROM owners WHERE id = 4
    )
WHERE
    owner_id IS NULL
;

