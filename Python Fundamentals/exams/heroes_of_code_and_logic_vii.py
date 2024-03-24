heroes_number = int(input())
heroes = {}
for index in range(heroes_number):
    hero_name, hit_points, mana_points = input().split()
    heroes[hero_name] = {'HIT_POINTS': int(hit_points), 'MANA_POINTS': int(mana_points)}

while True:
    command = input()
    if command == 'End':
        break

    action = command.split(' - ')

    if action[0] == 'CastSpell':
        hero_name = action[1]
        mana_points_needed = int(action[2])
        spell_name = action[3]
        if heroes[hero_name]['MANA_POINTS'] >= mana_points_needed:
            heroes[hero_name]['MANA_POINTS'] -= mana_points_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {heroes[hero_name]['MANA_POINTS']} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")

    elif action[0] == 'TakeDamage':
        hero_name = action[1]
        damage = int(action[2])
        attacker = action[3]
        heroes[hero_name]['HIT_POINTS'] -= damage
        if heroes[hero_name]['HIT_POINTS'] > 0:
            print(f"{hero_name} was hit for {damage} HP by {attacker}"
                  f" and now has {heroes[hero_name]['HIT_POINTS']} HP left!")
        else:
            del heroes[hero_name]
            print(f"{hero_name} has been killed by {attacker}!")

    elif action[0] == 'Recharge':
        current_hero_name = action[1]
        amount = int(action[2])
        if heroes[current_hero_name]['MANA_POINTS'] + amount > 200:
            amount_needed = 200 - heroes[current_hero_name]['MANA_POINTS']
            heroes[current_hero_name]['MANA_POINTS'] = 200
            print(f"{current_hero_name} recharged for {amount_needed} MP!")
        else:
            heroes[current_hero_name]['MANA_POINTS'] += amount
            print(f"{current_hero_name} recharged for {amount} MP!")

    elif action[0] == 'Heal':
        current_hero_name = action[1]
        amount = int(action[2])
        if heroes[current_hero_name]['HIT_POINTS'] + amount > 100:
            amount_needed = 100 - heroes[current_hero_name]['HIT_POINTS']
            heroes[current_hero_name]['HIT_POINTS'] = 100
            print(f"{current_hero_name} healed for {amount_needed} HP!")
        else:
            heroes[current_hero_name]['HIT_POINTS'] += amount
            print(f"{current_hero_name} healed for {amount} HP!")

for hero_name in heroes:
    print(f"{hero_name}\nHP: {heroes[hero_name]['HIT_POINTS']}\nMP: {heroes[hero_name]['MANA_POINTS']}")
