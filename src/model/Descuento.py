from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from src.model.declarative_base import Base
from .Trabajador import Trabajador
from datetime import date

class Descuento(Base):
    __tablename__ = 'descuento'

    id = Column(Integer, primary_key=True)
    fecha = Column(Date)
    diasFalta = Column(Integer)
    minutosTardanza = Column(Integer)
    trabajador_id = Column(Integer, ForeignKey('trabajador.id'))
    trabajador = relationship("Trabajador", backref="descuento")

    def __init__(self,
        fecha: date,
        diasFalta: int,
        minutosTardanza: int,
        trabajador: Trabajador
    ):
        self.fecha = fecha
        self.diasFalta = diasFalta
        self.minutosTardanza = minutosTardanza
        self.trabajador = trabajador