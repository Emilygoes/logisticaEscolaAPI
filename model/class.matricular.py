class Matricula:
    def __init__(self, nome, serie, ano_nascimento):
        self.nome = nome
        self.serie = serie
        self.ano_nascimento = ano_nascimento
        self.cadastro = "inativo" 
        self.retirada = "decremento"

    def cadastrar(self, acrescentar):
        self.cadastro = acrescentar
        print("Cadastrado com sucesso!")

    def retirar(self,retirar):
        self.retirada = retirar
        print("Matricula retirada!")

matricula1 = Matricula("Amanda", "nono", "2009")
matricula2 = Matricula("João", "terceiro EM", "2003")

print(matricula1.nome)
matricula1.cadastrar("")
matricula2.retirar("")