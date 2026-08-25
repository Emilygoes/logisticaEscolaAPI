from database import SessionLocal
from aluno import Aluno

session = SessionLocal()

novo_aluno = Aluno(cpf= "14583", nome = "aninha", sobrenome="borges", data_nascimento = "2000_09_09", telefone="55-49-5465-0350")
session.add(novo_aluno)
session.commit()
print("novo aluno adicionado!")

session.close