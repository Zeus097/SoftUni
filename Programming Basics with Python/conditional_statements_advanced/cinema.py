projection_name = input()
number_of_rows = int(input())
number_of_columns = int(input())
ticket_price = 0
number_of_seats = number_of_rows * number_of_columns

if projection_name == "Premiere":
    ticket_price = number_of_seats * 12.00
elif projection_name == "Normal":
    ticket_price = number_of_seats * 7.50
elif projection_name == "Discount":
    ticket_price = number_of_seats * 5.00

print(f"{ticket_price:.2f} leva")


