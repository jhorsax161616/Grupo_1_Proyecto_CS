import unittest
from src.logic.PersistenciaTrabajador import PersistenciaTrabajador
from src.model.Trabajador import Trabajador
from src.model.declarative_base import Session, Base, engine
from .data_trabajador import trabajadores_data


class TrabajadorTestCase(unittest.TestCase):
    def setUp(self) -> None:
        # Creamos la clase PersitenciaTrabajador
        self.persistencia = PersistenciaTrabajador()

        # Generando Esquema
        Base.metadata.create_all(engine)

        # Abrimos la session
        self.session = Session()

        # Registramos la data
        for trabajador in trabajadores_data:
            self.persistencia.registrarTrabajador(trabajador["nombre"], trabajador["sueldo"], trabajador["mesanio"])

    
    def tearDown(self) -> None:
        # Abrimos la sesion
        self.session = Session()

        # Consultamos todos los trabajadores
        busqueda = self.session.query(Trabajador).all()

        # Borramos todos los registros
        for trabajador in busqueda:
            self.session.delete(trabajador)

        self.session.commit()
        self.session.close()

        # Para vaciar la base de datos
        # Base.metadata.drop_all(engine)

    def test_registrar_trabajador(self):
        """Prueba de registro de trabajador
        """
        resultado = self.persistencia.registrarTrabajador('Jhordan', 1560, 'Agoust 2023')

        self.assertEqual(resultado, True)
    
    def test_registrar_trabajador_nombre_vacio(self):
        """Prueba de registro con nombre vacío
        """
        resultado = self.persistencia.registrarTrabajador('', 1653, 'July 2022')

        self.assertEqual(resultado, False)

    def test_registrar_nombres_con_caracteres_numericos(self):
        """Prueba de registro con caracteres numericos en el nombre
        """
        resultado = self.persistencia.registrarTrabajador('Jhim1', 1200, 'June 2023')

        self.assertEqual(resultado, False)

    def test_registrar_nombres_con_simbolos(self):
        """Prueba de registro con simbolos en el nombre
        """
        resultado = self.persistencia.registrarTrabajador('Rosales De la +', 1500, 'June 2023')

        self.assertEqual(resultado, False)
    
    def test_registrar_nombres_muy_largos(self):
        """Prueba de registro con nombre muy largo mayor a 75 caracteres
        """
        resultado = self.persistencia.registrarTrabajador('El nombre mas largo que existe es este y no puede ser registrado', 1500, 'June 2023')

        self.assertEqual(resultado, False)

    def test_registrar_sueldo_negativo(self):
        """Prueba de registro con sueldo negativo
        """
        resultado = self.persistencia.registrarTrabajador('Osorio', -1200, 'June 2023')

        self.assertEqual(resultado, False)

    def test_registrar_nombres_iguales(self):
        """Prueba de registro con dos nombres iguales
        """
        resultado = self.persistencia.registrarTrabajador('Marta', 2000, 'January 2023')

        self.assertEqual(resultado, False)

    def test_registrar_tipo_dato_erroneo(self):
        """Prueba de registro con tipos de datos incorrectos
        """
        resultado1 = self.persistencia.registrarTrabajador(5, 2000, 'January 2023')
        resultado2 = self.persistencia.registrarTrabajador('Zapata', "hola", 'January 2023')
        resultado3 = self.persistencia.registrarTrabajador('Marta', 2000, 2023)

        self.assertEqual(resultado1, False)
        self.assertEqual(resultado2, False)
        self.assertEqual(resultado3, False)
