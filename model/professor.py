from sqlalchemy import Column, Integer, String
from database import Base

class Professor(Base):

    __tablename__ = "professor"
    cpf = Column(integer, primary_key = True, index = True)
    nome_primeiro = Column (String(50), nullable = False)
    nome_sobrenome = Column(String(100), nullable = False)
    titulacao = Column(String, nullable = False)
    telefone = Column (Integer(15), nullable = False)