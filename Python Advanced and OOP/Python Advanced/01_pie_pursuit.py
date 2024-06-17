from collections import deque


contestants = deque(map(int, input().split()))
pie_pieces = list(map(int, input().split()))

while contestants and pie_pieces:
    if contestants[0] >= pie_pieces[-1]:
        contestants[0] -= pie_pieces.pop()
        if contestants[0] == 0:
            contestants.popleft()
        else:
            contestants.rotate(-1)

    else:
        pie_pieces[-1] -= contestants[0]
        if pie_pieces[-1] == 1:
            if len(pie_pieces) > 1:
                pie_pieces[-2] += pie_pieces[-1]
                pie_pieces.pop()
        contestants.popleft()

if not pie_pieces and contestants:
    print(f"We will have to wait for more pies to be baked!\nContestants left: {', '.join(map(str, contestants))}")

elif not pie_pieces and not contestants:
    print("We have a champion!")

elif not contestants and pie_pieces:
    print(f"Our contestants need to rest!\nPies left: {', '.join(map(str, pie_pieces))}")
