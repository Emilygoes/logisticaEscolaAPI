from database import SessionLocal
from aluno import Aluno

session = SessionLocal

novo_aluno = Aluno ( cpf= "12332145600", nome_primeiro = "julia", nome_sobrenome="borges", data_nascimento = "12/12/2008", telefone="55-49-3465-0350")
session.add(novo_aluno)
s