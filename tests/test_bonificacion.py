import unittest
from datetime import date
from src.logic.PersistenciaBonificacion import PersistenciaBonificacion
from src.model.Trabajador import Trabajador
from src.model.Bonificacion import Bonificacion
from src.model.declarative_base import Session, Base, engine
from .data_trabajador import trabajadores_data


class BonificacionTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        # Creamos la clase PersitenciaTrabajador
        self.persistencia = PersistenciaBonificacion()

        # Generando Esquema
        Base.metadata.create_all(engine)

        # Abrimos la session
        self.session = Session()

        # Registramos algunos trabajadores
        self.trabajador1 = Trabajador(trabajadores_data[0]["mesanio"], trabajadores_data[0]["nombre"], trabajadores_data[0]["sueldo"])
        self.trabajador2 = Trabajador(trabajadores_data[1]["mesanio"], trabajadores_data[1]["nombre"], trabajadores_data[1]["sueldo"])
        # Adicionamos a la sesion
        self.session.add(self.trabajador1)
        self.session.add(self.trabajador2)

        # Registramos unas bonificaciones
        self.bonificacion1 = Bonificacion(date(2023, 2, 1), 4, 1000, self.trabajador1)
        self.bonificacion2 = Bonificacion(date(2022, 1, 9), 3, 1000, self.trabajador2)
        self.bonificacion3 = Bonificacion(date(2019, 3, 10), 7, 1000, self.trabajador2)
        self.bonificacion4 = Bonificacion(date(2015, 6, 11), 9, 1000, self.trabajador1)
        #Adicionamos a la sesion
        self.session.add(self.bonificacion1)
        self.session.add(self.bonificacion2)
        self.session.add(self.bonificacion3)
        self.session.add(self.bonificacion4)

        # Peristimos los datos y cerramos sesion
        self.session.commit()
        self.session.close()

    def setUp(self) -> None:
        # Abir la Sesion
        self.session = Session()
    
    def tearDown(self) -> None:
        # Abrimos la sesion
        """ self.session = Session()

        # Consultamos todas las Bonificaciones
        busqueda = self.session.query(Bonificacion).all()

        # Borramos todos los registros
        for bonificacion in busqueda:
            self.session.delete(bonificacion)

        # Consultamos todos los trabajadores
        busqueda = self.session.query(Trabajador).all()

        # Borramos todos los registros
        for trabajador in busqueda:
            self.session.delete(trabajador)

        self.session.commit()
        self.session.close() """

        # Para vaciar la base de datos
        # Base.metadata.drop_all(engine)

    def test_registrar_bonificacion(self):
        """Prueba de registro de bonificacion
        """
        resultado = self.persistencia.registrarBonificaion(date(2023, 2, 1), 15, 0, self.trabajador1)
        resultado2 = self.persistencia.registrarBonificaion(date(2023, 1, 3), 15, 0, self.trabajador1)
        
        self.assertTrue(resultado)
        self.assertTrue(resultado2)

    def test_registrar_bonificacion_negativa(self):
        """Prueba de registro de bonificacion negativa
        """
        resultado = self.persistencia.registrarBonificaion(date(2022, 1, 6), 10, -15, self.trabajador2)
        
        self.assertFalse(resultado)

    def test_horas_extra_negativa(self):
        """Prueba de registro de bonificacion con horas extras negativas
        """
        resultado = self.persistencia.registrarBonificaion(date(2022, 3, 7), -9, 1000, self.trabajador1)
        
        self.assertFalse(resultado)

    def test_ingreso_de_caracteres_alfabeticos(self):
        """Prueba de registro de bonificacion con caracteres alfabéticos en horas extras y movilidad
        """
        resultado1 = self.persistencia.registrarBonificaion(date(2022, 3, 7), "6", 1000, self.trabajador1)
        resultado2 = self.persistencia.registrarBonificaion(date(2022, 3, 9), 6, "1000", self.trabajador2)
        
        self.assertFalse(resultado1)
        self.assertFalse(resultado2)

    def test_fechas_futuras(self):
        """No se deben permitir fechas que aún no llegan
        """
        resultado = self.persistencia.registrarBonificaion(date(2025, 3, 7), 5, 1000, self.trabajador1)
        
        self.assertFalse(resultado)

    def test_ingreso_vacio_en_fecha(self):
        """Prueba de registro de bonificacion con campo vacio en fecha
        """
        resultado1 = self.persistencia.registrarBonificaion(None, 5, 1000, self.trabajador2)
        resultado2 = self.persistencia.registrarBonificaion("", 6, 1000, self.trabajador2)
        
        self.assertFalse(resultado1)
        self.assertFalse(resultado2)

    def test_ingreso_no_enteros_en_horas_extras(self):
        resultado1 = self.persistencia.registrarBonificaion(date(2022, 3, 2), 5.6, 1000, self.trabajador1)
        resultado2 = self.persistencia.registrarBonificaion(date(2012, 9, 7), 6.1, 1000, self.trabajador1)
        
        self.assertFalse(resultado1)
        self.assertFalse(resultado2)
