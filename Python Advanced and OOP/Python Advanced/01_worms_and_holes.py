from collections import deque


worms = list(map(int, input().split()))
holes = deque(map(int, input().split()))
matches = 0
total_worms = len(worms)

while worms and len(holes) > 0:
    if worms[-1] == holes[0]:
        worms.pop()
        holes.popleft()
        matches += 1
    else:
        holes.popleft()
        worms[-1] -= 3
        if worms[-1] <= 0:
            worms.pop()

print(f"Matches: {matches}" if matches != 0 else "There are no matches.")

if matches != total_worms:
    print(f"Worms left: {', '.join(map(str, worms))}" if worms else "Worms left: none")

else:
    print("Every worm found a suitable hole!")

print(f"Holes left: {', '.join(map(str, holes))}" if holes else "Holes left: none")
