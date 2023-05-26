

from os import system

from data_stark import lista_personajes


def mostrar_menu() -> int:

    respuesta = int(input("""1.Mostrar nombres superhéroes
            2 Mostrar nombre y altura de superhéroe
            3 Mostrar superhéroe más alto y su nombre
            4 Mostrar superhéroe más bajo y  su nombre
            5 Mostrar promedio de alturas
            6 Mostrar superhéroe más pesado y  su nombre
            7 Mostrar superhéroe menos pesado y  su nombre
            Elija una opcion: """))
    return respuesta


def mostrar_nombres():
    # B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
    for data in lista_personajes:
        print(f"{data['nombre']}")


def mostrar_nombre_altura():
    # C. Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo

    for data in lista_personajes:
        print(f"{data['nombre']} -- {data['altura']}")


def mostrar_mas_alto():
    # D. Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
    flag_altura = True
    altura_maxima = None
    for data in lista_personajes:
        altura_parseada = float(data['altura'])
        if flag_altura == True or altura_maxima > altura_parseada:
            altura_maxima = data['altura']
            flag_altura = False
    print(
        f"El superhéroe mas alto es: {altura_maxima} nombre: {data['nombre']}")


def mostrar_mas_bajo():
    # E. Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
    flag_minima = True
    altura_minima = None
    for data in lista_personajes:
        altura_parseada_minima = float(data['altura'])
        if flag_minima == True or altura_minima < altura_parseada_minima:
            altura_minima = data['altura']
            nombre_mas_bajo = data['nombre']
            flag_minima = False
    print(
        f"El superhéroe mas bajo es: {altura_minima} nombre: {nombre_mas_bajo}")


def mostrar_promedio():
    # F. Recorrer la lista y determinar la altura promedio de los superhéroes(PROMEDIO)
    # G. Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)
    acumulador_altura = 0
    contador_altura = 0
    for data in lista_personajes:
        altura_parseada_promedio = float(data['altura'])
        acumulador_altura += altura_parseada_promedio
        contador_altura += 1

        promedio_altura = acumulador_altura / contador_altura

        print(
            f"El promedio de altura de los superhéroes es: {promedio_altura}")


def mostrar_mas_menos_pesado():

    # H. Calcular e informar cual es el superhéroe más y menos pesado.
    flag_mas_pesado = True
    flag_menos_pesado = True
    mas_pesado = None
    peso = None
    for data in lista_personajes:
        peso_parseado_maximo = float(data['peso'])
        if flag_mas_pesado == True or data['peso'] > mas_pesado:
            mas_pesado = data['peso']
            nombre_mas_pesado = data['nombre']
            flag_mas_pesado = False

        print(
            f"El peso mayor es : {mas_pesado} y su nombre{nombre_mas_pesado}")


flag_menos_pesado = True
menos_pesado = None
peso = None
for data in lista_personajes:
    peso_parseado_minimo = float(data['peso'])
    if flag_menos_pesado == True or data['peso'] < menos_pesado:
        menos_pesado = data['peso']
        nombre_menos_pesado = data['nombre']
        flag_menos_pesado = False

print(f"El peso mayor es : {menos_pesado} y su nombre: {nombre_menos_pesado}")

respuesta = True
while respuesta == True:
    system("cls")
    mostrar_respuesta = mostrar_menu()

    match mostrar_respuesta:
        case 1:
            mostrar_nombres()
        case 2:
            mostrar_nombre_altura()
        case 3:
            mostrar_mas_alto()
        case 4:
            mostrar_mas_bajo()
        case 5:
            mostrar_promedio()
        case 6:
            mostrar_mas_menos_pesado()
        case 7:
            respuesta = False


