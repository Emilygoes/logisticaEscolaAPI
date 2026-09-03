from sqlalchemy import Column, Integer, String
from database import Base


class Matricula(Base):
    __tablename__ = "matricula"
    n_matricula = Column (Integer, primary_key = True, index= True)
    cpf =Column( String(11), nullable = False)
    numero_turma = Column (Integer, nullable = False)
    status_matricula = Column(String(30), nullable = False)
    forma_ingresso = Column(String(50), nullable = False)