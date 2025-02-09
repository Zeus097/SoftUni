CREATE TABLE brands(
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE
)
;

CREATE TABLE classifications(
    id SERIAL PRIMARY KEY,
    name VARCHAR(30) NOT NULL UNIQUE
)
;

CREATE TABLE customers(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(30) NOT NULL,
    address VARCHAR(150) NOT NULL,
    phone VARCHAR(30) NOT NULL UNIQUE,
    loyalty_card BOOLEAN NOT NULL DEFAULT FALSE
)
;

CREATE TABLE items(
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    quantity INT NOT NULL,
    price DECIMAL(12, 2) NOT NULL, -- CHECK IF NOT WORKS 100% !
    description TEXT,

    brand_id INT
        REFERENCES brands
        ON UPDATE CASCADE
        ON DELETE CASCADE
        NOT NULL,

    classification_id INT
        REFERENCES classifications
        ON UPDATE CASCADE
        ON DELETE CASCADE
        NOT NULL,

    CONSTRAINT ck_items_quantity
    CHECK ( quantity >= 0 ), -- CHECK IF NOT WORKS 100% !

    CONSTRAINT ck_items_price
    CHECK ( price > 0.00 ) -- CHECK IF NOT WORKS 100% !

)
;

CREATE TABLE orders(
    id SERIAL PRIMARY KEY,
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    customer_id INT
        REFERENCES customers
        ON UPDATE CASCADE
        ON DELETE CASCADE
        NOT NULL
)
;

CREATE TABLE reviews(
    customer_id INT
        REFERENCES customers
        ON UPDATE CASCADE
        ON DELETE CASCADE
        NOT NULL,
    item_id INT
        REFERENCES items
        ON UPDATE CASCADE
        ON DELETE CASCADE
        NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    rating DECIMAL(3, 1) NOT NULL DEFAULT 0.0,

    CONSTRAINT pk_customer_item_id
    PRIMARY KEY (customer_id, item_id), -- CHECK IF NOT WORKS 100% !

    CONSTRAINT ck_reviews_rating
    CHECK ( rating <= 10.0 ) -- CHECK IF NOT WORKS 100%
)
;

CREATE TABLE orders_items(
    order_id INT
        REFERENCES orders
        ON UPDATE CASCADE
        ON DELETE CASCADE
        NOT NULL,
    item_id INT
        REFERENCES items
        ON UPDATE CASCADE
        ON DELETE CASCADE
        NOT NULL,
    quantity INT NOT NULL,

    CONSTRAINT pk_order_item_id
    PRIMARY KEY (order_id, item_id), -- CHECK IF NOT WORKS 100% !
    
    CONSTRAINT ck_orders_items_quantity
    CHECK ( quantity >= 0 )
)
;

