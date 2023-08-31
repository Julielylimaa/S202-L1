
class Professor:
    def __init__(self, nome):
        self.nome = nome
    
    def ministrar_aula(self, assunto):
        print(f'O professor {self.nome} está ministrando uma aula sobre {assunto}')


class Aluno:
    def __init__(self, nome):
        self.nome = nome
    
    def presenca(self):
        print(f'O aluno {self.nome} esta presente ')

class Aula:
    def __init__(self, Professor, assunto, alunos = None):
        self.Professor = Professor
        self.assunto= assunto
        self.alunos = alunos 
        
    
    def adicionar_aluno(self, novo_aluno):
        self.alunos.append(novo_aluno)

    def listar_presenca(self):
        print(f'Presença na aula sobre {assunto} ministrada pelo professor {self.Professor.nome}: ')
        for aluno in self.alunos:
            aluno.presenca()

professor = Professor("Renzo")
assunto = "Banco de Dados"
professor.ministrar_aula(assunto)

aluno1 = Aluno("aluno 1")
aluno2 = Aluno("aluno 2")
alunos = [aluno1, aluno2]

aula = Aula(professor, assunto, alunos)

aluno3 = Aluno("aluno 3")
aula.adicionar_aluno(aluno3)

aula.listar_presenca()






