from queue import Queue as Cola

def stock_de_productos(stock_cambios: list[tuple[str, int]]) -> dict[str, tuple[int, int]]:
    res = {}
    for elemento in stock_cambios:
        if elemento[0] not in res:
            res[elemento[0]] = (elemento[1], elemento[1])
        else:
            minimo = res[elemento[0]][0]
            maximo = res[elemento[0]][1]
            
            if elemento[1] < minimo:
                res[elemento[0]] = (elemento[1], maximo)
            elif elemento[1] > maximo:
                res[elemento[0]] = (minimo, elemento[1])
    return res

def filtrar_codigos_primos(codigos_barra:list[int]) -> list[int]:
    lista_res = []
    for numero in codigos_barra:
        ultimos_tres = numero % 1000
        if ultimos_tres >= 2:
            booleano = True
            i = 2
            while i < ultimos_tres:
                if ultimos_tres % i == 0:
                    booleano = False
                i += 1
            if booleano:
                lista_res.append(numero)
    return lista_res

def subsecuencia_mas_larga(tipos_pacientes_atendidos:list[str]) -> int:
    lista_temp = []
    contador = 1
    for i in range(len(tipos_pacientes_atendidos)):
        if i + 1 < len(tipos_pacientes_atendidos) and tipos_pacientes_atendidos[i] == tipos_pacientes_atendidos[i + 1]:
            contador += 1
        elif i + 1 == len(tipos_pacientes_atendidos):
            lista_temp.append(contador)
        else:
            lista_temp.append(contador)
            contador = 1
    
    maximo = 0
    indice = 0
    for j in range(len(lista_temp)):
        if lista_temp[j] > maximo:
            maximo = lista_temp[j]
            indice = j
    suma = 0
    for k in range(indice):
        suma += lista_temp[k]
    return suma


def un_responsable_por_turno(grilla_horaria:list[list[str]]) -> tuple[bool, bool]:
    lista_res = []
    for j in range(len(grilla_horaria[0])):
        primera_pos = grilla_horaria[0][j] == grilla_horaria[1][j] == grilla_horaria[2][j] == grilla_horaria[3][j]
        segunda_pos = grilla_horaria[4][j] == grilla_horaria[5][j] == grilla_horaria[6][j] == grilla_horaria[7][j]
        lista_res.append((primera_pos, segunda_pos))
    return lista_res

def promedio_de_salidas(diccionario:dict[str, list[int]]) -> dict[str, tuple[int, float]]:
    promedios = {}
    for clave in diccionario:
        suma = 0
        longitud = 0
        for numero in diccionario[clave]:
            if 0 < numero < 61:
                suma += numero
                longitud += 1
        promedios[clave] = (longitud, suma/longitud)
    return promedios

def tiempo_mas_rapido(tiempos_salas:list[int]) -> int:
    res = 0
    min = 60
    for elemento in tiempos_salas:
        if 0 < elemento <= 60 and elemento < min:
            min = elemento
    for i in range(len(tiempos_salas)):
        if tiempos_salas[i] == min:
            res = i
    return res

def escape_en_solitario(amigos_por_salas:list[list[int]]) -> list[int]:
    res = []

    for i in range(len(amigos_por_salas)):

        if amigos_por_salas[i][0] == amigos_por_salas[i][1] == amigos_por_salas[i][3] == 0 and not (amigos_por_salas[i][2] == 0):
            res.append(i)
    return res

def torneo_de_gallinas(estrategias:dict[str, str]) -> dict[str, int]:
    diccionario_res = {}
    jugadores = []
    for clave in estrategias:
        diccionario_res[clave] = 0
        jugadores.append(clave)
    for i in range(len(jugadores)):
        for j in range(len(jugadores)):
            if estrategias[jugadores[i]] == estrategias[jugadores[j]] == "me desvio siempre" and i != j:
                diccionario_res[jugadores[i]] -= 10
            elif estrategias[jugadores[i]] == estrategias[jugadores[j]] == "me la banco" and i != j:
                diccionario_res[jugadores[i]] -= 5
            elif estrategias[jugadores[i]] != estrategias[jugadores[j]] and estrategias[jugadores[i]] == "me desvio siempre" and i != j:
                diccionario_res[jugadores[i]] -= 15
            elif estrategias[jugadores[i]] != estrategias[jugadores[j]] and estrategias[jugadores[i]] == "me la banco" and i != j:
                diccionario_res[jugadores[i]] += 10
    return diccionario_res

