from sqlalchemy import Column, String, Date
from database import Base

class Aluno(Base):

    __tablename__ = "alunos"
    cpf = Column(String, primary_key = True, index = True)
    nome = Column (String(50), nullable = False)
    sobrenome = Column(String(100), nullable = False)
    data_nascimento = Column(Date, nullable = False)
    telefone = Column (String(15), nullable = False)
