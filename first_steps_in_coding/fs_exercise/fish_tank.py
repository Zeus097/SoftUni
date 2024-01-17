lenght = int(input())
wide = int(input())
height = int(input())
sand_percent = float(input())

aquarium_volume = lenght * wide * height
liters = aquarium_volume * 0.001
used_space = sand_percent / 100
needed_liters = liters * (1 - used_space)

print(needed_liters)
