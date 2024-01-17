from math import ceil,floor

#заделя 40% от реколтата за производство на вино
#За 1 литър вино са нужни 2,5 кг. грозде


vineyard_space = int(input())
grape_per_meter = float(input())
needed_wine_liters = int(input())
number_of_workers = int(input())

grape_sum = vineyard_space * grape_per_meter
wine = (grape_sum * 0.4) / 2.5
wine_per_worker = (wine - needed_wine_liters) / number_of_workers
diff = abs(wine - needed_wine_liters)

if wine >= needed_wine_liters:
    wine = floor(wine)
    diff = ceil(diff)
    wine_per_worker = ceil(wine_per_worker)
    print(f"Good harvest this year! Total wine: {wine} liters.")
    print(f"{diff} liters left -> {wine_per_worker} liters per person.")
else:
    diff = floor(diff)
    print(f"It will be a tough winter! More {diff} liters wine needed.")
