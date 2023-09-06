from database import Database
from writeAJson import writeAJson

db = Database(database="mercado", collection="compras")

class ProductAnalyzer: 
    def _init_ (self, database: Database):
        _database = Database

    def totalVendas(self):
        result = db.collection.aggregate([
        {"$unwind": "$produtos"},
        {"$group": {"_id": "$data_compra", "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
        ])
        return writeAJson(result, "Total de vendas por dia")
    
    def produtoMaisVendido(self):
        result = db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.descricao", "total": {"$sum": "$produtos.quantidade"}}},
            {"$sort": {"total": -1}},
            {"$limit": 1}
        ])
        return writeAJson(result, "Produto mais vendido")
    
    def clienteMaisGastou(self):
        result = db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$cliente_id", "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
            {"$sort": {"total": -1}},
            {"$limit": 1}
        ])
        return writeAJson(result, "Cliente que mais gastou")
    
    def produtosVenderamMais(self):
        result = db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id":"$produtos.descricao", "quantidade":{"$sum":"$produtos.quantidade"}}},
            {"$match": {"quantidade": {"$gt": 1}}},
        ])
        return writeAJson(result, "Produtos que venderam mais de uma unidade")
