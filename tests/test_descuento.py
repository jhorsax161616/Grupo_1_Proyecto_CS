import unittest
from datetime import date
from src.logic.PersistenciaDescuento import PersistenciaDescuento
from src.model.Trabajador import Trabajador
from src.model.Descuento import Descuento
from src.model.declarative_base import Session, Base, engine
from .data_trabajador import trabajadores_data


class DescuentoTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        # Creamos la clase PersitenciaTrabajador
        self.persistencia = PersistenciaDescuento()

        # Generando Esquema
        Base.metadata.create_all(engine)

        # Abrimos la session
        self.session = Session()

        # Registramos algunos trabajadores
        self.trabajador1 = Trabajador(trabajadores_data[2]["mesanio"], trabajadores_data[2]["nombre"], trabajadores_data[2]["sueldo"])
        self.trabajador2 = Trabajador(trabajadores_data[3]["mesanio"], trabajadores_data[3]["nombre"], trabajadores_data[3]["sueldo"])
        # Adicionamos a la sesion
        self.session.add(self.trabajador1)
        self.session.add(self.trabajador2)

        # Registramos unos descuentos
        self.descuento1 = Descuento(date(2021, 2, 1), 2, 200, self.trabajador1)
        self.descuento2 = Descuento(date(2016, 11, 5), 3, 100, self.trabajador2)
        self.descuento3 = Descuento(date(2018, 5, 10), 1, 10, self.trabajador2)
        self.descuento4 = Descuento(date(2015, 7, 11), 5, 26, self.trabajador1)
        #Adicionamos a la sesion
        self.session.add(self.descuento1)
        self.session.add(self.descuento2)
        self.session.add(self.descuento3)
        self.session.add(self.descuento4)

        # Peristimos los datos y cerramos sesion
        self.session.commit()
        self.session.close()

    def setUp(self) -> None:
        # Abir la Sesion
        self.session = Session()
    
    def tearDown(self) -> None:
        # Abrimos la sesion
        """ self.session = Session()

        # Consultamos todos los trabajadores
        busqueda = self.session.query(Descuento).all()

        # Borramos todos los registros
        for descuento in busqueda:
            self.session.delete(descuento)

        # Consultamos todos los trabajadores
        busqueda = self.session.query(Trabajador).all()

        # Borramos todos los registros
        for trabajador in busqueda:
            self.session.delete(trabajador)

        self.session.commit()
        self.session.close() """

        # Para vaciar la base de datos
        # Base.metadata.drop_all(engine)

    def test_registrar_descuento(self):
        """Prueba de registro de descuento
        """
        resultado = self.persistencia.registrarDescuento(3, 20, self.trabajador2, date(2021, 11, 9))
        resultado2 = self.persistencia.registrarDescuento(1, 0, self.trabajador2)
        
        self.assertTrue(resultado)
        self.assertTrue(resultado2)

    def test_ingreso_vacio_en_fecha(self):
        """Prueba de registro de descuento con campo vacio en fecha
        """
        resultado1 = self.persistencia.registrarDescuento(2, 15, self.trabajador1, None)
        resultado2 = self.persistencia.registrarDescuento(1, 30, self.trabajador2, "")
        
        self.assertFalse(resultado1)
        self.assertFalse(resultado2)

    def test_ingreso_no_enteros_en_dias_falta_y_minutos_tardanza(self):
        """Prueba de ingreso de numeros no enteros en los minutos y días
        """
        resultado1 = self.persistencia.registrarDescuento(5.6, 100, self.trabajador1)
        resultado2 = self.persistencia.registrarDescuento(3, 15.6, self.trabajador1)
        
        self.assertFalse(resultado1)
        self.assertFalse(resultado2)

    def test_ingreso_negativo_dias_y_minutos(self):
        resultado1 = self.persistencia.registrarDescuento(-5, 100, self.trabajador1)
        resultado2 = self.persistencia.registrarDescuento(3, -60, self.trabajador2)
        
        self.assertFalse(resultado1)
        self.assertFalse(resultado2)

    def test_ingreso_caracteres_alfabeticos_en_dias_y_minutos(self):
        resultado1 = self.persistencia.registrarDescuento("3", 100, self.trabajador1)
        resultado2 = self.persistencia.registrarDescuento(3, "a", self.trabajador2)
        
        self.assertFalse(resultado1)
        self.assertFalse(resultado2)

    def test_fechas_futuras(self):
        """No se deben permitir fechas que aún no llegan
        """
        resultado = self.persistencia.registrarDescuento(5, 10, self.trabajador1, date(2025, 3, 7))
        
        self.assertFalse(resultado)