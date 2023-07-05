from src.model.Trabajador import Trabajador
from src.model.declarative_base import session
from sqlalchemy.exc import SQLAlchemyError
import re
import datetime

class PersistenciaTrabajador():
    def registrarTrabajador(self,
        nombre: str,
        sueldo: float | int,
        mesanio: str = datetime.datetime.now().strftime('%B %Y') # Por defecto asigna fecha actual
    ) -> bool:
        # Verificación de Tipo de datos
        if not isinstance(mesanio, str):
            return False
        
        if not isinstance(nombre, str):
            return False
        
        if not (isinstance(sueldo, float) or isinstance(sueldo, int)):
            return False

        # El software no deberá dejar campos vacíos en los nombres, al registrar el nombre del trabajador.
        if not nombre or nombre == '':
            return False
        
        # El software no deberá permitir el ingreso de caracteres números, al registrar el nombre del trabajador.
        if re.search(r'\d', nombre):
            return False
        
        # El software no deberá permitir ingresar símbolos, al registrar el nombre del trabajador
        if re.search(r"[^\w\s]", nombre):
            return False
        
        # El software no deberá permitir el ingreso de sueldo básico negativo al registrar el sueldo.
        if sueldo < 0:
            return False
        
        # El software solo deberá permitir como máximo hasta 35 caracteres, al registrar el nombre del trabajador.
        if len(nombre) > 35:
            return False
        
        # El software no deberá permitir el ingreso de dos nombres iguales al registrar el nombre del trabajador
        busqueda = session.query(Trabajador).filter(Trabajador.nombreTrabajador == nombre).all()
        if len(busqueda) != 0:
            return False
        
        # AGREGAMOS AL TRABAJADOR
        trabajador = Trabajador(mesanio, nombre, sueldo)
        session.add(trabajador)
        session.commit()

        return True
    
    def verTrabajadores(self):
        trabajadores = session.query(Trabajador).all()
        print('\n-------- TRABAJADORES REGISTRADOS --------')
        for trabajador in trabajadores:
            print(f'nombre: {trabajador.nombreTrabajador} sueldo: {trabajador.sueldoBasico}')
        print('')