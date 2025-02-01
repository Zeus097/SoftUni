CREATE OR REPLACE PROCEDURE sp_withdraw_money(
    account_id INT,
    money_amount NUMERIC(10, 4)
)
AS
$$
    BEGIN
        IF (
            SELECT a.balance
            FROM accounts AS a
            WHERE a.id = account_id
            ) > money_amount
            THEN
                UPDATE accounts
                SET balance = balance - money_amount
                WHERE id = account_id;
        ELSE
            RAISE NOTICE 'Insufficient balance to withdraw %', money_amount;
        END IF;
        COMMIT;
    END;
$$
LANGUAGE plpgsql
;


-- -- TEST code
-- 
-- SELECT a.balance
-- FROM accounts AS a
-- WHERE a.id = 6;
-- 
-- CALL sp_withdraw_money(6,  5437.0000);

