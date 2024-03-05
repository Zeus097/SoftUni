def fill_phonebook():
    phonebook = {}

    while True:
        command = input().split("-")

        if len(command) == 1:
            break

        name, number = command[0], command[1]
        phonebook[name] = number

    return phonebook, int(command[0])


def main():
    phonebook, n = fill_phonebook()

    for _ in range(n):
        search_name = input()

        if search_name in phonebook:
            print(f"{search_name} -> {phonebook[search_name]}")
        else:
            print(f"Contact {search_name} does not exist.")


if __name__ == "__main__":
    main()
