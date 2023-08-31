from database import Database
from helper.writeAJson import writeAJson
db = Database(database="pokedex", collection="pokemons")

class Pokedex: 
    def _init_ (self, database: Database):
        _database = Database

    #buscar pokemons pelo tipo
    def getPokemonsByType(self, types: list):
        pokemons = db.collection.find({"type": {"$in": types}})
        return writeAJson(pokemons, "pokemons_by_type")
    
    #buscar pokemons que o nome começa com a letra B
    def getPokemonByName(self):
        busca_nome_B = db.collection.find({"name": {"$regex": "^B"}})
        return writeAJson(busca_nome_B, "pokemons_nome_começa_B")

    #buscar pokemons com altura menor que 0.5m e peso maior que 5kg
    def getPokemonByHeight(self):
        busca_altura = db.collection.find({"height": {"$lt":"0.5"}, "weight": {"$gt": "5.0"}})
        return writeAJson(busca_altura, "pokemons_altura_peso")
    
    #buscar pokemons que candy_count existe e é diferente de 50
    def getPokemonByCandyCount(self):
        busca_candy_count = db.collection.find({"$and": [{"candy_count": {"$exists": True}}, {"candy_count":{"$ne": 50}}]})
        return writeAJson(busca_candy_count, "pokemons_candy_count_diferente_50")
    
    #buscar pokemons com apenas um tipo
    def getPokemonOneType(self):
        busca_one_type = db.collection.find({"type": {"$size": 1}})
        return writeAJson(busca_one_type, "pokemons_apenas_um_tipo")