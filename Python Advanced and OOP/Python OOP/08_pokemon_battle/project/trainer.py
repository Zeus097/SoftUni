# In order to work the direktory(08_pokemon_battle) have to be marked as Sources Root !
# After that it have to be returned as normal directory !

from typing import Optional
from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon) -> Optional[str]:
        if pokemon in self.pokemons:
            return "This pokemon is already caught"

        self.pokemons.append(pokemon)
        return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name: str) -> str:
        for current_pokemon_name in self.pokemons:
            if current_pokemon_name.name == pokemon_name:
                self.pokemons.remove(current_pokemon_name)
                return f"You have released {pokemon_name}"

        return "Pokemon is not caught"

    def trainer_data(self) -> str:
        result = [f"Pokemon Trainer {self.name}", f"Pokemon count {len(self.pokemons)}"]
        for p in self.pokemons:
            result.append(f"- {p.pokemon_details()}")

        return "\n".join(result)


# Test code
# pokemon = Pokemon("Pikachu", 90)
# print(pokemon.pokemon_details())
# trainer = Trainer("Ash")
# print(trainer.add_pokemon(pokemon))
# second_pokemon = Pokemon("Charizard", 110)
# print(trainer.add_pokemon(second_pokemon))
# print(trainer.add_pokemon(second_pokemon))
# print(trainer.release_pokemon("Pikachu"))
# print(trainer.release_pokemon("Pikachu"))
# print(trainer.trainer_data())
