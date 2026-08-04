from database import SessionLocal
from model import agendamento

session = SessionLocal()

novo_agendamento = agendamento ("nono ano", "Vespertino", "Matemática, inglês, potuguês, espanhol, artes")
session.add(novo_agendamento)
session.commit()
print("Agendamento feito!")