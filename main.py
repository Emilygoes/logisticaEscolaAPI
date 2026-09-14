from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import SessionLocal
from aluno import Aluno
from professor import Professor
from agendamento import Agendamento
from grade import Grade
from matricula import Matricula
from disciplina import Disciplina
from turma import Turma

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
    resultado = [{"cpf": u.cpf, "nome": u.nome, "sobrenome": u.sobrenome, "data_nascimento": u.data_nascimento, "telefone": u.telefone}
                for u in aluno]
    return resultado

@app.post("/aluno")
def criarAluno(cpf: str, nome: str, sobrenome: str, data_nascimento: str, telefone: str):
    session = SessionLocal()
    novo_aluno = Aluno( cpf=cpf, nome=nome, sobrenome=sobrenome, data_nascimento=data_nascimento, telefone=telefone)
    session.add(novo_aluno)
    session.commit()
    session.close()
    return {"mensagem": "Novo aluno adicionado!"}

@app.put("/aluno/{cpf}")
def atualizarAluno(cpf: str, nome: str, sobrenome: str, data_nascimento: str, telefone: str):
    session = SessionLocal()
    aluno = session.query(Aluno).filter(Aluno.cpf == cpf).first()
    if aluno:
        aluno.nome = nome
        aluno.sobrenome = sobrenome
        aluno.data_nascimento = data_nascimento
        aluno.telefone = telefone
        session.commit()
        session.close()
        return {"mensagem": "Aluno atualizado!"}
    session.close()
    return {"mensagem": "Aluno não encontrado!"}


@app.delete("/aluno/{cpf}")
def deletarAluno(cpf: str):
    session = SessionLocal()
    aluno = session.query(Aluno).filter(Aluno.cpf == cpf).first()
    if aluno:

        session.delete(aluno)
        session.commit()
        session.close()
        return {"mensagem": "Aluno deletado!"}
    session.close()
    return {"mensagem": "Aluno não encontrado!"}



@app.get("/professor")
def listarProfessor():
    session = SessionLocal()
    professor = session.query(professor).all()
    resultado = [{"cpf": u.cpf, "nome": u.nome, "sobrenome": u.sobrenome, "titulacao": u.titulacao, "telefone": u.telefone}
                for u in professor]
    return resultado

@app.post("/professor")
def criarProfessor(cpf: str, nome: str, sobrenome: str, titulacao: str, telefone: str):
    session = SessionLocal()
    novo_professor = Professor( cpf=cpf, nome=nome, sobrenome=sobrenome, titulacao=titulacao, telefone=telefone)
    session.add(novo_professor)
    session.commit()
    session.close()
    return {"mensagem": "Novo professor adicionado!"}

@app.put("/professor/{cpf}")
def atualizarProfessor(cpf: str, nome: str, sobrenome: str, titulacao: str, telefone: str):
    session = SessionLocal()
    professor = session.query(Professor).filter(Professor.cpf == cpf).first()
    if professor:
        professor.nome = nome
        professor.sobrenome = sobrenome
        professor.titulacao = titulacao
        professor.telefone = telefone
        session.commit()
        session.close()
        return {"mensagem": "Professor atualizado!"}
    session.close()
    return {"mensagem": "Professor não encontrado!"}


@app.delete("/professor/{cpf}")
def deletarProfessor(cpf: str):
    session = SessionLocal()
    professor = session.query(Professor).filter(Professor.cpf == cpf).first()
    if professor:

        session.delete(professor)
        session.commit()
        session.close()
        return {"mensagem": "Professor deletado!"}
    session.close()
    return {"mensagem": "Professor não encontrado!"}


@app.get("/agendamento")
def listarAgendamento():
    session = SessionLocal()
    agendamento = session.query(Agendamento).all()
    resultado = [{"turma": u.turma, "turno": u.turno, "materiais": u.materiais, "agenda": u.agenda}
                for u in agendamento]
    return resultado


@app.post("/agendamento")
def criarAgendamento(turma: int, turno: str, materiais: str, agenda: str):
    session = SessionLocal()
    novo_agendamento = Agendamento( turma=turma, turno=turno, materiais=materiais, agenda=agenda)
    session.add(novo_agendamento)
    session.commit()
    session.close()
    return {"mensagem": "Novo agendamento"}

