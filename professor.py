from sqlalchemy import Column, String
from database import Base

class Professor(Base):

    __tablename__ = "professor"
    cpf = Column(String, primary_key = True, index = True)
    primeiro = Column (String(50), nullable = False)
    sobrenome = Column(String(100), nullable = False)
    titulacao = Column(String(100), nullable = False)
    telefone = Column (String(15), nullable = False)