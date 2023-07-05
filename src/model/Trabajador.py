from sqlalchemy import Column, String, Integer, Float
from src.model.declarative_base import Base

class Trabajador(Base):
    __tablename__ = 'trabajador'

    id = Column(Integer, primary_key=True)
    mesAnio = Column(String)
    nombreTrabajador = Column(String)
    sueldoBasico = Column(Float)

    def __init__(self,
        mesAnio: str,
        nombreTrabajador: str,
        sueldoBasico: float
    ):
        self.mesAnio = mesAnio
        self.nombreTrabajador = nombreTrabajador
        self.sueldoBasico = sueldoBasico