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

@app.get("/professor")
def listarAluno():
    session = SessionLocal()
    professor = session.query(professor).all()
    resultado = [{"cpf": u.cpf, "Nome_primeiro": u.nome, "Nome_sobrenome": u.sobrenome, "Titulacao": u.titulacao, "telefone": u.telefone}
                for u in professor]
    return resultado

@app.get("/agendamento")
def listarAgendamento():
    session = SessionLocal()
    agendamento = session.query(agendamento).all()
    resultado = [{"Turma": u.turma, "Turno": u.turno, "Materiais": u.materiais, "Agenda": u.agenda}
                for u in agendamento]
    return resultado

@app.get("/grade")
def listarGrade():
    session = SessionLocal()
    grade = session.query(grade).all()
    resultado = [{"Id_grade": u.id_grade, "Numero_turma": u.numero_turma, "Codigo_disciplina": u.codigo_disciplina, "Cpf_professor": u.cpf_professor, "Dia_semana": u.dia_semana, "Hora_inicio": u.hora_inicio, "Hora_fim": u.hora_fim, "Sala": u.sala}
                for u in grade]
    return resultado    

@app.get("/matricula")
def listarMatricula():
    session = SessionLocal()
    matricula = session.query(matricula).all()
    resultado = [{"N_matricula": u.n_matricula, "Cpf": u.cpf, "Numero_turma": u.numero_turma, "Status_matricula": U.status_matricula, "forma_ingresso":forma_ingresso}
                 for u in matricula]
    return resultado

@app.get("/disciplina")
def listarTurma():
    session = SessionLocal()
    disciplina = session.query(disciplina).all()
    resultado = [{"Codigo_disciplina": u.codigo_disciplina, "Nome_disciplina": u.nome_disciplina, "codigo": u.codigo, "Carga_horaria": u.carga_horaria, "ementa": u.ementa}
                 for u in turma]
    return resultado

@app.get("/turma")
def listarDisciplina():
    session = SessionLocal()
    turma = session.query(disciplina).all()
    resultado = [{}]