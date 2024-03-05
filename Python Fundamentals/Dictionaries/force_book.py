stored_information = {}

while True:
    command = input()

    if command == "Lumpawaroo":
        break

    if "|" in command:
        force_side, force_user = command.split(" | ")

        if force_user not in [user for users in stored_information.values() for user in users]:
            stored_information.setdefault(force_side, []).append(force_user)

    elif " -> " in command:
        force_user, force_side = command.split(" -> ")

        current_side = [side for side, users in stored_information.items() if force_user in users]
        if current_side:
            current_side = current_side[0]
            if current_side == force_side:
                continue

        for side, users in stored_information.items():
            if force_user in users:
                users.remove(force_user)

        stored_information.setdefault(force_side, []).append(force_user)
        print(f"{force_user} joins the {force_side} side!")

for side, users in stored_information.items():
    if users:
        print(f"Side: {side}, Members: {len(users)}")
        for user in users:
            print(f"! {user}")
