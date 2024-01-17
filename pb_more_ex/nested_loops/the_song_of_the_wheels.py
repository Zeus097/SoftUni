n = int(input())
num = 0
II = 0
J = 0
H = 0
G = 0

for i in range(1, n + 1):
    if i > 9:
        continue
    for j in range(1, n + 1):
        if j > 9:
            continue
        for h in range(1, n + 1):
            if h > 9:
                continue
            for g in range(1, n + 1):
                if g > 9:
                    continue
                if i < j and h > g:
                    if i * j + h * g == n:
                        num += 1
                        print(f"{i}{j}{h}{g}", end=" ")

                        if num == 4:
                            II = i
                            J = j
                            H = h
                            G = g

if II != 0:
    print(f"\nPassword: {II}{J}{H}{G}")
else:
    print("\nNo!")
