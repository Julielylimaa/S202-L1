class GameDatabase:
    def __init__(self, database):
        self.db = database

    #create
    def create_player(self,idPlayer, name):
        query = "CREATE (:Jogador {idPlayer: $idPlayer, name: $name})"
        parameters = {"idPlayer": idPlayer, "name": name}
        self.db.execute_query(query, parameters)

    def create_match(self, idMatch, resultado, idPlayer):
        query = "MATCH (j:Jogador {idPlayer: $idPlayer}) CREATE (:Partida {idMatch: $idMatch,resultado: $resultado})<-[:PARTICIPA]-(j)"
        parameters = {"idMatch": idMatch,"resultado": resultado, "idPlayer": idPlayer}
        self.db.execute_query(query, parameters)

    #read
    def get_players(self):
        query = "MATCH (j:Jogador) RETURN j.name AS name"
        results = self.db.execute_query(query)
        return [result["name"] for result in results]

    def get_match(self):
        query = "MATCH (p:Partida)<-[:PARTICIPA]-(j:Jogador) RETURN p.resultado AS resultado, j.name AS jogador_name"
        results = self.db.execute_query(query)
        return [(result["resultado"], result["jogador_name"]) for result in results]

    #update
    def update_player(self, idPlayer, new_name):
        query = "MATCH (j:Jogador {idPlayer: $idPlayer}) SET j.name = $new_name"
        parameters = {"idPlayer": idPlayer,"new_name": new_name}
        self.db.execute_query(query, parameters)
        
    def insert_player_match(self, idPlayer, idMatch):
        query = "MATCH (j:Jogador {idPlayer: $idPlayer}) MATCH (p:Partida {idMatch: $idMatch}) CREATE (j)-[:PARTICIPA]->(p)"
        parameters = {"idPlayer": idPlayer, "idMatch": idMatch}
        self.db.execute_query(query, parameters)

    #delete
    def delete_player(self, idPlayer):
        query = "MATCH (j:Jogador {idPlayer: $idPlayer}) DETACH DELETE j"
        parameters = {"idPlayer": idPlayer}
        self.db.execute_query(query, parameters)
    
    def delete_match(self, idMatch):
        query = "MATCH (p:Partida {idMatch: $idMatch})<-[:PARTICIPA]-(j:Jogador) DETACH DELETE p"
        parameters = {"idMatch": idMatch}
        self.db.execute_query(query, parameters)