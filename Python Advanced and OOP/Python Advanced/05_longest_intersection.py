def needed_range(start, end):
    return set(num for num in range(int(start), int(end) + 1))


n = int(input())
longest_intersection = set()

for _ in range(n):
    first_range, second_range = input().split('-')
    first_start, first_end = first_range.split(',')
    second_start, second_end = second_range.split(',')

    a_range = needed_range(first_start, first_end)
    b_range = needed_range(second_start, second_end)
    current_intersection = a_range & b_range
    if len(current_intersection) > len(longest_intersection):
        longest_intersection = current_intersection

unpacked_intersection = ', '.join(str(x) for x in longest_intersection)
print(f"Longest intersection is [{unpacked_intersection}] with length {len(longest_intersection)}")
