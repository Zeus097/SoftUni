needed_book = input()
searched_book = input()
book_counter = 0
book_is_found = False

while searched_book != "No More Books":

    if searched_book == needed_book:
        book_is_found = True
        break

    searched_book = input()
    book_counter += 1

if book_is_found:
    print(f"You checked {book_counter} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {book_counter} books.")