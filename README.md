# Proyecto de Fin de Curso: "Salary Horizon 1.0"

Este proyecto está desarrollado por estudiantes de la _Universidad Continental_, propuesto en el curso de ___Construcción de Software___ con la guía del docente [Daniel Gamarra Moreno](https://estudiantesavp.ucontinental.edu.pe/user/profile.php?id=9474), a quién agradecemos encarecidamente por su esfuerzo, apoyo y dedicación por brindarnos sus conocimientos.

### Equipo de Desarrollo

| __Integrante__  | __Apellidos y Nombres__  | __Rol__ |
|:-------------: |:---------------| :-----------------: |
| 1         | Cordova Poma Jhordan Sax | Scrum Master |
| 2         | Hilario Castro Kenss Lin Kadú | Developer |
| 3         | Ingaroca Maldonado Jhim Sebastian | Product Owner |
| 4         | Osorio Alanya Gianfranco          | Developer |
| 5         | Rosales Tapia Brad Jhomers        | Developer |
| 6         | Zapata Medina Juan Diego | Developer |

## Descripción del proyecto
La empresa Horizonte ha decidido implementar un sistema automatizado para el cálculo de los sueldos de sus empleados. Se quiere simplificar el proceso de cálculo y asegurarse de que los sueldos se calculen correctamente, evitando errores humanos y reduciendo el tiempo y los costos asociados con el cálculo manual de los sueldos.

### Consigna
#### El trabajador percibe las siguientes bonificaciones:
1. Por cada hora extra se le paga 50% más que una hora normal.
1. Bonificación por movilidad igual a 1000.
1. Bonificación suplementaria igual al 3% del sueldo básico (sueldo).
1. La bonificación total es la suma de todas las bonificaciones que percibe.

#### Asimismo, el trabajador está sujeto a los siguientes descuentos:
1. Las tardanzas y faltas se descuentan con respecto a remuneración computable. La remuneración computable es igual al sueldo básico más la suma de todas las bonificaciones excepto la bonificación por horas extras.
1. El total de descuentos se obtiene sumando todos los descuentos.

## Objetivos

### Objetivo Principal
- Desarrollar un software que permita a la empresa Horizonte calcular los sueldos de sus empleados de manera rápida, precisa y eficiente. Aplicando el desarrollo guiado por pruebas y control de versiones.
 

### Objetivos Específicos
- Permitir el ingreso de la información del empleado, incluyendo el sueldo básico y las horas trabajadas, en un formato fácil de usar.
- Calcular automáticamente las bonificaciones correspondientes al empleado, incluyendo las bonificaciones por horas extras, movilidad y suplementarias.
- Calcular automáticamente los descuentos correspondientes al empleado, incluyendo los descuentos por tardanzas y faltas.
- Presentar un reporte de sueldos que muestre el sueldo bruto, las bonificaciones, los descuentos y el sueldo neto de cada empleado.
- Permitir al empleador agregar bonificaciones adicionales o aplicar descuentos adicionales según sea necesario.
- Proporcionar una interfaz (programa) para que los empleados puedan ingresar sus horas trabajadas, tardanzas y faltas, y revisar su historial de sueldos.

## ÍTEM UNO

Lista de historias de usuario (product backlog priorizada).

| __Prioridad__  | __Identificador__  | __Nombre (alias)__  | __Descripción__  | __Puntos de Historia (Horas ideales)__  | __Responsable__  |
|:----: |:-------- |:--------------------- |:------------------------|:----: |:-----------------|
| null |HYST01 | Ingresar el nombre del trabajador | Como gerente, quiero colocar el nombre del trabajador para registrar a quien pagar el sueldo. | 2 | null |
| null |HYST02 | Ingresar sueldo básico | Como gerente, quiero ingresar el sueldo básico de cada trabajador para la consideración de su pago | 2 | null |
| null |HYST03 | Ingresar días que no asistió | Como gerente, quiero colocar los días que faltó un trabajador para realizar el debido proceso de descuento | 3 | null |
| null |HYST04 | Ingresar días que asistió tarde | Como gerente, quiero colocar la cantidad de días que el trabajador llegó tarde para el debido proceso de descuento.  | 3 | null |
| null |HYST05 | Ingresar horas extras | Como gerente, quiero colocar la cantidad de minutos de tardanza para realizar su descuento. | null | null |
| null |HYST06 | Imprimir boleta de pago | Como gerente, quiero imprimir la boleta de pago de los trabajadores para archivar | null | null |
| null |HYST07 | Calcular bonificación | Como gerente, quiero calcular la bonificación del trabajador en caso haya ingresado los datos para hallar bonificación. | null | null |
| null |HYST08 | Calcular descuento | Como gerente, quiero calcular el descuento del trabajador en caso haya ingresado los datos para hallar el descuento. | null | null |
| null |HYST09 | Exportar historial de pagos del mes | Como gerente, quiero obtener un historial de pagos de los empleados mensualmente, para tener un registro de historial de pagos. | null | null |
| null |HYST10 | Validación de datos ingresados | Como gerente,quiero validar los datos, para que no exista ningún dato suelto ni campos vacíos. | null | null |
| null |HYST11 | Mostrar trabajadores | Como gerente, quiero visualizar una lista de todos los trabajadores, para poder administrar, seleccionar y realizar un control. | null | null |
| null |HYST12 | Seleccionar trabajadores | Como gerente, quiero seleccionar a los trabajadores para poder aplicar algunos cambios en grupo. | null | null |
| null |HYST13 | Ver el historial de pagos de trabajador | Como gerente, quiero visualizar el historial de pagos de cada uno de mis trabajadores | null | null |
| null |HYST14 | Calculo de bonificación suplementaria | Como gerente, quiero calcular y modificar los bonos correspondientes a mis trabajadores | null | null |
| null |HYST15 | Cálculo de salario neto | Como gerente, quiero calcular y modificar el salario de mis trabajadores | null | null |
| null |HYST16 | Actualizar tardanza | Como gerente, quiero ver los minutos de tardanzas de mis trabajadores para poder realizar cambios en su sueldo | null | null |
| null |HYST17 | Pago por horas extras | Como gerente deseo calcular calcular él pago por horas extras  para agregar él bono al sueldo del trabajador  | null | null |
| null |HYST18 | Movilidad | Como gerente deseo generar la siguiente constante para poder realizar los cálculos posteriores. |null | null |
| null |HYST19 | Bonificación suplementarias | Como gerente deseo calcular las bonificaciones suplementarias para aplicarlos a los sueldos de los trabajadores. | null | null |
| null |HYST20 | Hallar emuneración computable | Como gerente deseo calcular el la remuneración computable en base al sueldo básico más las bonificaciones para aplicarlo en el sueldo del trabajador. | null | null |
| null |HYST21 | Calcular descuento por tardanza | Como gerente deseo calcular el descuento por tardanza para aplicarlo en el sueldo del trabajador. | null | null |
| null |HYST22 | Calcular descuento porfaltas | Como gerente deseo calcular el descuento por faltas para aplicarlo en el sueldo del trabajador | null | null |
| null |HYST23 | Hallar emuneracion minima | Como gerente deseo calcular el la remuneración mínima en base al sueldo básico más las bonificaciones para aplicarlo en el sueldo del trabajador. | null | null |
| null |HYST24 | Hallar descuentos Totales | Como gerente deseo calcular los descuentos totales para aplicarlo en el sueldo del trabajador. | null | null |
