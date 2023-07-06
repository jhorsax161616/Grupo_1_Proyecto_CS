from src.model.Descuento import Descuento
from src.model.Trabajador import Trabajador
from src.model.declarative_base import session
from sqlalchemy.exc import SQLAlchemyError
from datetime import date

class PersistenciaDescuento():
    def registrarDescuento(self,
        diasFalta: int,
        minutosTardanza: int,
        trabajador: Trabajador,
        fecha: date = date.today()
    ):
        # Verificación de Tipo de datos
        if not isinstance(fecha, date):
            return False
        
        # El software permitirá ingresar solamente números enteros en los días de falta y minutos de tardanza.
        # El software no permitirá ingresar caracteres alfabéticos en los campos de registro de días y minutos de tardanza.
        if not isinstance(diasFalta, int):
            return False
        
        if not isinstance(minutosTardanza, int):
            return False
        
        if not isinstance(trabajador, Trabajador):
            return False
        
        # El software no deberá dejar ingresar campos vacíos en la fecha.
        if not fecha or fecha == "":
            return False
        
        # El software permitirá ingresar solamente números positivos en los días de falta y minutos de tardanza.
        if minutosTardanza < 0:
            return False
        
        if diasFalta < 0:
            return False

        # No permitir fechas futuras
        if fecha > date.today():
            return False
        
        # REGISTRAMOS EL DESCUENTO
        descuento = Descuento(fecha, diasFalta, minutosTardanza, trabajador)
        session.add(descuento)
        session.commit()

        return True

        
    def verDescuentos(self):
        descuentos = session.query(Descuento).all()
        print('\n-------- DESCUENTOS REGISTRADOS --------')
        for descuento in descuentos:
            print(f'id_trabajador: {descuento.trabajador_id} Dias Falta: {descuento.diasFalta} Minutos Tardanza: {descuento.minutosTardanza} Fecha: {descuento.fecha}')
        print('')