from sqlalchemy import Column, Integer, String
from database import Base


class Grade(Base):
    __tablename__ = "grade_horaria"
    id_grade = Column(Integer, primary_key= True, index=True )
    numero_turma = Column(Integer, nullable= False)
    codigo_disciplina = Column(String, nullable=False)
    cpf_professor = Column(String, nullable=False)
    dia_semana = Column(String, nullable=False)
    hora_inicio = Column(String, nullable= False)
    hora_fim = Column (String, nullable= False)
    sala = Column(String, nullable= False) 