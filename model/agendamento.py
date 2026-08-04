from sqlalchemy import Column, Integer, String
from database import Base

class Agendamento(Base):
    _tablename__ = "agendamentos"
    turma = Column(Integer, primary_key = True, index= True)
    turno = Column (String(100), nullable = False)
    materiais = Column (String(100), nullable= False)
    agenda = Column (String(100), nullable= False)

    def agendar(self, lista):
        self.agendar = lista
        print("Agendamento realizado.")

agendamento1 = Agendamento("nono ano", "Vespertino", "Matemática, inglês, potuguês, espanhol, artes")
agendamento2 = Agendamento("terceiro EM", "Matutino", "Geografia, Artes, Biologia, Espanhol, Matemática")

print(agendamento1.turma)
agendamento1.agendar("")
agendamento2.agendar("")