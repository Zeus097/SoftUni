CREATE OR REPLACE PROCEDURE sp_deposit_money(
    account_id INT,
    money_amount NUMERIC(10, 4)
)
AS
$$
    BEGIN
        UPDATE accounts
            SET
                balance = balance + money_amount
             WHERE id = account_id;
    END;
$$
LANGUAGE plpgsql;

-- SELECT balance
-- FROM accounts
-- WHERE id = 1;
-- 
-- CALL sp_deposit_money(1, 200)

