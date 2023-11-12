from database import Database
from teacher_crud import TeacherCRUD

db = Database("bolt://44.201.152.63:7687", "neo4j", "abuses-millimeters-conductor")
# db.drop_all()

teacher_crud = TeacherCRUD(db)

#b
# teacher_crud.create(1956, "Chris Lima",  '189.052.396-66')

#c
print(teacher_crud.read("Chris Lima"))

#d
teacher_crud.update("Chris Lima","162.052.777-77")
