command = input()
secret_word = ""
final_word = ""
c_counter = 0
o_counter = 0
n_counter = 0

while command != "End":
    if command.isalpha():
        if command != "c" and command != "o" and command != "n":
            secret_word += command
        if command == "c":
            c_counter += 1
            if c_counter > 1:
                secret_word += command
        elif command == "o":
            o_counter += 1
            if o_counter > 1:
                secret_word += command
        elif command == "n":
            n_counter += 1
            if n_counter > 1:
                secret_word += command
        if c_counter > 0 and o_counter > 0 and n_counter > 0:
            c_counter = 0
            o_counter = 0
            n_counter = 0
            secret_word += " "
            final_word += secret_word
            secret_word = ""
    else:
        pass
    command = input()
else:
    print(final_word)
