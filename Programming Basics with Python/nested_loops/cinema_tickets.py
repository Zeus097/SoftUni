student_tickets = 0
standard_tickets = 0
kid_tickets = 0
movie_name = input()
while movie_name != "Finish":
    free_seats = int(input())
    sold_tickets = 0
    for tickets in range(free_seats):
        current_ticket = input()
        if current_ticket == "End":
            break
        elif current_ticket == "student":
            student_tickets += 1
        elif current_ticket == "standard":
            standard_tickets += 1
        elif current_ticket == "kid":
            kid_tickets += 1
        sold_tickets += 1
    percentage_full_hall = sold_tickets / free_seats * 100
    print(f"{movie_name} - {percentage_full_hall:.2f}% full.")
    movie_name = input()
total_tickets_sold = student_tickets + standard_tickets + kid_tickets
percentage_student_tickets = student_tickets / total_tickets_sold * 100
percentage_standard_tickets = standard_tickets / total_tickets_sold * 100
percentage_kid_tickets = kid_tickets / total_tickets_sold * 100
print(f"Total tickets: {total_tickets_sold}")
print(f"{percentage_student_tickets:.2f}% student tickets.")
print(f"{percentage_standard_tickets:.2f}% standard tickets.")
print(f"{percentage_kid_tickets:.2f}% kids tickets.")