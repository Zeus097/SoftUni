from collections import deque


current_money = list(map(int, input().split()))
foods = deque(map(int, input().split()))
food_count = 0

while current_money and foods:
    if current_money[-1] == foods[0]:
        food_count += 1
        current_money.pop()
        foods.popleft()

    elif current_money[-1] > foods[0]:
        food_count += 1
        difference = abs(current_money.pop() - foods.popleft())
        if current_money:
            current_money[-1] += difference

    else:
        current_money.pop()
        foods.popleft()

if food_count == 0:
    print("Henry remained hungry. He will try next weekend again.")
elif 1 <= food_count <= 3:
    if food_count == 1:
        print(f"Henry ate: {food_count} food.")
    else:
        print(f"Henry ate: {food_count} foods.")
else:
    print(f"Gluttony of the day! Henry ate {food_count} foods.")
