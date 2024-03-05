collected_resources = {}

while True:
    string_sequence = input()

    if string_sequence == 'stop':
        break
    resources = string_sequence
    quantity = int(input())

    if string_sequence not in collected_resources:
        collected_resources[string_sequence] = 0
    collected_resources[string_sequence] += quantity

for key, value in collected_resources.items():
    print(f"{key} -> {value}")
