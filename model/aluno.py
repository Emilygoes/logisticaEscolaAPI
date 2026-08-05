from sqlalchemy import Column, String
from database import Base

class Aluno(Base):

    __tablename__ = "aluno"
    cpf = Column(String, primary_key = True, index = True)
    nome_primeiro = Column (String(50), nullable = False)
    nome_sobrenome = Column(String(100), nullable = False)
    data_nascimento = Column(String, nullable = False)
    telefone = Column (String(15), nullable = False)
