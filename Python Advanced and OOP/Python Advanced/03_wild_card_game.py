def draw_cards(*args, **kwargs):
    result = ""
    monster_deck = []
    spell_deck = []

    for card_name, card_type in (list(args) + list(kwargs.items())):
        if card_type == "monster":
            monster_deck.append(f"  ***{card_name}")
        elif card_type == "spell":
            spell_deck.append(f"  $$${card_name}")

    if monster_deck:
        result += f"Monster cards:\n" + '\n'.join(sorted(monster_deck, reverse=True))

    if spell_deck:
        result += "\nSpell cards:\n" + '\n'.join(sorted(spell_deck))

    return result.strip()


# print(draw_cards(("cyber dragon", "monster"), freeze="spell",))

# print(draw_cards(("celtic guardian", "monster"), ("earthquake", "spell"), ("fireball", "spell"),
# raigeki="spell", destroy="spell",))

# print(draw_cards(("brave attack", "spell"), ("freeze", "spell"), lightning_bolt="spell", fireball="spell",))
