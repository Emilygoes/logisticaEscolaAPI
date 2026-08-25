from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import SessionLocal
from aluno import Aluno

app = FastAPI()

app.add_middleware(
     CORSMiddleware,
     allow_origins=["*"],
     allow_methods=["*"],
     allow_headers=["*"]
)

@app.get("/alunos")
def listarAluno():
    session = SessionLocal()
    aluno = session.query(Aluno).all()
    resultado = [{"cpf": u.cpf, "Nome_primeiro": u.nome, "Nome_sobrenome": u.sobrenome, "Data_nascimento": u.data_nascimento, "telefone": u.telefone}
                for u in aluno]
    return resultado
