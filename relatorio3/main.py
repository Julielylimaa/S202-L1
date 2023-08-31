from helper.writeAJson import writeAJson
from pokedex import Pokedex


pokemon = Pokedex()

types = ["Fighting", "Fire"]

pokemon.getPokemonsByType(types)
pokemon.getPokemonByName()
pokemon.getPokemonByHeight()
pokemon.getPokemonByCandyCount()
pokemon.getPokemonOneType()