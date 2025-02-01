CREATE OR REPLACE FUNCTION fn_calculate_future_value(
	initial_sum DECIMAL, -- amount of money initially invested
	yearly_interest_rate DECIMAL, -- annual interest rate
	number_of_years INT -- duration for which the investment will earn interest
)
RETURNS DECIMAL
AS
$$
	BEGIN
		RETURN TRUNC(
			initial_sum * POWER( 1 + yearly_interest_rate , number_of_years),
			4
		);
	END;
$$
LANGUAGE plpgsql;