@app.put("/agendamento/{turma}")
def atualizarAgendamento(turma: int, turno: str, materiais: str, agenda: str):
    session = SessionLocal()
    agendamento = session.query(Agendamento).filter(Agendamento.turma == turma).first()
    if agendamento:
        agendamento.turma = turma
        agendamento.turno = turno
        agendamento.materiais = materiais
        agendamento.agenda= agenda
        session.commit()
        session.close()
        return {"mensagem": "Agendamento atualizado!"}
    session.close()
    return {"mensagem": "Agendamento não encontrado!"}


@app.delete("/agendamento/{turma}")
def deletarAgendamento(turma: int):
    session = SessionLocal()
    agendamento = session.query(Agendamento).filter(Agendamento.turma == turma).first()
    if agendamento:

        session.delete(agendamento)
        session.commit()
        session.close()
        return {"mensagem": "agendamento deletado!"}
    session.close()
    return {"mensagem": "agendamento não encontrado!"}


@app.get("/grade")
def listarGrade():
    session = SessionLocal()
    grade = session.query(Grade).all()
    resultado = [{"id_grade": u.id_grade, "numero_turma": u.numero_turma, "codigo_disciplina": u.codigo_disciplina, "cpf_professor": u.cpf_professor, "dia_semana": u.dia_semana, "hora_inicio": u.hora_inicio, "hora_fim": u.hora_fim, "sala": u.sala}
                for u in grade]
    return resultado

@app.post("/grade")
def criarGrade(id_grade: int, numero_turma: int, codigo_disciplina: str, cpf_professor: str, dia_semana: str, hora_inicio: str, hora_fim: str, sala:str):
    session = SessionLocal()
    nova_grade = Grade( id_grade=id_grade, numero_turma=numero_turma, codigo_disciplina=codigo_disciplina, cpf_professor=cpf_professor, dia_semana=dia_semana, hora_inicio=hora_inicio, hora_fim=hora_fim, sala=sala)
    session.add(nova_grade)
    session.commit()
    session.close()
    return {"mensagem": "Nova grade!"}

@app.put("/grade/{id_grade}")
def atualizarGrade(id_grade: int, numero_turma:int, codigo_disciplina:str, cpf_professor:str, dia_semana:str, hora_inicio:str, hora_fim:str, sala:str):
    session = SessionLocal()
    grade = session.query(Grade).filter(Grade.id_grade == id_grade).first()
    if grade:
        grade.id_grade = id_grade
        grade.numero_turma= numero_turma
        grade.codigo_disciplina=codigo_disciplina
        grade.cpf_professor=cpf_professor
        grade.dia_semana=dia_semana
        grade.hora_inicio=hora_inicio
        grade.hora_fim= hora_fim
        session.commit()
        session.close()
        return {"mensagem": "Grade atualizada!"}
    session.close()
    return {"mensagem": "não há grade!"}


@app.delete("/grade/{id_grade}")
def deletarGrade(id_grade: int):
    session = SessionLocal()
    grade = session.query(Grade).filter(Grade.id_grade == id_grade).first()
    if grade:

        session.delete(Grade)
        session.commit()
        session.close()
        return {"mensagem": "Grade excluida!"}
    session.close()
    return {"mensagem": "grade não existe!"}


@app.get("/matricula")
def listarMatricula():
    session = SessionLocal()
    matricula = session.query(matricula).all()
    resultado = [{"N_matricula": u.n_matricula, "cpf": u.cpf, "numero_turma": u.numero_turma, "status_matricula": u.status_matricula, "forma_ingresso": u.forma_ingresso}
                 for u in matricula]
    return resultado

@app.post("/matricula")
def criarmatricula(n_matricula: int, cpf: str, numero_turma: int, status_matricula: str, forma_ingresso: str):
    session = SessionLocal()
    nova_matricula = Matricula( n_matricula=n_matricula, cpf=cpf, numero_turma=numero_turma, status_matricula=status_matricula, forma_ingresso=forma_ingresso)
    session.add(nova_matricula)
    session.commit()
    session.close()
    return {"mensagem": "Matrícula criada com sucesso adicionado!"}

@app.put("/matricula{n_matricula}")
def atualizarmatricula(n_matricula: int, cpf: str, numero_turma: int, status_matricula: str, forma_ingresso: str):
    session = SessionLocal()
    matricula = session.query(matricula).filter(n_matricula == n_matricula).first()
    if matricula:
        matricula.cpf = cpf
        matricula.numero_turma = numero_turma
        matricula.status_matricula = status_matricula
        matricula.forma_ingresso = forma_ingresso
        session.commit()
        session.close()
        return {"mensagem": "Matrícula atualizado!"}
    session.close()
    return {"mensagem": "Matrícula não encontrado!"}


