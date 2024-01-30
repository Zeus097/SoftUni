def josephus_permutation(people, k):
    result = []
    index = 0

    while len(people) > 0:
        index = (index + k - 1) % len(people)
        result.append(people.pop(index))

    return result

people_list = list(map(int, input().split()))
k_value = int(input())

result_permutation = josephus_permutation(people_list, k_value)
output_str = "[" + ",".join(map(str, result_permutation)) + "]"
print(output_str)
