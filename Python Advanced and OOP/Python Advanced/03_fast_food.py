from collections import deque


daily_food_quantity = int(input())
food_orders_quantity = deque(list(map(int, input().split())))

print(max(food_orders_quantity))

while food_orders_quantity and food_orders_quantity[0] <= daily_food_quantity:
    daily_food_quantity -= food_orders_quantity.popleft()

if not food_orders_quantity:
    print("Orders complete")
else:
    orders_left = ' '.join([str(order) for order in food_orders_quantity])
    print(f"Orders left: {orders_left}")
