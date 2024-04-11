def dungeon_survival(health, bitcoins, rooms):
    alive = True
    for current_room in range(len(rooms)):
        action = rooms[current_room].split()

        if action[0] == 'potion':
            heal_points = int(action[1])
            if health == 100:
                heal_points -= heal_points
            elif health + heal_points > 100:
                heal_points = 100 - health
                health += heal_points
            else:
                health += heal_points
            print(f"You healed for {heal_points} hp.")
            print(f"Current health: {health} hp.")

        elif action[0] == 'chest':
            bitcoins_amount = int(action[1])
            bitcoins += bitcoins_amount
            print(f"You found {bitcoins_amount} bitcoins.")

        else:
            monster = action[0]
            moster_attack_points = int(action[1])
            health -= moster_attack_points
            if health > 0:
                print(f"You slayed {monster}.")
            else:
                print(f"You died! Killed by {monster}.")
                room_number = current_room + 1
                print(f"Best room: {room_number}")
                alive = False
                break
    if alive:
        print(f"You've made it!\nBitcoins: {bitcoins}\nHealth: {health}")


initial_health = 100
initial_bitcoins = 0
dungeons_rooms = input().split('|')
dungeon_survival(initial_health, initial_bitcoins, dungeons_rooms)
