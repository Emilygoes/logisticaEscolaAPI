class Planejamento:
    def __init__(self, professor, serie, roteiro):
        self.professor = professor
        self.serie = serie
        self.roteiro = roteiro
        self.planeja = "adicionar" 
        self.altera = "alterar"

    def planejar(self, adicionar):
        self.planejar = adicionar
        print("Adicionado com sucesso!")

    def alterar(self,alterar):
        self.alterar = alterar
        print("Alterado com sucesso!")

planejamento1 = Planejamento("Arã", "nono", "Moleculas")
planejamento2 = Planejamento("João", "terceiro EM", "Circunferencia")

print(planejamento1.professor)
planejamento1.planejar("")
planejamento2.alterar("")