@app.delete("//{n_matricula}")
def deletarMatricula(n_matricula: str):
    session = SessionLocal()
    matricula = session.query(matricula).filter(matricula.n_matricula == n_matricula).first()
    if matricula:

        session.delete(matricula)
        session.commit()
        session.close()
        return {"mensagem": "Matrícula deletado!"}
    session.close()
    return {"mensagem": "Matrícula não encontrado!"}


@app.get("/disciplina")
def listarDisciplina():
    session = SessionLocal()
    disciplina = session.query(disciplina).all()
    resultado = [{"Codigo_disciplina": u.codigo_disciplina, "nome_disciplina": u.nome_disciplina, "codigo": u.codigo, "Carga_horaria": u.carga_horaria, "ementa": u.ementa}
                 for u in disciplina]
    return resultado

@app.post("/disciplina")
def criarDisciplina(codigo_disciplina: str, nome_disciplina: str, codigo:str, carga_horaria:int, ementa:str):
    session = SessionLocal()
    nova_disciplina = Disciplina( codigo_disciplina=codigo_disciplina, nome_disciplina=nome_disciplina, codigo=codigo, carga_horaria=carga_horaria, ementa=ementa)
    session.add(nova_disciplina)
    session.commit()
    session.close()
    return {"mensagem": "Nova disciplina!"}

@app.put("/disciplina/{codigo_disciplina")
def atualizarDisciplina(codigo_disciplina: str, nome_disciplina: str, codigo: str, carga_horaria: int, ementa: str):
    session = SessionLocal()
    disciplina = session.query(Disciplina).filter(Disciplina.codigo_disciplina == codigo_disciplina).first()
    if disciplina:
        disciplina.codigo_disciplina = codigo_disciplina
        disciplina.nome_disciplina = nome_disciplina
        disciplina.codigo = codigo
        disciplina.carga_horaria = carga_horaria
        disciplina.ementa = ementa
        session.commit()
        session.close()
        return {"mensagem": "Disciplina atualizada!"}
    session.close()
    return {"mensagem": "Disciplina não encontrada."}


@app.delete("/disciplina/{codigo_disciplina}")
def deletarDisciplina(codigo_disciplina: str):
    session = SessionLocal()
    disciplina = session.query(Disciplina).filter(Disciplina.codigo_disciplina== codigo_disciplina).first()
    if disciplina:

        session.delete(disciplina)
        session.commit()
        session.close()
        return {"mensagem": "Disciplina deletada!"}
    session.close()
    return {"mensagem": "Disciplina não encontrada!"}

@app.get("/turma")
def listarTurma():
    session = SessionLocal()
    turma = session.query(turma).all()
    resultado = [{"numero_turma": u.numero_turma, "codigo_turma": u.codigo_turma, "ano_letivo": u.ano_letivo, "turno": u.turno, "capacidade": u.capacidade}
                for u in turma]
    return resultado

@app.post("/turma")
def criarTurma(numero_turma: int, codigo_turma: str, ano_letivo: int, turno: str, capacidade: int):
    session = SessionLocal()
    nova_turma = Turma( numero_turma=numero_turma, codigo_turma=codigo_turma, ano_letivo=ano_letivo, turno=turno, capacidade=capacidade)
    session.add(nova_turma)
    session.commit()
    session.close()
    return {"mensagem": "Nova turma criada!"}

@app.put("/turma/{numero_turma}")
def atualizarTurma(numero_turma: str, codigo_turma: str, ano_letivo: int, turno: str, capacidade: str):
    session = SessionLocal()
    turma = session.query(Turma).filter(Turma.numero_turma == numero_turma).first()
    if turma:
        turma.numero_turma = numero_turma
        turma.codigo_turma = codigo_turma
        turma.ano_letivo = ano_letivo
        turma.turno = turno
        turma.capacidade = capacidade
        session.commit()
        session.close()
        return {"mensagem": "Turma atualizada!"}
    session.close()
    return {"mensagem": "Turma não encontrada!"}


@app.delete("/turma/{numero_turma}")
def deletarTurma(numero_turma: str):
    session = SessionLocal()
    turma = session.query(Turma).filter(Turma.numero_turma == numero_turma).first()
    if turma:

        session.delete(turma)
        session.commit()
        session.close()
        return {"mensagem": "Turma excluida!"}
    session.close()
    return {"mensagem": "Turma não encontrada!"}

    