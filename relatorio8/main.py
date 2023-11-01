from database import Database
from game_database import GameDatabase

db = Database("bolt://54.242.78.250:7687", "neo4j", "experience-tachometers-cathodes")
db.drop_all()

gamedb = GameDatabase(db)

#criando players
gamedb.create_player(122, "João")
gamedb.create_player(134, "Maria")
gamedb.create_player(153, "José")

#criando partidas
gamedb.create_match(21, "vitória",122)
gamedb.create_match(22,"derrota", 122)
gamedb.create_match(23,"vitória", 134)
gamedb.create_match(24,"vitória", 134)
gamedb.create_match(25,"vitória", 134)
gamedb.create_match(26,"derrota", 153)
gamedb.create_match(27,"derrota", 153)

gamedb.update_player(153, "Joaquim")
gamedb.insert_player_match(134, 21)

gamedb.delete_match(25)

print(gamedb.get_players())
print(gamedb.get_match())


db.close()