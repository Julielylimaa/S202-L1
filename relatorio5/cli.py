class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Enter a command: ")
            if command == "quit":
                print("Goodbye!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Invalid command. Try again.")

class BookCLI(SimpleCLI):
    def __init__(self, book_model):
        super().__init__()
        self.book_model = book_model
        self.add_command("create", self.create_book)
        self.add_command("read", self.read_book)
        self.add_command("update", self.update_book)
        self.add_command("delete", self.delete_book)


    def create_book(self):
        titulo = input("Digite o titulo: ")
        autor = input("Digite o autor: ")
        ano = int(input("Digite o ano: "))
        preco = float(input("Digite o preço: "))
        self.book_model.create_book(titulo, autor, ano, preco)

    def read_book(self):
        id = input("Digite o id: ")
        book = self.book_model.read_book_by_id(id)
        if book:
            print(f"titulo: {book['titulo']}")
            print(f"autor: {book['autor']}")
            print(f"ano: {book['ano']}")
            print(f"preço: {book['preco']}")

    def update_book(self):
        id = input("Digite o id: ")
        titulo = input("Digite o novo titulo: ")
        autor = input("Digite o novo autor: ")
        ano = int(input("Digite o novo ano: "))
        preco = float(input("Digite o novo preço: "))
        self.book_model.update_book(id, titulo, autor, ano, preco)

    def delete_book(self):
        id = input("Digite o id: ")
        self.book_model.delete_book(id)
        
    def run(self):
        print("Welcome to the Book CLI!")
        print("Available commands: create, read, update, delete, quit")
        super().run()