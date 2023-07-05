from sqlalchemy import Column, Integer, Float, ForeignKey, Date
from sqlalchemy.orm import relationship
from src.model.declarative_base import Base
from .Trabajador import Trabajador
from datetime import date

class Bonificacion(Base):
    __tablename__ = 'bonificacion'

    id = Column(Integer, primary_key=True)
    fecha = Column(Date)
    horasExtra = Column(Integer)
    movilidad = Column(Float)
    trabajador_id = Column(Integer, ForeignKey('trabajador.id'))
    trabajador = relationship("Trabajador", backref="bonificacion")

    def __init__(self,
        fecha: date,
        horasExtra: int,
        movilidad: float,
        trabajador: Trabajador
    ):
        self.fecha = fecha
        self.horasExtra = horasExtra
        self.movilidad = movilidad
        self.trabajador = trabajador