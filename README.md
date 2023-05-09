# Proyecto de Fin de Curso: "Salary Horizon 1.0"

Este proyecto está desarrollado por estudiantes de la _Universidad Continental_, propuesto en el curso de ___Construcción de Software___ con la guía del docente [Daniel Gamarra Moreno](https://estudiantesavp.ucontinental.edu.pe/user/profile.php?id=9474), a quién agradecemos encarecidamente por su esfuerzo, apoyo y dedicación por brindarnos sus conocimientos.

## Equipo de Desarrollo

| __Integrante__  | __Apellidos y Nombres__  | __Rol__ |
|:-------------: |:---------------| :-----------------: |
| 1         | Cordova Poma Jhordan Sax | Scrum Master |
| 2         | Hilario Castro Kenss Lin Kadú | Developer |
| 3         | Ingaroca Maldonado Jhim Sebastian | Product Owner |
| 4         | Osorio Alanya Gianfranco          | Developer |
| 5         | Rosales Tapia Brad Jhomers        | Developer |
| 6         | Zapata Medina Juan Diego | Developer |

## Descripción del proyecto

La empresa Horizonte ha decidido implementar un sistema automatizado para el cálculo de los sueldos de sus trabajadores. Se quiere simplificar el proceso de cálculo y asegurarse de que los sueldos se calculen correctamente, evitando errores humanos y reduciendo el tiempo y los costos asociados con el cálculo manual de los sueldos.

### Consigna

#### El trabajador percibe las siguientes bonificaciones

1. Por cada hora extra se le paga 50% más que una hora normal.
1. Bonificación por movilidad igual a 1000.
1. Bonificación suplementaria igual al 3% del sueldo básico (sueldo).
1. La bonificación total es la suma de todas las bonificaciones que percibe.

#### Asimismo, el trabajador está sujeto a los siguientes descuentos

1. Las tardanzas y faltas se descuentan con respecto a remuneración computable. La remuneración computable es igual al sueldo básico más la suma de todas las bonificaciones excepto la bonificación por horas extras.
1. El total de descuentos se obtiene sumando todos los descuentos.

## Objetivos

### Objetivo Principal

- Desarrollar un software que permita a la empresa Horizonte calcular los sueldos de sus trabajadores de manera rápida, precisa y eficiente. Aplicando el desarrollo guiado por pruebas y control de versiones.

### Objetivos Específicos

- Permitir el ingreso de la información del trabajador, incluyendo su sueldo básico.
- Calcular automáticamente las bonificaciones correspondientes al trabajador, incluyendo las bonificaciones por horas extras, movilidad y suplementarias.
- Calcular automáticamente los descuentos correspondientes al trabajador, incluyendo los descuentos por tardanzas y faltas.
- Mantener un registro de los recibos de cada trabajador, registrando los descuentos y su sueldo neto.
- Proporcionar una interfaz (programa) para que los administradores puedan registrar trabajadores, sus horas trabajadas, tardanzas y faltas, y revisar el historial de sueldos e imprimir boletas de pago.

## ÍTEM 1

__Lista de historias de usuario (product backlog priorizada).__

| __Prioridad__  | __Identificador__  | __Nombre (alias)__  | __Descripción__  | __Puntos de Historia (Horas ideales)__  | __Responsable__  |
|:----: |:-------- |:--------------------- |:------------------------|:----: |:-----------------|
| 1 |HYST01 | Login de empleador para acceder al software de administración. | Como empleador, deseo loguearme con una cuenta para empleador de tal manera qué pueda acceder al software y administrar las configuraciones. | 2 | Cordova Poma |
| 2 |HYST02 | Ingresar nombre y sueldo básico para calcular salario. | Como empleador, quiero ingresar el nombre y sueldo básico del trabajador para calcular su salario. | 2 | Cordova Poma |
| 3 |HYST03 | Ingresar días trabajados para calcular el sueldo total. | Como empleador, quiero ingresar la cantidad de días trabajados por el empleado para calcular el sueldo total. | 3 | Cordova Poma |
| 4 |HYST04 | Ingresar horas extras para la bonificación correspondiente. | Como empleador, quiero ingresar la cantidad de horas extras trabajadas por el empleado para agregar la bonificación correspondiente. | 3 | Cordova Poma |
| 5 |HYST05 | Ingresar tardanzas y faltas para descontar del sueldo. | Como empleador, quiero poder ingresar la cantidad de tardanzas y faltas del empleado para descontarlas de su sueldo. | 2 | Hilario Castro |
| 6 |HYST06 | Calcular automáticamente descuentos por tardanzas y faltas. | Como empleador, quiero que el programa calcule automáticamente el total de descuentos correspondientes a las tardanzas y faltas del empleado. | 2 | Hilario Castro |
| 7 |HYST07 | Calcular automáticamente el sueldo neto del empleado. | Como empleador, quiero que el programa calcule automáticamente el sueldo neto del empleado restando los descuentos del sueldo total. | 3 | Hilario Castro |
| 8 |HYST08 | Ingresa las fechas de inicio y fin del período de pago. | Como empleador, quiero poder ingresar la fecha de inicio y fin del período de pago para calcular el sueldo del empleado durante ese período. | 2 | Hilario Castro |
| 9 |HYST09 | Calcular automáticamente el sueldo promedio en horas extras. | Como empleador, quiero que el programa calcule automáticamente el sueldo promedio del empleado si ha trabajado horas extras. | 3 | Ingaroca Maldonado |
| 10 |HYST10 | Selección múltiple de trabajadores para aplicar cambios en grupo. | Como empleador, quiero seleccionar a los trabajadores para poder aplicar algunos cambios en grupo. | 3 | Ingaroca Maldonado |
| 11 |HYST11 | Calcular automáticamente las bonificaciones correspondientes al empleado. | Como empleador, quiero que el programa calcule automáticamente el total de bonificaciones correspondientes al empleado, incluyendo las bonificaciones adicionales que he agregado. | 2 | Ingaroca Maldonado |
| 12 |HYST12 | Alerta si el sueldo neto es menor al salario mínimo legal. | Como empleador, quiero que el programa muestre una alerta si el sueldo neto del empleado es menor que el salario mínimo legal para asegurarme de que estoy cumpliendo con las leyes laborales. | 2 | Ingaroca Maldonado |
| 13 |HYST13 | Imprimir o exportar reporte de sueldos en diferentes formatos. | Como empleador, quiero poder imprimir o exportar el reporte de sueldos en diferentes formatos, como PDF o Excel. | 3 | Osorio Alanya |
| 14 |HYST14 | Login de empleado para revisar cuenta y pagos. | Como empleado, deseo loguearme con una cuenta para empleado de tal manera qué pueda acceder al software y revisar mi cuenta, donde se especifica mis pagos y otros aspectos. | 2 | Osorio Alanya |
| 15 |HYST15 | Ver sueldo bruto, bonificaciones, descuentos y sueldo neto en reporte de sueldos. | Como empleado, quiero poder ver mi sueldo bruto, bonificaciones, descuentos y sueldo neto en el reporte de sueldos para verificar que se me haya pagado correctamente. | 3 | Osorio Alanya |
| 16 |HYST16 | Ver horas trabajadas, extras, tardanzas y faltas en reporte de sueldos. | Como empleado, quiero poder ver las horas trabajadas, las horas extras y las tardanzas y faltas en el reporte de sueldos para asegurarme de que se hayan registrado correctamente. | 2 | Osorio Alanya |
| 17 |HYST17 | Solicitar revisión de sueldo si se cree que no corresponde. | Como empleado, quiero poder solicitar una revisión de mi sueldo si creo que se me ha pagado menos de lo que corresponde según las horas trabajadas y las bonificaciones correspondientes. | 3 | Rosales Tapia |
| 18 |HYST18 | Ver historial de pagos anteriores. | Como empleado, quiero poder ver mi historial de pagos para verificar que se me haya pagado correctamente en períodos anteriores. | 2 | Rosales Tapia |
| 19 |HYST19 | Solicitar el adelanto de sueldo si se necesita. | Como empleado, quiero poder solicitar una reunión con el jefe de RR.HH, el que se encargará de poder brindar un adelanto de sueldo si necesito dinero antes de la fecha de pago habitual. | 3 | Rosales Tapia |
| 20 |HYST20 | Solicitar corrección en cálculo de sueldo. | Como empleado, quiero poder solicitar una corrección en el cálculo del sueldo si encuentro algún error en las horas trabajadas, las bonificaciones o los descuentos. | 3 | Rosales Tapia |
| 21 |HYST21 | Obtener historial de pagos mensualmente como gerente. | Como gerente, quiero obtener un historial de pagos de los empleados mensualmente, para tener un registro de historial de pagos. | 2 | Zapata Medina |
| 22 |HYST22 | Validar datos para evitar errores. | Como gerente, quiero validar los datos, para que no exista ningún dato suelto ni campos vacíos. | 1 | Zapata Medina |
| 23 |HYST23 | Visualizar lista de trabajadores para administrar y controlar. | Como gerente, quiero visualizar una lista de todos los trabajadores, para poder administrar, seleccionar y realizar un control. | 2 | Zapata Medina |
| 24 |HYST24 | Ver historial de pagos de cada trabajador como gerente. | Como gerente, quiero visualizar el historial de pagos de cada uno de mis trabajadores. | 3 | Zapata Medina |

## Item 2

![Modelo conceptual del proyecto](/others/img/diagrama_uml.png)
