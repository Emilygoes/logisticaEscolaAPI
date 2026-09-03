from database import SessionLocal
from matricula import Matricula

session = SessionLocal()

nova_matricula = Matricula(n_matricula= 1432, cpf= "234353943", numero_turma= 202, status_matricula = "nao sei", forma_ingresso="prova")
session.add(nova_matricula)
session.commit()
print("Matricula feita!")

session.close