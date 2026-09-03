from database import SessionLocal
from disciplina import Disciplina

session = SessionLocal()

nova_disciplina = Disciplina(codigo_disciplina = 1235, nome_disciplina= "Matemática", codigo = "a92cis", carga_horaria = 38, ementa ="????")
session.add(nova_disciplina)
session.commit()
print("Disciplina adicionada!")

session.close()