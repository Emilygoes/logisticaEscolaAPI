from database import SessionLocal
from grade import Grade

session = SessionLocal()

nova_grade = Grade(id_grade= 1, numero_turma= 301, codigo_disciplina = "1235", cpf_professor="19458649300", dia_semana= "1", hora_inicio= "745", hora_fim="1145", sala= "2")
session.add(nova_grade)
session.commit()
print("Agendamento feito!")

session.close()