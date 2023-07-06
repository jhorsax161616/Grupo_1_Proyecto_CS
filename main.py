from src.logic.PersistenciaTrabajador import PersistenciaTrabajador
from src.logic.PersistenciaBonificacion import PersistenciaBonificacion
from src.logic.PersistenciaDescuento import PersistenciaDescuento
from src.model.Trabajador import Trabajador
from src.model.Bonificacion import Bonificacion
from src.model.Descuento import Descuento
from src.model.declarative_base import Session, Base

def verDatos():
    trabajador = PersistenciaTrabajador()
    trabajador.verTrabajadores()
    bonificacion = PersistenciaBonificacion()
    bonificacion.verBonificaciones()
    descuento = PersistenciaDescuento()
    descuento.verDescuentos()

def verTrabajadoresBonificacion():
    # create a new session
    session = Session()
    # 3 - extract all movies
    trabajadores = session.query(Trabajador).all()

    # Imprimir trabajadores
    print('\n### Todos los trabajadores:')
    for trabajador in trabajadores:
        print(f'Id: {trabajador.id} - Mes-Año: {trabajador.mesAnio} - Nombre: {trabajador.nombreTrabajador:25} - Sueldo básico: {trabajador.sueldoBasico}')
    print('')

    datosPagos = session.query(Bonificacion).join(Trabajador).all()

    for datosPago in datosPagos:
        print(f"Trabajador: {datosPago.trabajador.nombreTrabajador}, Horas Extra: {datosPago.horasExtra}, movilidad: {datosPago.movilidad}")


if __name__ == '__main__':
    verTrabajadoresBonificacion()