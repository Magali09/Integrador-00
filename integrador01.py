from data_stark import lista_personajes
# clase 20/04/2023 Magali Cristofori 1B
# Desafío #01:
# Agregar al código elaborado para cumplir el desafío #00 los siguientes puntos,
# utilizando un menú que permita acceder a cada uno de los puntos por separado.
# A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M
# B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F
# C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
# D. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
# E. Recorrer la lista y determinar cuál es el superhéroe más bajo de género M
# F. Recorrer la lista y determinar cuál es el superhéroe más bajo de género F
# G. Recorrer la lista y determinar la altura promedio de los superhéroes de género M
# H. Recorrer la lista y determinar la altura promedio de los superhéroes de género F
# I. Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)
# J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
# K. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
# L. Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’).
# M. Listar todos los superhéroes agrupados por color de ojos.
# N. Listar todos los superhéroes agrupados por color de pelo.
# O. Listar todos los superhéroes agrupados por tipo de inteligencia


def mostrar_menu_stark01() -> int:

    respuesta = int(input("""
            1. Mostrar el nombre de cada superhéroe de género M
            2. Mostrar el nombre de cada superhéroe de género F
            3. Mostrar el superhéroe más alto de género M
            4. Mostrar el superhéroe más alto de género F
            5. Mostrar el superhéroe más bajo de género M
            6. Mostrar el superhéroe más bajo de género F
            7. Mostrar la altura promedio de los superhéroes de género M
            8. Mostrar la altura promedio de los superhéroes de género F
            9. Mostrar el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (3 / 6) 
            10 Mostrar cuántos superhéroes tienen cada tipo de color de ojos
            11 Mostrar cuántos superhéroes tienen cada tipo de color de pelo
            12 Mostrar cuántos superhéroes tienen cada tipo de inteligencia
            Elija una opcion: """))
    return respuesta


def mostrar_nombres_masculino():
    # A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M
    for data in lista_personajes:
        genero_masculino = data['genero']
        if genero_masculino == "M":
            print(f"Los nombre masculinos son {data['nombre']}")
            
        
    


def mostrar_nombres_femenino():
    # B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F
    for data in lista_personajes:
        genero_femenino = data['genero']
        if genero_femenino == "F":
            print(f"Los nombre femeninos son {data['nombre']}")


def mostrar_mas_alto_masculino():
    # C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
    flag_altura_masculino = True
    altura_maxima_masculino = None
    for data in lista_personajes:
        genero_masculino = data['genero']
        if genero_masculino == 'M':
            altura_parseada_masculino = float(data['altura'])
            if flag_altura_masculino == True or altura_parseada_masculino > altura_maxima_masculino:
                altura_maxima_masculino = altura_parseada_masculino
                flag_altura_masculino = False
                nombre_alto_masculino = data['nombre']
    print(
        f"El superhéroe mas alto masculino es: {altura_maxima_masculino} nombre: {nombre_alto_masculino}")


def mostrar_mas_alta_femenina():
    # D. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
    flag_altura_femenina = True
    altura_maxima_femenino = None

    for data in lista_personajes:
        genero_femenino = data['genero']
        if genero_femenino == 'F':
            altura_parseada_femenina = float(data['altura'])
            if flag_altura_femenina == True or altura_parseada_femenina > altura_maxima_femenino:
                altura_maxima_femenino = altura_parseada_femenina
                flag_altura_femenina = False
                nombre_alto_femenino = data['nombre']
    print(
        f"El superhéroe mas alto femenino es: {altura_maxima_femenino} nombre: {nombre_alto_femenino}")


def mostrar_mas_bajo_masculino():
    # E. Recorrer la lista y determinar cuál es el superhéroe más bajo de género M
    flag_altura_baja_masculino = True
    altura_minima_masculino = None
    for data in lista_personajes:
        genero_masculino = data['genero']
        if genero_masculino == "M":
            altura_parseada_minima_masculino = float(data['altura'])
            if flag_altura_baja_masculino == True or altura_parseada_minima_masculino < altura_minima_masculino:
                altura_minima_masculino = altura_parseada_minima_masculino
                flag_altura_baja_masculino = False
                nombre_masculino_bajo = data['nombre']
    print(
        f"El superhéroe mas bajo masculino es: {altura_minima_masculino} nombre: {nombre_masculino_bajo}")


