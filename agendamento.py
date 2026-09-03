from sqlalchemy import Column, Integer, String
from database import Base

class Agendamento(Base):
    __tablename__ = "agendamento"
    turma = Column(Integer, primary_key = True, index= True)
    turno = Column (String(100), nullable = False)
    materiais = Column (String(100), nullable= False)
    agenda = Column (String(100), nullable= False)

   