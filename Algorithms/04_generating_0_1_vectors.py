def gen01(idx, vector):
    if idx >= len(vector):
        print("".join([str(x) for x in vector]))
        return
    for number in range(0, 2):
        vector[idx] = number
        gen01(idx + 1, vector)


n = int(input())
idx = 0
vector = [0] * n
gen01(idx, vector)

# Input: 3
# Output: 
# 000
# 001
# 010
# 011
# 100
# 101
# 110
# 111
