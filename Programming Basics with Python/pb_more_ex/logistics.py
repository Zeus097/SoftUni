cargo_number = int(input())
average_price = 0
cargo_sum = 0

microbus_counter = 0
truck_counter = 0
train_counter = 0

microbus_cargo = 0
truck_cargo = 0
train_cargo = 0

microbus_cargo_percentage = 0
truck_cargo_percentage = 0
train_cargo_percentage = 0

for transport in range(cargo_number):
    quantity_of_tones = int(input())
    if quantity_of_tones <= 3:
        microbus_cargo += quantity_of_tones * 200
        microbus_counter += quantity_of_tones
    elif quantity_of_tones <= 11:
        truck_cargo += quantity_of_tones * 175
        truck_counter += quantity_of_tones
    elif quantity_of_tones >= 12:
        train_cargo += quantity_of_tones * 120
        train_counter += quantity_of_tones
    cargo_sum += quantity_of_tones
    average_price = (microbus_cargo + truck_cargo + train_cargo) / cargo_sum
    microbus_cargo_percentage = microbus_counter / cargo_sum * 100
    truck_cargo_percentage = truck_counter / cargo_sum * 100
    train_cargo_percentage = train_counter / cargo_sum * 100
print(f"{average_price:.02f}")
print(f"{microbus_cargo_percentage:.02f}%")
print(f"{truck_cargo_percentage:.02f}%")
print(f"{train_cargo_percentage:.02f}%")