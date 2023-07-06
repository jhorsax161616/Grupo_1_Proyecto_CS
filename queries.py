from datetime import date
from src.model.Trabajador import Trabajador
from src.model.Bonificacion import Bonificacion
from src.model.Descuento import Descuento
from src.model.declarative_base import Base, engine, Session

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
    print(datosPago.id, datosPago.trabajador_id, datosPago.horasExtra, datosPago.movilidad)

""" for c, i in session.query(Trabajador, Bonificacion).filter(Trabajador.id == Bonificacion.id).all():
   print ("ID: {} Name: {} ".format(c.id, c.nombreTrabajador))

for c, i in session.query(Trabajador, Descuento).filter(Trabajador.id == Descuento.id).all():
   print ("ID: {} Name: {} ".format(c.id, i.diasFalta))


result = session.query(Trabajador).join(Descuento).all()
for row in result:
   for des in row.descuento:
            print (row.id, des.id)


for c, i in session.query(Trabajador, Descuento) \
    .filter(Trabajador.id == Descuento.id) \
    .all():
    print ("ID: {} Name: {}".format(c.id, i.diasFalta))

print("Tres:")
for c, i, x in session.query(Trabajador, Descuento, Bonificacion) \
    .filter(Trabajador.id == Descuento.id) \
    .filter(Trabajador.id == Bonificacion.id) \
    .all():
   print ("ID: {} Name: {} {} ".format(c.id, i.diasFalta, x.movilidad)) """