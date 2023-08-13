import re
import datetime

def pedir_telefono_buscar():
    while True:
        telefono = input("Escribe tu numero de telefono (que tenga 9 digitos): ")
        if len(telefono) == 9 and telefono.isdigit():
            return int(telefono)
        else:
            print("El número de teléfono no es válido. Debe tener 9 dígitos numéricos.")
               
    #input del telf, si no lo pone bien, que lo vuelva a intetnar
    #return telf;

def buscar_numero_eliminar(numero, datos):
    for sub_array in datos: 
        if str(numero) == sub_array[3]:
            datos.remove(sub_array)
            print(f"El número {numero} fue encontrado y el sub_array fue eliminada del array.")
            return
    print(f"El número {numero} no se encuentra en ninguna tupla del array.")

#buscar en el array datos el numero,
#existe el numero, coges posicion y haces remove de datos

def ejecutar_menu_busqueda(array):
   while True:
        mostrar_menu_principal()
        opcion = input("Escoja una opcion: 1/2/3/4 ")

        if opcion == "1":
            datos_persona = pedir_datos()
            if datos_persona is not None:
                array.append(datos_persona)
        elif opcion == "2":
            ejecutar_menu_busqueda(array)
        elif opcion == "3":
            break
        elif opcion == "4":
            print("HA SALIDO DEL PROGRAMA")
            break
        else:
            print("ERROR")

def mostrar_menu_principal():
    print("Buscar por:")
    print("1) Nombre")
    print("2) Apellido")
    print("3) Número")
    print("4) DNI")
    print("5) NIE")
    print("6) Pasaporte")
    print("7) Volver al menu principal")

def ejecutar_menu_principal(array):
    while True:
        mostrar_menu_busqueda()
        opcion = input("Elije una opcion: ")

        if opcion == "1":
            nombre_buscar = input("Ingrese el nombre a buscar: ")
            resultados = buscar_nombre(array, nombre_buscar)
            if resultados:
                mostrar_resultados(resultados)
            else:
                print("aun no hay resultados")
        elif opcion == "2":
            apellido_buscar = input("Ingrese el apellido a buscar: ")
            resultados = buscar_apellido(array, apellido_buscar)
            if resultados:
             mostrar_resultados(resultados)
            else:
                print("aun no hay resultados")
        elif opcion == "3":
            numero_buscar = input("Ingrese el numero a buscar: ")
            resultados = buscar_numero(array, numero_buscar)
            if resultados:
                mostrar_resultados(resultados)
            else:
                print("aun no hay resultado")
        elif opcion == "4":
            dni_buscar = input("Ingrese el DNI a buscar: ")
            resultados = buscar_dni(array, dni_buscar)
            if resultados:
                mostrar_resultados(resultados)
            else:
                print("aun no hay resultados")
        elif opcion == "5":
            nie_buscar = input("Ingrese el NIE a buscar: ")
            resultados = buscar_nie(array, nie_buscar)
            if resultados:
                mostrar_resultados(resultados)
            else:
                print("aun no hay resultados")
        elif opcion == "6":
            pasaporte_buscar = input("Ingrese el pasaporte a buscar: ")
            resultados = buscar_pasaporte(array, pasaporte_buscar)
            if resultados:
                mostrar_resultados(resultados)
            else:
                print(" aun no hay resultados")
        elif opcion == "7":
            break
        else:
            print("ERROR, intenta de nuevo")


def mostrar_resultados(resultados):
      print(resultados[0])
      print(resultados[1])
      print(resultados[2])
      print(resultados[3])
      print(resultados[4])
      print(resultados[5])
      print(resultados[6])
      print(resultados[7])


def main():
    array = []
    while True:
        print("Pon los datos de esa persona")
        datos_persona = pedir_datos()
        if datos_persona is not None:
            array.append(datos_persona)

        salir = input("Pulse 1 para salir o cualquier otro número para continuar ingresando datos: ")
        if salir == "1":
            break

    print("Buscador de personas")
    while True:
        print("Ponga los datos de una persona")
        datos_persona = pedir_datos()
        if datos_persona is not None:
            array.append(datos_persona)

        salir = input("Pulse 1 para salir o cualquier otro numero para continuar ingresando datos: ")
        if salir == "1":
            break

    while True:
        print("¿Cómo quieres buscar a esa persona?")
def validar_nombre(nombre):
    patron_nombre = r'^[a-zA-Z]+$'
    if not re.match(patron_nombre, nombre):
        raise ValueError("El nombre debe contener solo letras (sin números ni caracteres especiales).")
    return nombre

