# Proyecto de Fin de Curso: "Salary Horizon 1.0"

 ![Badge en Desarollo](https://img.shields.io/badge/STATUS-EN%20DESAROLLO-green)

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
| 1 | [HYST01](#hyst01) | Login de empleador para acceder al software de administración | Como empleador, deseo loguearme con una cuenta para empleador de tal manera qué pueda acceder al software y administrar las configuraciones. | 2 | Cordova Poma |
| 2 | [HYST02](#hyst02) | Registro de nuevo trabajador | Como empleador, deseo registrar a un trabajador, incluido su sueldo base, para actualizar el registro en la base de datos. | 1 | Ingaroca Maldonado |
| 3 | HYST03 | Editar trabajador | Como empleador, deseo editar los datos de un trabajador, para actualizar su registro en  la base de datos. | 2 | Hilario Castro |
| 4 | HYST04 | Eliminar trabajador | Como empleador, deseo eliminar a un trabajador, para actualizar la lista de trabajadores. | 1 | Zapata Medina |
| 5 | HYST05 | Buscar trabajador por DNI | Como empleador, quiero poder buscar a un Trabajador, para poder seleccionarlo. | 2 | Rosales Tapia |
| 6 | HYST06 | Seleccionar trabajador | Como empleador, quiero poder seleccionar un Trabajador, para poder administrar y registrar sus datos respecto al sueldo. | 1 | Osorio Alanya |
| 7 | HYST07 | Buscar trabajador por apellidos y nombres | Como empleador, quiero poder buscar a un trabajador por su nombre, para poder seleccionarlo. | 1 | Ingaroca Maldonado |
| 8 | HYST08 | Listar trabajadores | Como empleador, quiero obtener una lista de los trabajadores registrados y sus datos para poder utilizarlos en otro proceso. | 2 | Hilario Castro |
| 9 | HYST09 | Ingresar horas extras | Como empleador, quiero ingresar la cantidad de horas extras trabajadas por el trabajador para el cálculo de la bonificación correspondiente. | 1 | Zapata Medina |
| 10 | HYST10 | Marcar bonificación por movilidad | Como empleador, quiero poder marcar si a un trabajador le corresponde la bonificación por movilidad, para que se incremente en su sueldo. | 1 | Rosales Tapia |
| 11 | HYST11 | Marcar bonificación suplementaria | Como empleador, quiero poder marcar si a un trabajador le corresponde la bonificación suplementaria, para que se incremente en su sueldo. | 1 | Osorio Alanya |
| 12 | HYST12 | Ingresar días de falta | Como empleador, quiero ingresar la cantidad de días que un trabajador faltó, para el cálculo del respectivo descuento. | 1 | Ingaroca Maldonado |
| 13 | HYST13 | Ingresar minutos de tardanza | Como empleador, quiero ingresar la cantidad de minutos que un trabajador tiene de tardanza, para el cálculo del respectivo descuento. | 1 | Osorio Alanya |
| 14 | HYST14 | Calcular automáticamente descuento neto | Como empleador, quiero que el programa calcule automáticamente el valor neto de descuento correspondiente a las tardanzas y faltas del trabajador, para su registro. | 2 | Cordova Poma |
| 15 | HYST15 | Calcular automáticamente bonificación neta | Como empleador, quiero que el programa calcule automáticamente el valor neto de bonificación, para su registro. | 2 | Hilario Castro |
| 16 | HYST16 | Calcular automáticamente el sueldo neto | Como empleador, quiero que el programa calcule automáticamente el sueldo neto del trabajador, para poder realizar su pago. | 2 | Ingaroca Maldonado |
| 17 | HYST17 | Visualizar boletas de trabajador | Como empleador, quiero visualizar las boletas de pago correspondiente a un trabajador, para su selección. | 1 | Rosales Tapia |
| 18 | HYST18 | Imprimir boleta de pago | Como empleador, quiero poder imprimir una boleta de pago del trabajador, para poder utilizarlo en otro proceso. | 3 | Cordova Poma |
| 19 | HYST19 | Listar pagos por mes | Como empleador, quiero ver una lista de pagos a realizar por mes, para poder imprimirlo. | 1 | Hilario Castro |
| 20 | HYST20 | Imprimir lista de pagos del mes | Como empleador, quiero poder imprimir la lista de pagos de un mes, para poder llevar un registro físico. | 3 | Zapata Medina |
| 21 | HYST21 | Visualizar reporte económico general del mes | Como empleador, quiero visualizar un reporte económico general del mes, para poder redactar un informe. | 4 | Cordova Poma |
| 22 | HYST22 | Enviar boleta de pago por correo | Como empleador, quiero poder enviar una boleta de pago al trabajador, para su notificación inmediata. | 3 | Cordova Poma |
| 23 | HYST23 | Listar asistencia perfecta por mes | Como empleador, quiero ver una lista de los trabajadores que tuvieron asistencia perfecta en un mes, para poder imprimirlo. | 2 | Rosales Tapia |
| 24 | HYST24 | Imprimir lista de asistencia perfecta del mes | Como empleador, quiero imprimir la lista de los trabajadores que tuvieron asistencia perfecta en un mes, para poder utilizarlo en otro proceso. | 3 | Zapata Medina |
|  |  |  | __Total de puntos__ | __43__ |  |

### __Revisión__

| Criterio | Comentario | Realizado por | Solucionado |
| :------- | :-----------------: | :------- | :--------:|
| __Forma__ | _Conforme_ | _Rosales Tapia_ | ✔️ |
| __Completo__ | _Conforme_ | _Cordova Poma_ | ✔️ |
| __Consistente__ | _Conforme_ | _Ingaroca Maldonado_ | ✔️ |
| __Independiente__ | _Conforme_ | _Zapata Medina_ | ✔️ |

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

## __Ítem 3 - Velocidad del Equipo de desarrollo__ 💻

Se está considerando seis desarrolladores, de los cuales se dedica el 15% del tiempo a generar código, con la duración de un sprint de 10 días (5 días por semana).

```text
6 * 10 * 0.15 = 9 puntos de historia
```

El equipo de desarrollo obtuvo una velocidad de 9 puntos de historia por __Sprint__. Por lo tanto la cantidad de puntos de historia por cada Sprint no deberían superar este indicador.

## __Ítem 4 - Sprint Backlog__ 📇

### __Sprint 1__

| __Prioridad__  | __Identificador__  | __Nombre (alias)__  | __Descripción__  | __Puntos de Historia (Días ideales)__  | __Responsable__  |
|:----: |:-------- |:--------------------- |:------------------------|:----: |:-----------------|
| 1 | [HYST01](#hyst01) | Login de empleador para acceder al software de administración | Como empleador, deseo loguearme con una cuenta para empleador de tal manera qué pueda acceder al software y administrar las configuraciones. | 2 | Cordova Poma |
| 2 | [HYST02](#hyst02) | Registro de nuevo trabajador | Como empleador, deseo registrar a un trabajador incluido su sueldo base, para actualizar el registro en la base de datos. | 1 | Ingaroca Maldonado |
| 3 | HYST03 | Editar trabajador | Como empleador, deseo editar los datos de un trabajador, para actualizar su registro en  la base de datos. | 2 | Hilario Castro |
| 4 | HYST04 | Eliminar trabajador | Como empleador, deseo eliminar a un trabajador, para actualizar la lista de trabajadores. | 1 | Zapata Medina |
| 5 | HYST05 | Buscar trabajador por DNI | Como empleador, quiero poder buscar a un Trabajador, para poder seleccionarlo. | 2 | Rosales Tapia |
| 6 | HYST06 | Seleccionar trabajador | Como empleador, quiero poder seleccionar un Trabajador, para poder administrar y registrar sus datos respecto al sueldo. | 1 | Osorio Alanya |
|  |  |  | __Total de puntos__ | __9__ |  |

## __Ítem 5 - Historias de Usuario__ 📜

Se muestran las historias de usuario de una forma más detallada.

----

### __HYST01__

| Identificador | HYST01 |
| :---------- | :-------- |
| __Nombre (alias)__ | Login de empleador para acceder al software de administración. |
| __Descripción__ | Como empleador, deseo loguearme con una cuenta para empleador de tal manera qué pueda acceder al software y administrar las configuraciones. |
| __Puntos de historia (Horas Ideaales)__ | 2 |
| __Criterios de aceptación__ | Al abrir el software, se presentará una pantalla con espacios en blanco donde se solicitará el ID y contraseña del usuario.  |
|| Cuando se completen los espacios en blanco, el usuario deberá hacer click en el botón “Login” para acceder a otra ventana. |
|| Si el usuario se equivocó en algún espacio en blanco, el usuario podrá dar click en el botón “Cancel” para volver a escribir sus datos. |
|| Si el usuario se olvidó su contraseña, podrá hacer click en “Forgot Password” para recuperar su contraseña. |

#### __Revisión 01__

| Criterio | Comentario | Realizado por | Solucionado |
| :-------- | :--------- | :----------| :--------:|
| __Completo__ | Aceptado | Osorio Alanya | ✔️ |
| __Consistente__ | Aceptado | Osorio Alanya | ✔️ |
| __Negocible__ | Aceptado | Osorio Alanya | ✔️ |
| __Valiosa__ | Aceptado | Osorio Alanya | ✔️ |
| __Estimable__ | Aceptado | Osorio Alanya | ✔️ |
| __Pequeña__ | Aceptado | Osorio Alanya | ✔️ |
| __Comprobable__ | Aceptado | Osorio Alanya | ✔️ |

#### __Wireframe 01__

![Login del empleador|80][Login]

----

### __HYST02__

| Identificador | HYST02 |
| :---------- | :-------- |
| __Nombre (alias)__ | Registro de nuevo empleado |
| __Descripción__ | Como empleador, deseo registrar a un trabajador, para actualizar el registro en la base de datos. |
| __Puntos de historia (Horas Ideaales)__ | 1 |
| __Criterios de aceptación__ | Al seleccionar la opción de "Registrar Trabajador", se debe presentar al usuario una pantalla con diferentes espacios en blanco en donde solicitan información del empleado.  |
|| Cuando él usuario termine de completar los espacios en blanco, asegurarse de guardar él nuevo registro del trabajador con él botón “agregar”. |
|| Si el usuario decide cancelar él registro  del trabajador, no se deben guardar los cambios en la base de datos y se debe borrar todos los espacios en blanco anteriormente rellenados . |
|| Si el nuevo trabajador que quiere registrarse ingresa datos erróneos, o se salta alguna casilla no podrá realizar el registro y saltará una notificación que comunique la revisión de que  los datos sean correctos. |

#### __Revisión 02__

| Criterio | Comentario | Realizado por | Solucionado |
| :-------- | :--------- | :----------| :--------:|
| __Completo__ | La historia de usuario “Registro de nuevo empleado” describe todas las funcionalidades necesarias para el registro de un nuevo empleado. | Rosales Tapia | ✔️ |
| __Consistente__ | El historial del usuario es consistente con el propósito general y los requisitos del proyecto. | Rosales Tapia | ✔️ |
| __Negocible__ | La historia de usuario es flexible y se puede ajustar en el proceso de desarrollo para adaptarse a los cambios en los requisitos para el proyecto. | Rosales Tapia | ✔️ |
| __Valiosa__ | La historia de usuario trabajada da un valor real para los usuarios finales. | Rosales Tapia | ✔️ |
| __Estimable__ | La historia de usuario se puede estimar con gran precisión  en términos de tiempo y esfuerzo que son necesarios para completarlo. | Rosales Tapia | ✔️ |
| __Pequeña__ | La historia de usuario es lo suficientemente pequeña como para que pueda ser completada en un ciclo de funcionamiento. | Rosales Tapia | ✔️ |
| __Comprobable__ | La historia de usuario es  sumamente específica. | Rosales Tapia | ✔️ |

<!-- #### __Wireframe 02__

![][] -->

----

### __HYST03__

| Identificador | HYST03 |
| :---------- | :-------- |
| __Nombre (alias)__ | Editar Empleado |
| __Descripción__ | Como empleador, deseo editar los datos de un trabajador, para actualizar su registro en  la base de datos. |
| __Puntos de historia (Horas Ideaales)__ | 2 |
| __Criterios de aceptación__ | Al seleccionar la opción de "Editar Trabajador", se debe presentar al empleador una pantalla con los datos actuales del trabajador.  |
|| El empleador debe poder modificar cualquier campo de los datos del trabajador. |
|| Si el empleador decide cancelar la edición del trabajador, no se deben guardar los cambios en la base de datos y se debe volver a la pantalla anterior sin realizar ninguna acción. |
|| Si el empleador intenta guardar cambios con datos inválidos, se debe mostrar un mensaje de error indicando cuál campo tiene un valor no válido. |

#### __Revisión 03__

| Criterio | Comentario | Realizado por | Solucionado |
| :-------- | :--------- | :----------| :--------:|
| __Completo__ | Tiene una descripción detallada de lo que se espera de la funcionalidad y los datos específicos que se necesitan actualizar. | HIlario Castro | ✔️ |
| __Consistente__ | Es coherente con los objetivos generales del sistema y está alineada con las necesidades de los usuarios. | HIlario Castro | ✔️ |
| __Negocible__ | Hay cierto margen para ajustar los detalles de la implementación, siempre y cuando se mantenga el objetivo general y la funcionalidad básica. | HIlario Castro | ✔️ |
| __Valiosa__ | Se considera valiosa, ya que permite mantener actualizada la información de los trabajadores de manera efectiva.   | HIlario Castro | ✔️ |
| __Estimable__ | La historia de usuario es fácilmente estimable, ya que involucra una tarea clara y definida. | HIlario Castro | ✔️ |
| __Pequeña__ | Es una tarea relativamente pequeña y manejable. | HIlario Castro | ✔️ |
| __Comprobable__ | Es posible probar la funcionalidad y validar si se cumplen todos los requisitos. | HIlario Castro | ✔️ |

<!-- #### __Wireframe 03__

![][] -->

----
[Modelo Conceptual]: /others/img/modelo_Conceptual.PNG
[Login]: /others/img/login.jpg