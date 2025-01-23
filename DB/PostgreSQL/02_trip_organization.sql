SELECT
	driver_id,
	vehicle_type,
	CONCAT(first_name, ' ', last_name) AS driver_name
FROM campers as c
	JOIN vehicles as v
		ON c.id = v.driver_id
;

