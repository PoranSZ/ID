# Índice
- [Introducción](#introducción)
- [¿Quienes somos?](#Quienes_somos)
- [Desarrollo(tiempo,dedicacion...)](#De_que_va_nuestro_codigo...?)
- [Conclusiones](#conclusiones)

## Introducción
En la era de la información, tener un método efectivo para mantener organizados y localizar datos personales se vuelve crucial. Este código te brinda una solución para ingresar y buscar información de manera estructurada. Puedes registrar datos como nombres, fechas de nacimiento y números de teléfono, y después buscarlos con facilidad. Simplifica tu rutina al mantener tus detalles personales bajo control con este sistema de gestión intuitivo.
## ¿Quienes somos?
Permítannos presentarnos, somos dos personas de 15 años con una pasión compartida por la programación y el desarrollo tecnológico. A medida que nos acercamos al inicio de nuestra experiencia en el bachillerato, hemos decidido invertir nuestro verano en explorar a fondo el mundo de la programación y mejorar nuestras habilidades.

A pesar de nuestra edad, hemos invertido tiempo y esfuerzo en aprender diversos lenguajes de programación y técnicas. Durante este proceso, hemos experimentado la emoción de crear soluciones prácticas y funcionales, y el sistema de gestión de datos personales que presentamos aquí es el fruto de nuestros esfuerzos conjuntos.

Nuestra motivación para desarrollar esta herramienta proviene de la creciente necesidad de mantener los datos personales organizados en una era cada vez más digitalizada. A través de este proyecto, hemos aplicado nuestras habilidades para crear una forma sencilla y eficiente de registrar información y acceder a ella cuando sea necesario.

Este sistema representa más que un simple proyecto de verano para nosotros; simboliza nuestro anhelo compartido de aprender y aplicar la tecnología para resolver problemas del mundo real. Esperamos que esta herramienta resulte útil no solo para nosotros, sino también para aquellos que buscan gestionar sus datos personales de manera más efectiva.
## Desarrollo (nuestro codigo)
Es un programa que  administrar datos personales, agrega personas con detalles como nombre, fecha de nacimiento, teléfono, DNI, etc. Ofrece búsqueda y eliminación, validaciones y guarda datos en un archivo. 

1.Funciones de validación y verificación :
validar_nombre(nombre): Verifica que el nombre solo contenga letras. 
verificar_apellido(apellido): Verifica si un apellido contiene letras.
validar_fecha_nacimiento(fecha): Verifica que la fecha de nacimiento esté en un formato válido y dentro del rango adecuado.
verificar_numero_valido(numero_de_telefono): Verifica si un número de teléfono es válido (9 dígitos numéricos).
verificar_dni(dni): Verifica si un número de DNI (Documento Nacional de Identidad) es válido.
verificar_nie(nie): Verifica si un número de NIE (Número de Identificación de Extranjero) es válido.
verificar_pasaporte(pasaporte): Verifica si un número de pasaporte es válido.

2.Funciones de búsqueda:
buscar_nombre(array, buscarnombre): Busca personas por nombre.
buscar_apellido(array, buscarapellido): Busca personas por apellido.
buscar_numero(array, buscarnumero): Busca personas por número de teléfono.
buscar_dni(array, buscardni): Busca personas por número de DNI/NIE.
buscar_pasaporte(array, buscarpasaporte): Busca personas por número de pasaporte.

3.Funciones para mostrar y cambiar datos:
pedir_datos(): Solicita al usuario que ingrese los datos de una persona y realiza las validaciones correspondientes.
mostrar_resultados(resultados): Muestra los resultados de una búsqueda en la consola.
mostrar_menu_principal(): Muestra el menú principal de búsqueda.
mostrar_menu_busqueda(array): Muestra el menú de búsqueda por diferentes criterios.

4.Funciones para agregar y administrar personas:
pedir_telefono_buscar(): Solicita al usuario que ingrese un número de teléfono para buscar.
buscar_numero_eliminar(numero, datos): Busca y elimina una persona de la lista según el número de teléfono.
ejecutar_menu_busqueda(array): Ejecuta el menú de búsqueda y realiza las operaciones correspondientes.

5.Funciones principales:
main(): Función principal del programa que inicia la aplicación y maneja la creación, búsqueda y administración de personas en la lista.

6.Funciones de escritura y lectura de datos:
escribir_datos(datos): Guarda los datos de las personas en el archivo 'output.txt'.
leer_datos(datos): Lee los datos de las personas desde el archivo 'output.txt'.

El programa crea una lista llamada array para almacenar los datos de las personas. A través de distintos menús, el usuario puede agregar datos de personas, buscar personas por diferentes criterios, eliminar personas y salir del programa. Los datos se almacenan en la lista y se pueden guardar en un archivo de texto para su uso posterior. El programa utiliza funciones de validación y verificación para asegurarse de que los datos ingresados sean válidos y coherentes.

## Conclusiones
En conclusion el programa es una herramienta  para gestionar informacion personal. Ofrece opciones que permite ingresar, buscar y eliminar registros con facilidad. Su capacidad para validar datos garantiza la seguridad de la información ingresada.



