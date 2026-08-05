from database import SessionLocal
from agendamento import Agendamento

session = SessionLocal()

novo_agendamento = Agendamento(turma= "sexto ano", turno= "Vespertino", materiais = "Matemáticas", agenda = "sim")
session.add(novo_agendamento)
session.commit()
print("Agendamento feito!")

session.close