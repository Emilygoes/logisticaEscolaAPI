from Fastapi import FastAPI

app = FastAPI()

@app.get("/aluno")
def aluno():
    return {
        "cpf": "1",
        "primeiro_nome": "João",
        "sobrenome": "Silva",
        "data_nascimento": "15/05/2008",
        "cpf": "123.456.789-00",
        "telefone": "(49)99999-9999"
    }

@app.get("/professor")
def professor():
    return {
        "cpf": "1",
        "primeiro_nome": "Carlos",
        "sobrenome": "Souza",
        "titulacao": "Mestre",
        "cpf": "987.654.321-00",
        "telefone": "(49)98888-8888"
    }

@app.get("/turma")
def turma():
    return {
        "numero_turma": "1",
        "codigo_turma": "INF301",
        "ano_letivo": "2026",
        "turno": "Matutino",
        "capacidade": "35"
    }

@app.get("/matricula")
def matricula():
    return {
        "cod_matricula": "1",
        "data_matricula": "10/02/2026",
        "forma_ingresso": "Vestibular",
        "status": "Ativa"
    }

@app.get("/grade")
def grade():
    return {
        cod_grade": "1",
        "dia_semana": "Segunda-feira",
        "hora_inicio": "07:30",
        "hora_fim": "08:20",
        "sala": "Laboratório 01"
    }


@app.get("/disciplina")
def disciplina():
    return {
        "nome_disciplina": "1",
        "nome_disciplina": "Banco de Dados",
        "codigo": "BD101",
        "carga_horaria": "80",
        "ementa": "Modelagem de Banco de Dados"
    }