def buscar_nombre(array, buscarnombre):
    resultados = []
    for datos_persona in array:
        nombre = datos_persona[0]
        if buscarnombre.lower() in nombre.lower():
            resultados.append(datos_persona)
    return resultados

def verificar_apellido(apellido):
    for caracter in apellido:
        if caracter.isalpha():
            return False
    return True

def buscar_apellido(array, buscarapellido):
    resultados = []
    for datos_persona in array:
        apellido = datos_persona[1]
        if buscarapellido.lower() in apellido.lower():
            resultados.append(datos_persona)
    return resultados

def validar_fecha_nacimiento(fecha):
    try:
        fecha_parseada = datetime.datetime.strptime(fecha, '%d/%m/%Y')
        fecha_minima = datetime.datetime(year=1900, month=1, day=1)
        fecha_maxima = datetime.datetime.today()
        if fecha_parseada < fecha_minima or fecha_parseada > fecha_maxima:
            raise ValueError("La fecha de nacimiento está fuera de rango.")
    except ValueError:
        raise ValueError("ERROR. Debe ser dia/mes/año.")
    return fecha_parseada

def buscar_numero(array, buscarnumero):
    resultados = []
    for datos_persona in array:
        numero = datos_persona[3]
        if buscarnumero == numero:
            resultados.append(datos_persona)
    return resultados

def verificar_numero_valido(numero_de_telefono):
    if numero_de_telefono.isdigit() and len(numero_de_telefono) == 9:
        return True
    else:
        return False

def verificar_dni(dni):
    if len(dni) != 9:
        return False
    if not dni[:8].isdigit() or not dni[8].isalpha():
        return False

    tabla_letras = "TRWAGMYFPDXBNJZSQVHLCKE"
    letra_calculada = tabla_letras[int(dni[:8]) % 23]
    if dni[8].upper() != letra_calculada:
        return False
    else:
        return True

def buscar_dni(array, buscardni):
    resultados = []
    for datos_persona in array:
        dni_nie = datos_persona[2]
        if buscardni == dni_nie:
            resultados.append(datos_persona)
    return resultados

def verificar_nie(nie):
    if len(nie) != 9:
        return False

    letras_validas = "XYZ"
    primer_caracter = nie[0].upper()

    if primer_caracter not in letras_validas:
        return False

    if not nie[1:8].isdigit() or not nie[-1].isalpha():
        return False 

    tabla_letras = "TRWAGMYFPDXBNJZSQVHLCKE"
    letra_calculada = tabla_letras[int(nie[1:8]) % 23]

    if nie[-1].upper() != letra_calculada:
        return False
    else:
        return True

def buscar_nie(array, buscarnie):
    resultados = []
    for datos_persona in array:
        dni_nie = datos_persona[2]
        if buscarnie == dni_nie:
            resultados.append(datos_persona)
    return resultados

def verificar_pasaporte(pasaporte):
    if len(pasaporte) != 9:
        return False
    return True

def buscar_pasaporte(array, buscarpasaporte):
    resultados = []
    for datos_persona in array:
        pasaporte = datos_persona[5]
        if buscarpasaporte == pasaporte:
            resultados.append(datos_persona)
    return resultados

def pedir_datos():
    datos = []
    
    print("Bienvenido para crear su identidad")
    nombre = input("Escribe tu nombre: ")
    

    
    try:
        nombre_validado = validar_nombre(nombre)
        print(f"Nombre válido: {nombre_validado}")
    except ValueError as e:
        print(f"Error: {e}")
        return None

    apellido = input("Escribe tu apellido: ")
    if not verificar_apellido(apellido):
        print("El apellido contiene letras.")
    else:
        print("¡El apellido no contiene letras!")
        return None

    fecha_nacimiento = input("Escribe tu fecha de nacimiento (día/mes/año): ")
    try:
        fecha_validada = validar_fecha_nacimiento(fecha_nacimiento)
        print(f"Fecha de nacimiento válida: {fecha_validada.strftime('%d/%m/%Y')}")
    except ValueError as e:
        print(f"Error: {e}")
        return None

    numero = input("Escribe tu numero: ")
    if verificar_numero_valido(numero):
        print("Número válido.")
    else:
        print("ERROR")
        return None

    while True:
        tipo_documento = input("Elige el tipo de documento (dni/NIE): ").lower()
        if tipo_documento == "dni":
            dni = input("Escribe aqui tu DNI: ")
            if verificar_dni(dni):
                print("valido")
                break
            else:
                print("ERROR")
        elif tipo_documento == "nie":
            nie = input("Escribe aqui tu NIE: ")
            if verificar_nie(nie):
                print("valido")
                break
            else:
                print("ERROR")
        else:
            print("error") 

    pasaporte = input("Escribe aquí tu pasaporte: ")
    if verificar_pasaporte(pasaporte):
        print("Número de pasaporte válido.")
    else:
        print("ERROR, ponga su número de pasaporte correctamente.")
        return None

    datos_persona = (
        nombre_validado,
        apellido,
        dni if dni else nie,
        numero,
        fecha_validada,
        pasaporte
    )

    return datos_persona



