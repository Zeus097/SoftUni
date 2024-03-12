text = input()
rage = ""
repetition_text = ""
substring = ""

for index in range(len(text)):
    if not text[index].isdigit():
        repetition_text += text[index].upper()

    else:
        for next_index in range(index, len(text)):
            if not text[next_index].isdigit():
                break
            rage += text[next_index]
        substring += int(rage) * repetition_text
        repetition_text = ""
        rage = ""

print(f"Unique symbols used: {len(set(substring))}")
print(substring)