def mostrar_mas_baja_femenina():
    # F. Recorrer la lista y determinar cuál es el superhéroe más bajo de género F
    flag_altura_baja_femenina = True
    altura_minima_femenino = None
    for data in lista_personajes:
        genero_femenino = data['genero']
        if genero_femenino == 'F':
            altura_parseada_minima_femenina = float(data['altura'])
            if flag_altura_baja_femenina == True or altura_parseada_minima_femenina < altura_minima_femenino:
                altura_minima_femenino = altura_parseada_minima_femenina
                flag_altura_baja_femenina = False
                nombre_femenino_baja = data['nombre']
    print(
        f"El superhéroe mas bajo fememnino es: {altura_minima_femenino} nombre: {nombre_femenino_baja}")


def mostrar_promedio_altura_masculino():
    # G. Recorrer la lista y determinar la altura promedio de los superhéroes de género M
    acumulador_altura_masculina = 0
    contador_altura_masculino = 0
    for data in lista_personajes:

        if data["genero"] == "M":
            altura_masculina = float(data['altura'])
            acumulador_altura_masculina += altura_masculina
            contador_altura_masculino += 1
    promedio_altura_masculino = acumulador_altura_masculina / contador_altura_masculino
    print(
        f"La altura promedio de los superhéroes de género M: {promedio_altura_masculino}")


def mostrar_promedio_altura_femenino():
    # H. Recorrer la lista y determinar la altura promedio de los superhéroes de género F
    acumulador_altura_femenino = 0
    contador_altura_femenino = 0
    for data in lista_personajes:
        if data["genero"] == "F":
            altura_femenino = float(data['altura'])
            acumulador_altura_femenino = altura_femenino + acumulador_altura_femenino
            contador_altura_femenino += 1

    promedio_altura_femenino = acumulador_altura_femenino / contador_altura_femenino
    print(
        f" el promedio de los superhéroes femeninos es {promedio_altura_femenino}")


def mostrar_asociado_nombres():
    # I. Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)
    mostrar_mas_alto_masculino()
    mostrar_mas_alta_femenina()
    mostrar_mas_baja_femenina()
    mostrar_mas_bajo_masculino()


def tipo_color_ojos():
    # J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
    diccionario_ojos = {}
    for data in lista_personajes:
        tipo = data["color_ojos"]
        if tipo in diccionario_ojos:
            diccionario_ojos[tipo] += 1
        else:
            diccionario_ojos[tipo] = 1
        print(f"Cuántos superhéroes tienen cada tipo de color de ojos: {diccionario_ojos}")


def tipo_color_pelo():
    # K. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
    diccionario_pelo = {}
    for data in lista_personajes:
        tipo_pelo = data["color_pelo"]
        if tipo_pelo in diccionario_pelo:
            diccionario_pelo[tipo_pelo] += 1
        else:
            diccionario_pelo[tipo_pelo] = 1
    print(f"cuántos superhéroes tienen cada tipo de color de pelo: {diccionario_pelo}")


def mostrar_inteligencia():
    # L. Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’)
    diccionario_inteligencia = {}
    for data in lista_personajes:
        tipo_inteligencia = data["inteligencia"]
        if tipo_inteligencia in diccionario_inteligencia:
            diccionario_inteligencia[tipo_inteligencia] +=1
        else:
            diccionario_inteligencia[tipo_inteligencia] = 1
            if tipo_inteligencia == "":
                diccionario_inteligencia[tipo_inteligencia] = "No Tiene"
            

    print(f"cuántos superhéroes tienen cada tipo de inteligencia: {diccionario_inteligencia}")


respuesta = True
while respuesta == True:

    mostrar_respuesta = mostrar_menu_stark01()

    match mostrar_respuesta:
        case 1:
            mostrar_nombres_masculino()
        case 2:
            mostrar_nombres_femenino()
        case 3:
            mostrar_mas_alto_masculino()
        case 4:
            mostrar_mas_alta_femenina()
        case 5:
            mostrar_mas_bajo_masculino()
        case 6:
            mostrar_mas_baja_femenina()
        case 7:
            mostrar_promedio_altura_masculino()
        case 8:
            mostrar_promedio_altura_femenino()
        case 9:
            mostrar_asociado_nombres()
        case 10:
            tipo_color_ojos()
        case 11:
            tipo_color_pelo()
        case 12:
            mostrar_inteligencia()
        case 15:
            respuesta = False