def ejecutar_menu_busqueda(array):
   while True:
        mostrar_menu_principal()
        opcion = input("Escoja una opción: 1/2/3/4 ")

        if opcion == "1":
            datos_persona = pedir_datos()
            if datos_persona is not None:
                array.append(datos_persona)
        elif opcion == "2":
            ejecutar_menu_busqueda(array)
        elif opcion == "3":
            numero = pedir_telefono_buscar()
        elif opcion == "4":
            print("HA SALIDO DEL PROGRAMA")
            break
        else:
            print("ERROR")
    

def mostrar_menu_busqueda(array):
    while True:
        print("Buscar por:")
        print("1) Nombre")
        print("2) Apellido")
        print("3) Numero")
        print("4) DNI")
        print("5) NIE")
        print("6) Pasaporte")
        print("7) Volver al menu principal")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            nombre_buscar = input("Ingrese el nombre a buscar: ")
            resultados = buscar_nombre(array, nombre_buscar)
            mostrar_resultados(resultados)
        elif opcion == "2":
            apellido_buscar = input("Ingrese el apellido a buscar: ")
            resultados = buscar_apellido(array, apellido_buscar)
            mostrar_resultados(resultados)
        elif opcion == "3":
            numero_buscar = input("Ingrese el número a buscar: ")
            resultados = buscar_numero(array, numero_buscar)
            mostrar_resultados(resultados)
        elif opcion == "4":
            dni_buscar = input("Ingrese el DNI a buscar: ")
            resultados = buscar_dni(array, dni_buscar)
            mostrar_resultados(resultados)
        elif opcion == "5":
            nie_buscar = input("Ingrese el NIE a buscar: ")
            resultados = buscar_nie(array, nie_buscar)
            mostrar_resultados(resultados)
        elif opcion == "6":
            pasaporte_buscar = input("Ingrese pasaporte a buscar: ")
            resultados = buscar_pasaporte(array, pasaporte_buscar)
            mostrar_resultados(resultados)
        elif opcion == "7":
            break
        else:
            print("ERROR")



def ejecutar_menu_principal(array):
    while True:
        print("1: Mostrar menu para introducir datos")
        print("2: Mostrar menu de busqueda")
        print("3: Eliminar")
        print("4: Salir")
        opcion = input("Elije opcion: ")

        if opcion == "1":
            print("Pon los datos de esa persona")
            datos_persona = pedir_datos()
            if datos_persona is not None:
                array.append(datos_persona)
        elif opcion == "2":
            mostrar_menu_busqueda(array)
        elif opcion == "3":
             n = pedir_telefono_buscar()
             buscar_numero_eliminar(n, datos)
        elif opcion == "4":
            print("HA SALIDO DEL PROGRAMA")
            break
        else:
            print("ERROR")

def mostrar_resultados(resultados):
    if resultados:
        print("Resultados de la busqueda:")
        for resultado in resultados:
            print(resultado)
    else:
        print("No se encontraron resultados.")

def main():
    array = []
    while True:
        print("Create una identidad")
        datos_persona = pedir_datos()
        if datos_persona is not None:
            array.append(datos_persona)

        salir = input("Pulse 1 para salir o cualquier otro numero para continuar poniendo datos: ")
        if salir == "1":
            break

    print("Buscador de personas")
    while True:
        print("Ponga los datos de una persona")
        datos_persona = pedir_datos()
        if datos_persona is not None:
            array.append(datos_persona)

        salir = input("Pulse 1 para salir o cualquier otro numero para continuar poniendo datos: ")
        if salir == "1":
            break

    while True:
        print("¿como quieres buscar a esa persona?")


def escribir_datos(datos):
    with open('output.txt', 'w') as file:  
        for dato in datos:
            file.write('\t'.join(map(str, dato)) + '\n')

def leer_datos(datos):
    try:
        with open('output.txt', 'r') as file:
            contenido = file.readlines()
            for linea in contenido:
                dato = linea.strip().split('\t')
                datos.append(dato)
    except FileNotFoundError:
        print("El archivo no existe.")


datos = []
leer_datos(datos)
ejecutar_menu_principal(datos)
escribir_datos(datos)
 
 
 


