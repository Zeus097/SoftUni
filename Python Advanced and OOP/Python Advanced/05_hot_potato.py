from collections import deque


kids_names = deque(input().split())
toss = int(input())

while len(kids_names) > 1:
    kids_names.rotate(- (toss - 1))
    removed_kid = kids_names.popleft()
    print(f"Removed {removed_kid}")

print(f"Last is {''.join(kids_names)}")
