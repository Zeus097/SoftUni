number_of_commands = int(input())
parking_lot = {}

for i in range(number_of_commands):
    command = input().split()
    operation_type = command[0]
    username = command[1]

    if operation_type == "register":
        license_plate_number = command[2]

        if username in parking_lot:
            print(f"ERROR: already registered with plate number {license_plate_number}")
        else:
            parking_lot[username] = license_plate_number
            print(f"{username} registered {license_plate_number} successfully")

    elif operation_type == "unregister":
        if username not in parking_lot:
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            parking_lot.pop(username)

for username, license_plate_number in parking_lot.items():
    print(f"{username} => {license_plate_number}")
