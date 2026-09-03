from sqlalchemy import Column, Integer, String
from database import Base

class Disciplina(Base):
    __tablename__ = "disciplina"
    codigo_disciplina = Column (String, primary_key = True, index= True )
    nome_disciplina = Column(String(100), nullable= False)
    codigo= Column (String, nullable = False)
    carga_horaria = Column(Integer, nullable = False)
    ementa = Column(String, nullable = False)