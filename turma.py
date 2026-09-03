from sqlalchemy import Column, Integer, String
from database import Base

class Turma(Base):
    __tablename__ = "turma"
    numero_turma = Column(Integer, primary_key = True, index = True)
    codigo_turma = Column (String(50), nullable = False)
    ano_letivo = Column(Integer, nullable = False)
    turno = Column(String, nullable = False)
    capacidade = Column (Integer, nullable = False)