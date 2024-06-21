from collections import deque


tools = deque(map(int, input().split()))
substances = list(map(int, input().split()))

challenges = list(map(int, input().split()))

while True:
    if len(tools) == 0 or len(substances) == 0:
        break

    match = False

    current_tool = tools[0]
    current_substance = substances[-1]
    result = current_tool * current_substance

    for element in challenges:
        if result == element:
            tools.popleft()
            substances.pop()
            challenges.remove(element)
            match = True
            break

    if not match:
        tools[0] += 1
        tools.rotate(-1)

        substances[-1] -= 1
        if substances[-1] == 0:
            substances.pop()

if challenges:
    print("Harry is lost in the temple. Oblivion awaits him.")
else:
    print("Harry found an ostracon, which is dated to the 6th century BCE.")

if tools:
    print(f"Tools: {', '.join(map(str, tools))}")

if substances:
    print(f"Substances: {', '.join(map(str, substances))}")

if challenges:
    print(f"Challenges: {', '.join(map(str, challenges))}")
