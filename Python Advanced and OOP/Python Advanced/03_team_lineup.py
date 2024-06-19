def team_lineup(*args):
    output = ""
    collection = {}
    for player_names, countre_names in args:
        if countre_names not in collection:
            collection[countre_names] = []
        collection[countre_names].append(player_names)
    sorted_collection = dict(sorted(collection.items(), key=lambda x: (-len(x[1]), x[0])))

    for current_country, current_player in sorted_collection.items():
        output += f"{current_country}:\n"
        for player_name in current_player:
            output += f"  -{player_name}\n"

    return output


# OUTPUT 1
# print(team_lineup(
#     ("Harry Kane", "England"),
#     ("Manuel Neuer", "Germany"),
#     ("Raheem Sterling", "England"),
#     ("Toni Kroos", "Germany"),
#     ("Cristiano Ronaldo", "Portugal"),
#     ("Thomas Muller", "Germany")))


# OUTPUT 2
# print(team_lineup(("Lionel Messi", "Argentina"),
#                   ("Neymar", "Brazil"),
#                   ("Cristiano Ronaldo", "Portugal"),
#                   ("Harry Kane", "England"),
#                   ("Kylian Mbappe", "France"),
#                   ("Raheem Sterling", "England")))


# OUTPUT 3
# print(team_lineup(
#    ("Harry Kane", "England"),
#    ("Manuel Neuer", "Germany"),
#    ("Raheem Sterling", "England"),
#    ("Toni Kroos", "Germany"),
#    ("Cristiano Ronaldo", "Portugal"),
#    ("Thomas Muller", "Germany"),
#    ("Bruno Fernandes", "Portugal"),
#    ("Bernardo Silva", "Portugal"),
#    ("Harry Maguire", "England")))

