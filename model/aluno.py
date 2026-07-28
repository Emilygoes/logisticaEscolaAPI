class Aluno:

    def __init__(self, id_aluno, nome, sobrenome, nascimento, cpf, telefone):
        self.id_aluno = id_aluno
        self.nome = nome
        self.sobrenome = sobrenome
        self.nascimento = nascimento
        self.cpf = cpf
        self.telefone = telefone

Class disciplinas:

    def__init__(self, id_disciplina, nome_disciplina, codigo, carga_horaria, ementa)
        self.id_disciplina = id_disciplina
        self.nome_disciplina = nome-disciplina
        self.codigo = codigo
        self.carga_horaria = carga_horaria
        self.ementa = ementa

Class turma:

    def__init__(self, id_turma, codigo_turma, ano_letivo, turno, capacidade)
        self.id_turma = id_turma
        self.codigo_turma = codigo_turma
        self.ano_letivo = ano_letivo
        self.turno = turno
        self.capacidade = capacidade

Class matricula:

    def__init__(self, id_matricula, data_matricula, forma_ingresso, status)
        self.id_matricula = id_matricula
        self.data_matricula = data_matricula
        self.forma_ingresso = forma_ingresso
        self.status = status

class Grade:

    def __init__(self, id_grade, dia_semana, horario_inicio, hora_fim, sala):
        self.id_grade = id_grade
        self.dia_semana = dia_semana
        self.horario_inicio = horario_inicio
        self.hora_fim = horario_fim
        self.sala = sala

class Professor:

    def __init__(self, id_professor, primeiro_nome, sobrenome, titulacao, cpf, telefone):
        self.id_professor = id_professor
        self.primeiro_nome = primeiro_nome
        self.sobrenome = sobrenome
        self.titulacao = titulacao
        self.cpf = cpf
        self.telefone = telefone
        
