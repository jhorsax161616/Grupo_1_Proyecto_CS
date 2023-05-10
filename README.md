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
| 3 | [HYST03](#hyst03) | Editar trabajador | Como empleador, deseo editar los datos de un trabajador, para actualizar su registro en  la base de datos. | 2 | Hilario Castro |
| 4 | [HYST04](#hyst04) | Eliminar trabajador | Como empleador, deseo eliminar a un trabajador, para actualizar la lista de trabajadores. | 1 | Zapata Medina |
| 5 | [HYST05](#hyst05) | Buscar trabajador por DNI | Como empleador, quiero poder buscar a un Trabajador, para poder seleccionarlo. | 2 | Rosales Tapia |
| 6 | [HYST06](#hyst06) | Seleccionar trabajador | Como empleador, quiero poder seleccionar un Trabajador, para poder administrar y registrar sus datos respecto al sueldo. | 1 | Osorio Alanya |
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
| -------- | ----------- | -------------: |
| __Empleador__ | Es una tabla, donde se almacenarán los datos del empleador. Es quien está a cargo de gestionar los datos de los trabajadores. | Ninguna |
| __Bonificación__ | Es una tabla donde se guardan los datos sobre bonificaciones del trabajador. El cual obtendrá los datos de pagos por horas extras, bonificaciones por movilidad y bonificaciones suplementarias, todo para su respectivo cálculo de sueldo. | Ninguna |
| __Descuento__ | Es una tabla donde se guardan los datos sobre los descuentos del trabajador. Se ingresan los datos de días faltantes y la tardanza en minutos, para luego proceder con su cálculo.  | Ninguna |
| __BoletaDePago__ | Es una tabla detalle, donde todas las demás tablas están vinculadas a esta para poder procesar la boleta de pago. En esta parte se dará a conocer al Trabajador, la cantidad de bonificación, el descuento, y el sueldo total. | Ninguna |
| __Trabajador__ | Es una tabla encargada de almacenar los datos del Trabajador, en el cual se incluyen los datos importantes del trabajador. | Ninguna |
| __Empleador-BoletaDePago__ | En esta relación, la boleta de pago se relaciona de a uno con el Empleador, ya que el empleador puede hacer muchas boletas. | Ninguna |
| __Descuento-BoletaDePago__ | En esta relación, la boleta de pago se relaciona de uno a uno con Descuento, ya que el descuento para el cálculo se usará un ID donde se almacenarán los datos. | Ninguna |
| __Bonificacion-BoletaDePago__ | En esta relación, la boleta de pago se relaciona de uno a uno con la bonificación, ya que la bonificación tendrá un ID correspondiente por su calcio realizado, y la boleta de pago solo se calcula por cada cálculo que ingrese el Empleador | Ninguna |
| __Trabajador-BoletaDePago__ | En esta relación, la boleta de pago se relaciona de muchos a uno con trabajador, ya que una boleta de pago solo puede contener a un Trabajador al ser efectuada. | Ninguna |

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
| 3 | [HYST03](#hyst03) | Editar trabajador | Como empleador, deseo editar los datos de un trabajador, para actualizar su registro en  la base de datos. | 2 | Hilario Castro |
| 4 | [HYST04](#hyst04) | Eliminar trabajador | Como empleador, deseo eliminar a un trabajador, para actualizar la lista de trabajadores. | 1 | Zapata Medina |
| 5 | [HYST05](#hyst05) | Buscar trabajador por DNI | Como empleador, quiero poder buscar a un Trabajador, para poder seleccionarlo. | 2 | Rosales Tapia |
| 6 | [HYST06](#hyst06) | Seleccionar trabajador | Como empleador, quiero poder seleccionar un Trabajador, para poder administrar y registrar sus datos respecto al sueldo. | 1 | Osorio Alanya |
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
| __Criterios de aceptación__ | Al abrir el software, se presentará una pantalla con espacios en blanco donde se solicitará el ID y contraseña del empleador.  |
|| Cuando se completen los espacios en blanco, el empleador deberá hacer click en el botón “Login” para acceder a otra ventana. |
|| Si el empleador se equivocó en algún espacio en blanco, el empleador podrá dar click en el botón “Cancel” para volver a escribir sus datos. |
|| Si el empleador olvidó su contraseña, podrá hacer click en “Forgot Password” para recuperar su contraseña. |

#### __Revisión 01__

| Criterio | Comentario | Realizado por | Solucionado |
| :-------- | :--------- | :----------| :--------:|
| __Completo__ | _Aceptado_ | _Osorio Alanya_ | ✔️ |
| __Consistente__ | _Aceptado_ | _Osorio Alanya_ | ✔️ |
| __Negocible__ | _Aceptado_ | _Osorio Alanya_ | ✔️ |
| __Valiosa__ | _Aceptado_ | _Osorio Alanya_ | ✔️ |
| __Estimable__ | _Aceptado_ | _Osorio Alanya_ | ✔️ |
| __Pequeña__ | _Aceptado_ | _Osorio Alanya_ | ✔️ |
| __Comprobable__ | _Aceptado_ | _Osorio Alanya_ | ✔️ |

#### __Wireframe 01__

![Login del empleador|80][Login]

----

### __HYST02__

| Identificador | HYST02 |
| :---------- | :-------- |
| __Nombre (alias)__ | Registro de nuevo trabajador |
| __Descripción__ | Como empleador, deseo registrar a un trabajador, para actualizar el registro en la base de datos. |
| __Puntos de historia (Horas Ideaales)__ | 1 |
| __Criterios de aceptación__ | Al seleccionar la opción de "Registrar Trabajador", se debe presentar al empleador una pantalla con diferentes espacios en blanco en donde solicitan información del trabajador.  |
|| Cuando el empleador termine de completar los espacios en blanco, asegurarse de guardar el nuevo registro del trabajador con el botón “agregar”. |
|| Si el empleador decide cancelar el registro  del trabajador, no se deben guardar los cambios en la base de datos y se debe borrar todos los espacios en blanco anteriormente rellenados . |
|| Si el nuevo trabajador que quiere registrarse ingresa datos erróneos, o se salta alguna casilla no podrá realizar el registro y saltará una notificación que comunique la revisión de que  los datos sean correctos. |

#### __Revisión 02__

| Criterio | Comentario | Realizado por | Solucionado |
| :-------- | :--------- | :----------| :--------:|
| __Completo__ | _La historia de usuario “Registro de nuevo empleado” describe todas las funcionalidades necesarias para el registro de un nuevo empleado._ | _Rosales Tapia_ | ✔️ |
| __Consistente__ | _El historial del usuario es consistente con el propósito general y los requisitos del proyecto._ | _Rosales Tapia_ | ✔️ |
| __Negocible__ | _La historia de usuario es flexible y se puede ajustar en el proceso de desarrollo para adaptarse a los cambios en los requisitos para el proyecto._ | _Rosales Tapia_ | ✔️ |
| __Valiosa__ | _La historia de usuario trabajada da un valor real para los usuarios finales._ | _Rosales Tapia_ | ✔️ |
| __Estimable__ | _La historia de usuario se puede estimar con gran precisión  en términos de tiempo y esfuerzo que son necesarios para completarlo._ | _Rosales Tapia_ | ✔️ |
| __Pequeña__ | _La historia de usuario es lo suficientemente pequeña como para que pueda ser completada en un ciclo de funcionamiento._ | _Rosales Tapia_ | ✔️ |
| __Comprobable__ | _La historia de usuario es  sumamente específica._ | _Rosales Tapia_ | ✔️ |

#### __Wireframe 02__

![Registrar nuevo trabajador GUI][Registrar_Trabajador]

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
| __Completo__ | _Tiene una descripción detallada de lo que se espera de la funcionalidad y los datos específicos que se necesitan actualizar._ | _Hilario Castro_ | ✔️ |
| __Consistente__ | _Es coherente con los objetivos generales del sistema y está alineada con las necesidades de los usuarios._ | _Hilario Castro_ | ✔️ |
| __Negocible__ | _Hay cierto margen para ajustar los detalles de la implementación, siempre y cuando se mantenga el objetivo general y la funcionalidad básica._ | _Hilario Castro_ | ✔️ |
| __Valiosa__ | _Se considera valiosa, ya que permite mantener actualizada la información de los trabajadores de manera efectiva._   | _Hilario Castro_ | ✔️ |
| __Estimable__ | _La historia de usuario es fácilmente estimable, ya que involucra una tarea clara y definida._ | _Hilario Castro_ | ✔️ |
| __Pequeña__ | _Es una tarea relativamente pequeña y manejable._ | _Hilario Castro_ | ✔️ |
| __Comprobable__ | _Es posible probar la funcionalidad y validar si se cumplen todos los requisitos._ | _Hilario Castro_ | ✔️ |

<!-- #### __Wireframe 03__

![][] -->

----

### __HYST04__

| Identificador | HYST04 |
| :---------- | :-------- |
| __Nombre (alias)__ | Eliminar Trabajador |
| __Descripción__ | Como empleador, deseo eliminar a un trabajador, para actualizar la lista de trabajadores. |
| __Puntos de historia (Horas Ideaales)__ | 1 |
| __Criterios de aceptación__ | Si se decide eliminar a un trabajador, al momento de seleccionar “eliminar trabajador” se rellenará un registro donde se especifica la fecha, hora y el motivo por el cual se está llevando a cabo la eliminación del trabajador. |
|| Si se desea continuar con el proceso, al momento de seleccionar “continuar” saldra una notificacion en donde se requerirá la confirmación de seguridad en donde se mostrara dos opciones “1 continuar”  y “2 deshacer cambios”. |
|| Cuando se haya eliminado el trabajador también se eliminará de la base de datos de los trabajadores actuales. |
|| Para cuando se haya eliminado al trabajador, el sistema debe actualizar automáticamente cualquier registro relacionado con el trabajador que se eliminó. |

#### __Revisión 04__

| Criterio | Comentario | Realizado por | Solucionado |
| :-------- | :--------- | :----------| :--------:|
| __Completo__ | _Se describen todas las funcionalidades necesarias para eliminar un trabajador._ | _Rosales Tapia_ | ✔️ |
| __Consistente__ | _La historia de usuario es coherente con los objetivos y requisitos generales del proyecto._ | _Rosales Tapia_ | ✔️ |
| __Negocible__ | _La historia de usuario es flexible y se puede ajustar durante el proceso de desarrollo para adaptarse a los cambios en los requisitos del proyecto._  | _Rosales Tapia_ | ✔️ |
| __Valiosa__ | _La funcionalidad de eliminar trabajadores es crucial para el correcto mantenimiento de los registros de los trabajadores._ | _Rosales Tapia_ | ✔️ |
| __Estimable__ | _La historia de usuario se puede estimar con precisión en términos de tiempo y esfuerzo requerido para completarla._ | _Rosales Tapia_ | ✔️ |
| __Pequeña__ | _La historia de usuario es lo suficientemente pequeña como para que pueda ser completada en un ciclo de funcionalidad._ | _Rosales Tapia_ | ✔️ |
| __Comprobable__ | _La historia de usuario es lo suficientemente específica como para que se pueda comprobar su implementación en el sistema._ | _Rosales Tapia_ | ✔️ |

<!-- #### __Wireframe 04__

![][] -->

----

### __HYST05__

| Identificador | HYST05 |
| :---------- | :-------- |
| __Nombre (alias)__ | Buscar Trabajador por DNI |
| __Descripción__ | Como empleador, quiero poder buscar a un Trabajador por su número de DNI, para poder seleccionarlo. |
| __Puntos de historia (Horas Ideaales)__ | 2 |
| __Criterios de aceptación__ | Al ingresar el DNI debe de tener los 8 caracteres.  |
|| Al ingresar el DNI no debe permitir letras. |
|| Al ingresar el DNI no debe permitir caracteres especiales |
|| Al realizar la búsqueda del trabajador se mostrará su ficha con los datos rellenados en su registro. |

#### __Revisión 05__

| Criterio | Comentario | Realizado por | Solucionado |
| :-------- | :--------- | :----------| :--------:|
| __Completo__ | _La historia está completa y cumple con su propósito de buscar un trabajador con la primary key “DNI”._ | _Zapata Medina_ | ✔️ |
| __Consistente__ | _Es clara y consistente, por lo que evita que el usuario tenga complicaciones con su uso, a su vez alineada a su propósito._ | _Zapata Medina_ | ✔️ |
| __Negocible__ | _Es negociable a cambios de ser necesario, por practicidad o costumbre del usuario._ | _Zapata Medina_ | ✔️ |
| __Valiosa__ | _Es muy valiosa ya que sin esta historia de usuario seria difisil encontrar a los usuarios y aplicar los cambios en torno a su sueldo._ | _Zapata Medina_ | ✔️ |
| __Estimable__ | _Es estimable definiendo límites reales y posibles tanto en tiempo como en esfuerzo por parte del equipo de desarrollo._ | _Zapata Medina_ | ✔️ |
| __Pequeña__ | _Es lo suficientemente pequeña como para ser completada en una sola iteración de desarrollo, a su vez considerando su entrega rápida._ | _Zapata Medina_ | ✔️ |
| __Comprobable__ | _Posee criterios de aceptación claros y  llegó a comprobar con el equipo de desarrollo siendo específico y medible._ | _Zapata Medina_ | ✔️ |

<!-- #### __Wireframe 05__

![][] -->

----

### __HYST06__

| Identificador | HYST06 |
| :---------- | :-------- |
| __Nombre (alias)__ | Seleccionar trabajador |
| __Descripción__ | Como empleador, quiero poder seleccionar un trabajador, para poder administrar y registrar sus datos respecto al sueldo. |
| __Puntos de historia (Horas Ideaales)__ | 1 |
| __Criterios de aceptación__ | Luego de encontrar un trabajador, al hacer click en el resultado este debe de oscurecerse, o tomar un tono oscuro, señalando que se ha seleccionado.  |
|| Al hacer doble click en la ficha del Empleado encontrado, deberá mostrar los datos de este trabajador, esta ficha está acompañada de botones para seleccionar, editar y eliminar, que son para fácil acceso. |
|| En caso de no encontrar un trabajador registrado se mostrará una alerta que indica que: El trabajador no ha sido encontrado. |

#### __Revisión 06__

| Criterio | Comentario | Realizado por | Solucionado |
| :-------- | :--------- | :----------| :--------:|
| __Completo__ | _Está completa y forma parte de otra historia, por lo que su funcionamiento puede afectar otros procedures._ | _Zapata Medina_ | ✔️ |
| __Consistente__ | _Es clara y consistente, por lo que evita que el usuario tenga complicaciones con su uso, a su vez alineada a su propósito._ | _Zapata Medina_ | ✔️ |
| __Negocible__ | _No es negociable a cambios, por practicidad o costumbre del usuario, se recomienda mantener esta historia como tal, llegando así a una comprensión del funcionamiento._ | _Zapata Medina_ | ✔️ |
| __Valiosa__ | _Es valiosa ya que permite seleccionar un trabajador para luego aplicar cambios en sus datos._ | _Zapata Medina_ | ✔️ |
| __Estimable__ | _Es estimable definiendo límites reales y posibles tanto en tiempo como en esfuerzo por parte del equipo de desarrollo._ | _Zapata Medina_ | ✔️ |
| __Pequeña__ | _Es lo suficientemente pequeña como para ser completada en una sola iteración de desarrollo._ | _Zapata Medina_ | ✔️ |
| __Comprobable__ | _Posee criterios de aceptación claros y  llegó a comprobar con el equipo de desarrollo siendo específico y medible._ | _Zapata Medina_ | ✔️ |

#### __Wireframe 03, 04, 05 y 06__

![Crud de trabajador][Crud_Trabajador]

----

## Ítem 6 - Definición de Hecho

> __Todos los criterios de aceptación de cada ítem del producto backlog se han validado y aceptado por el dueño del producto, el trabajo de cada miembro del equipo ha sido revisado por al menos otro miembro del equipo. Todo tiene que estar documentado y con sus respectivos casos de prueba.__

## Ítem 7 - Diseño UML

![Diseño del diagrama UML][Diagrama_UML]

[Modelo Conceptual]: /others/img/modelo_Conceptual.PNG
[Login]: /others/img/login.jpg
[Registrar_Trabajador]: /others/img/registrar_Trabajador.PNG
[Crud_Trabajador]: /others/img/crud_Trabajador.PNG
[Diagrama_UML]: /others/img/diagrama_UML.PNG
