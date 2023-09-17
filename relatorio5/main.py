from database import Database
from bookModel import BookModel
from cli import BookCLI

db = Database(database="relatorio05", collection="Livros")
bookModel = BookModel(database=db)

bookCLI = BookCLI(bookModel)
bookCLI.run()