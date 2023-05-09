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

## __ÍTEM 1 - Product Backlog__ 📑

__Lista de historias de usuario (product backlog priorizada).__

| __Prioridad__  | __Identificador__  | __Nombre (alias)__  | __Descripción__  | __Puntos de Historia (Días ideales)__  | __Responsable__  |
|:----: |:-------- |:--------------------- |:------------------------|:----: |:-----------------|
| 1 |HYST01 | Login de empleador para acceder al software de administración | Como empleador, deseo loguearme con una cuenta para empleador de tal manera qué pueda acceder al software y administrar las configuraciones. | 2 | Cordova Poma |
| 2 |HYST02 | Registro de nuevo trabajador | Como empleador, deseo registrar a un empleado incluido su sueldo base, para actualizar el registro en la base de datos. | 1 | Ingaroca Maldonado |
| 3 |HYST03 | Editar trabajador | Como empleador, deseo editar los datos de un trabajador, para actualizar su registro en  la base de datos. | 2 | Hilario Castro |
| 4 |HYST04 | Eliminar trabajador | Como empleador, deseo eliminar a un trabajador, para actualizar la lista de trabajadores. | 1 | Zapata Medina |
| 5 |HYST05 | Buscar trabajador por DNI | Como empleador, quiero poder buscar a un Trabajador, para poder seleccionarlo. | 2 | Rosales Tapia |
| 6 |HYST06 | Seleccionar trabajador | Como empleador, quiero poder seleccionar un Trabajador, para poder administrar y registrar sus datos respecto al sueldo. | 1 | Osorio Alanya |
| 7 |HYST07 | Buscar trabajador por apellidos y nombres | Como empleador, quiero poder buscar a un trabajador por su nombre, para poder seleccionarlo. | 1 | Ingaroca Maldonado |
| 8 |HYST08 | Listar trabajadores | Como empleador, quiero obtener una lista de los trabajadores registrados y sus datos para poder utilizarlos en otro proceso. | 2 | Hilario Castro |
| 9 |HYST09 | Ingresar horas extras | Como empleador, quiero ingresar la cantidad de horas extras trabajadas por el trabajador para el cálculo de la bonificación correspondiente. | 1 | Zapata Medina |
| 10 |HYST10 | Marcar bonificación por movilidad | Como empleador, quiero poder marcar si a un trabajador le corresponde la bonificación por movilidad, para que se incremente en su sueldo. | 1 | Rosales Tapia |
| 11 |HYST11 | Marcar bonificación suplementaria | Como empleador, quiero poder marcar si a un trabajador le corresponde la bonificación suplementaria, para que se incremente en su sueldo. | 1 | Osorio Alanya |
| 12 |HYST12 | Ingresar días de falta | Como empleador, quiero ingresar la cantidad de días que un trabajador faltó, para el cálculo del respectivo descuento. | 1 | Ingaroca Maldonado |
| 13 |HYST13 | Ingresar minutos de tardanza | Como empleador, quiero ingresar la cantidad de minutos que un trabajador tiene de tardanza, para el cálculo del respectivo descuento. | 1 | Osorio Alanya |
| 14 |HYST14 | Calcular automáticamente descuento neto | Como empleador, quiero que el programa calcule automáticamente el valor neto de descuento correspondiente a las tardanzas y faltas del trabajador, para su registro. | 2 | Cordova Poma |
| 15 |HYST15 | Calcular automáticamente bonificación neta | Como empleador, quiero que el programa calcule automáticamente el valor neto de bonificación, para su registro. | 2 | Hilario Castro |
| 16 |HYST16 | Calcular automáticamente el sueldo neto | Como empleador, quiero que el programa calcule automáticamente el sueldo neto del empleado, para poder realizar su pago. | 2 | Ingaroca Maldonado |
| 17 |HYST17 | Visualizar boletas de trabajador | Como empleador, quiero visualizar las boletas de pago correspondiente a un trabajador, para su selección. | 1 | Rosales Tapia |
| 18 |HYST18 | Imprimir boleta de pago | Como empleador, quiero poder imprimir una boleta de pago del trabajador, para poder utilizarlo en otro proceso. | 3 | Cordova Poma |
| 19 |HYST19 | Listar pagos por mes | Como empleador, quiero ver una lista de pagos a realizar por mes, para poder imprimirlo. | 1 | Hilario Castro |
| 20 |HYST20 | Imprimir lista de pagos del mes | Como empleador, quiero poder imprimir la lista de pagos de un mes, para poder llevar un registro físico. | 3 | Zapata Medina |
| 21 |HYST21 | Visualizar reporte económico general del mes | Como empleador, quiero visualizar un reporte económico general del mes, para poder redactar un informe. | 4 | Cordova Poma |
| 22 |HYST22 | Enviar boleta de pago por correo | Como empleador, quiero poder enviar una boleta de pago al trabajador, para su notificación inmediata. | 3 | Cordova Poma |
| 23 |HYST23 | Listar asistencia perfecta por mes | Como empleador, quiero ver una lista de los trabajadores que tuvieron asistencia perfecta en un mes, para poder imprimirlo. | 2 | Rosales Tapia |
| 24 |HYST24 | Imprimir lista de asistencia perfecta del mes | Como empleador, quiero imprimir la lista de los trabajadores que tuvieron asistencia perfecta en un mes, para poder utilizarlo en otro proceso. | 3 | Zapata Medina |
|  |  |  | __Total de puntos__ | __43__ |  |

### __Revisión__

| Criterio | Comentario | Realizado por | Solucionado |
| :------- | :-----------------: | :------- | :--------:|
| __Forma__ | Conforme | Rosales Tapia | ✔️ |
| __Completo__ | Conforme | Cordova Poma | ✔️ |
| __Consistente__ | Conforme | Ingaroca Maldonado | ✔️ |
| __Independiente__ | Conforme | Zapata Medina | ✔️ |

## __Ítem 2 - Modelo Conceptual__ 📟

![Modelo conceptual del proyecto][Modelo Conceptual]

### Glosario de Conceptos

| Concepto | Descripción | Observaciones |
| -------- | ----------- | ------------- |
| Empleador |  |  |
| Bonificación |  |  |
| Descuento |  |  |
| BoletaDePago |  |  |
| Empleador-BoletaDePago |  |  |
| Descuento-BoletaDePago |  |  |
| Bonificacion-BoletaDePago |  |  |
| Trabajador-BoletaDePago |  |  |

[Modelo Conceptual]: /others/img/modelo_Conceptual.PNG