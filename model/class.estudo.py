class Estudo:
    def __init__(self, professor, turma, conteudos):
        self.professor = professor
        self.turma = turma
        self.conteudos = conteudos
        self.lista = "lista" 
        self.altera = "alterar"

    def listar(self, lista):
        self.listar = lista
        print("Agendamento realizado.")

    def alterar(self, alterar):
        self.alterar = alterar
        print("alterado com sucesso")

turma1 = Estudo("Arã", "nono ano", "Circunferencia, graficos, multiplicação, divisão")
turma2 = Estudo("Alessandra", "segundo ano", "arte moderna, barroco, cinema, arte egipicia")

print(turma1.conteudos)
turma1.listar("")
turma2.alterar("")