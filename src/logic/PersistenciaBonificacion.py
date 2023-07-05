from src.model.Bonificacion import Bonificacion
from src.model.Trabajador import Trabajador
from src.model.declarative_base import session
from sqlalchemy.exc import SQLAlchemyError
from datetime import date

class PersistenciaBonificacion():
    def registrarBonificaion(self,
        fecha: date,
        horasExtra: int,
        movilidad: float | int,
        trabajador: Trabajador
    ):
        # Verificación de Tipo de datos
        if not isinstance(fecha, date):
            return False
        
        if not (isinstance(movilidad, float) or isinstance(movilidad, int)):
            return False
        
        if not isinstance(trabajador, Trabajador):
            return False

        # El software permitirá ingresar solamente números enteros en las horas extras.
        if not isinstance(horasExtra, int):
            return False
        
        # Las bonificación por movilidad tiene que tener un número positivo
        if movilidad < 0:
            return False
        
        # Las horas extras ingresadas sólo permiten números positivos mayores a 0.
        if horasExtra < 0:
            return False
        
        # No se permite el ingreso nulo en el campo de fecha.
        if not fecha or fecha == "":
            return False
        
        # No permitir fechas futuras
        if fecha > date.today():
            return False
        
        # REGISTRAMOS LA BONIFICACION
        bonificaon = Bonificacion(fecha, horasExtra, movilidad, trabajador)
        session.add(bonificaon)
        session.commit()

        return True
        
    def verBonificaciones():
        bonificaciones = session.query(Bonificacion).all()
        print('\n-------- BONIFICACIONES REGISTRADOS --------')
        for bonificacion in bonificaciones:
            print(f'id_trabajador: {bonificacion.trabajador_id} Horas Extra: {bonificacion.horasExtra} Movilidad: {bonificacion.movilidad} Fecha: {bonificacion.fecha}')
        print('')
