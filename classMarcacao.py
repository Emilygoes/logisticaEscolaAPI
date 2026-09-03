class Marcacao:
    def __init__(self, nome, serie, notas):
        self.nome = nome
        self.serie = serie
        self.notas = notas
        self.aprova = "aprovacao" 
        self.reprova = "reprovacao"

    def aprovar(self, aprovacao):
        self.aprovar = aprovacao
        print("Aprovado com sucesso!")

    def reprovar(self,retirar):
        self.reprovar = retirar
        print("Reprovado!")

marcacao1 = Marcacao("Amanda", "nono", "4.5, 7.5, 10.0, 10.0")
marcacao2 = Marcacao("João", "terceiro EM", "5.0, 2.0, 6.4, 3.0")

print(marcacao1.nome)
marcacao1.aprovar("")
marcacao2.reprovar("")
