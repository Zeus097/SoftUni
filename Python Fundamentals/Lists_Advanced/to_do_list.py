def todo_list_program():
    todo_notes = []

    while True:
        notes = input()

        if notes == "End":
            break

        todo_notes.append(notes)

    sorted_notes = sorted(todo_notes, key=lambda notes: int(notes.split("-")[0]))
    sorted_notes = [notes.split("-")[1] for notes in sorted_notes]

    return sorted_notes

result = todo_list_program()
print(result)
