from database import SessionLocal
from professor import Professor

session = SessionLocal()

novo_professor = Professor(cpf= "19458649300", nome= "Ricardo", sobrenome = "Vasconcelhos", titulacao = "química", telefone = "12346578")
session.add(novo_professor)
session.commit()
print("Professor cadastrado!")

session.close