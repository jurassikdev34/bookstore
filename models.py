from sqlalchemy import Column, Integer, String, TIMESTAMP, func
from database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False, index=True)
    password_hash = Column(String, nullable=False)
    ciudad = Column(String, nullable=True)
    fecha_registro = Column(TIMESTAMP, server_default=func.now())

