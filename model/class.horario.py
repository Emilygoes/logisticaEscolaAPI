

class Horario:
    def __init__(self, turno, serie, periodos):
        self.turno = turno
        self.serie = serie
        self.periodos = periodos
        self.horario = "criar" 
        self.altera = "alterar"

    def criar_horario(self, criar):
        self.criar_horario = criar
        print("Criado com sucesso!")

    def alterar(self,alterar):
        self.alterar = alterar
        print("Alterado com sucesso!")

horario1 = Horario("Noturno", "nono", "18:30-19:20-20:00-20:15-21:00-21:45")
horario2 = Horario("Matutino", "terceiro EM", "07:45-08:30-09:00-09:45-10:00")

print(horario1.periodos)
horario1.criar_horario("")
horario2.alterar("")