def reordenar_cola_priorizando_vips(cola:Cola[tuple[str, str]]) -> Cola[str]:
    cola_res:Cola = Cola()
    aux:Cola = Cola()
    while not cola.empty():
        e:tuple[str, str] = cola.get()
        if e[1] == "vip":
            cola_res.put(e[0])
        aux.put(e)

    while not aux.empty():
        f:tuple[str, str] = aux.get()
        if f[1] == "comun":
            cola_res.put(f[0])
        cola.put(f)
    return cola_res

def palindromo(texto:str) -> bool:
    nueva_palabra = ""
    i = len(texto) - 1
    while i >= 0:
        nueva_palabra += texto[i]
        i -= 1
    return nueva_palabra == texto


def dividir_en_sufijos(palabra:str) -> list[str]:
    sufijos = []
    for i in range(len(palabra)):
        sufijo = ""
        for j in range(i, len(palabra)):
            sufijo += palabra[j]
        sufijos.append(sufijo)
    return sufijos


def cuantos_sufijos_son_palindromos(texto:str) -> int:
    contador = 0
    lista_a_probar = []
    palabra = ""
    for letra in texto:
        if letra != " ":
            palabra += letra
        else: 
            lista_a_probar.append(palabra)
            palabra = ""
    lista_a_probar.append(palabra)
    lista_palindromos_sufijos = []

    for elemento in lista_a_probar:
        sufijos = dividir_en_sufijos(elemento)
        for sufijo in sufijos:
            if palindromo(sufijo):
                contador += 1
                lista_palindromos_sufijos.append(sufijo)
    return contador, lista_palindromos_sufijos

def orden_de_atencion(urgentes:Cola[int], postergables:Cola[int]) -> Cola[int]:
    aux_urgentes = Cola()
    aux_postergables = Cola()
    res = Cola()

    while not urgentes.empty() and not postergables.empty():
        elemento_urgentes = urgentes.get()
        elemento_postergables = postergables.get()

        res.put(elemento_urgentes)
        res.put(elemento_postergables)

        aux_urgentes.put(elemento_urgentes)
        aux_postergables.put(elemento_postergables)

    while not aux_urgentes.empty() and not aux_postergables.empty():
        devolver_urgentes = aux_urgentes.get()
        devolver_postergables = aux_postergables.get()

        urgentes.put(devolver_urgentes)
        postergables.put(devolver_postergables)
    
    return res

def alarma_epidemiologica(registros:list[tuple[int, str]], infecciosas:list[str], umbral:int) -> dict[str, int]:
    
    pacientes_totales = len(registros)
    lista_a_eliminar = []

    diccionario_res = {}
    for elemento in registros:
        if elemento[1] not in diccionario_res:
            diccionario_res[elemento[1]] = 1
        elif elemento[1] in diccionario_res:
            diccionario_res[elemento[1]] += 1

    for clave in diccionario_res:
        if not diccionario_res[clave]/pacientes_totales > umbral and clave in infecciosas:
            lista_a_eliminar.append(clave)
        elif diccionario_res[clave]/pacientes_totales > umbral and clave in infecciosas:
            diccionario_res[clave] = diccionario_res[clave]/pacientes_totales
        else:
            lista_a_eliminar.append(clave)

    for i in lista_a_eliminar:
        diccionario_res.pop(i)

    return diccionario_res

def suma(lista:list[int]) -> int:
    total = 0
    for elemento in lista:
        total += elemento
    return total

def maximo(lista:list[int]) -> int:
    maximo = 0
    for elemento in lista:
        if elemento > maximo:
            maximo = elemento
    return maximo

def empleados_del_mes(horas:dict[int, list[int]]) -> list[int]:
    res = []
    lista_aux = []
    for clave in horas:
        sumar = suma(horas[clave])
        lista_aux.append(sumar)

    for clave in horas:
        if suma(horas[clave]) == maximo(lista_aux):
            res.append(clave)
    return res

def nivel_ocupacion_aux(lista:list[bool]) -> float:
    ocupadas:int = 0
    for elemento in lista:
        if elemento:
            ocupadas += 1
    res = ocupadas/len(lista)
    return res

def nivel_ocupacion(m:list[list[bool]]) -> list[int]:
    res:list[int] = []
    for linea in m:
        res.append(nivel_ocupacion_aux(linea))
    return res