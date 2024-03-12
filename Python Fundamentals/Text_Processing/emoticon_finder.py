text_input = input()

for index in range(len(text_input)):
    if text_input[index].startswith(":"):
        print(f":{text_input[index + 1]}")
