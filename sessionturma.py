from database import SessionLocal
from turma import Turma

session = SessionLocal()

nova_turma = Turma(numero_turma= 301, codigo_turma= "342234", ano_letivo = 2026, turno = "matutino", capacidade=31)
session.add(nova_turma)
session.commit()
print("turma criada com sucesso!")

session.close