from database import Database
from motoristaDAO import MotoristaDAO
from cli import MotoristaCLI

db = Database(database="atlas-cluster", collection="Motoristas")

motoristaDAO = MotoristaDAO(database=db)

motoristaCLI = MotoristaCLI(motoristaDAO)
motoristaCLI.run()
