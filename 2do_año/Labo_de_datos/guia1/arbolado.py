import csv
import pandas as pd
ruta_1 = '/Users/lautarostude/Facultad/2do_año/Labo_de_datos/guia1/arbolado-en-espacios-verdes.csv'
ruta_2 = "/Users/lautarostude/Facultad/2do_año/Labo_de_datos/guia1/arbolado-publico-lineal-2017-2018.csv"

def leer_parque(nombre_archivo, parque):
    lista_arboles = []
    
    with open(nombre_archivo, 'rt', encoding='utf-8') as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        
        for fila in filas:
            arbol = dict(zip(encabezado, fila))
            if arbol['espacio_ve'] == parque:
                lista_arboles.append(arbol)
                
    return lista_arboles

def especies(lista_arboles):
    especies = set()

    for arbol in lista_arboles:
        especies.add(arbol['nombre_com'])
    return especies

def contar_ejemplares(lista_arboles):
    diccionario = {}

    for arbol in lista_arboles:
        especie = arbol["nombre_com"]
        if especie not in diccionario:
            diccionario[especie] = 1
        else:
            diccionario[especie] += 1
    return diccionario

def obtener_altura(lista_arboles, especie):
    lista = []

    for arbol in lista_arboles:
        if arbol["nombre_com"] == especie:
            lista.append(float(arbol["altura_tot"]))
    return lista

alturas = obtener_altura(leer_parque(ruta_1, "GENERAL PAZ"), "Jacarandá")
maximo = max(alturas)
promedio = sum(alturas)/len(alturas)

def obtener_inclinaciones(lista_arboles, especie):
    lista = []

    for arbol in lista_arboles:
        if arbol["nombre_com"] == especie:
            lista.append(float(arbol["inclinacio"]))
    return lista

inclinaciones = obtener_inclinaciones(leer_parque(ruta_1, "GENERAL PAZ"), "Jacarandá")

def especimen_mas_inclinado(lista_arboles):
    maximo = 0.0
    conjunto_especies = especies(lista_arboles)
    for especie in conjunto_especies:
        maximo_especie = max(obtener_inclinaciones(lista_arboles, especie))
        
        if maximo_especie > maximo:
            especie_mas_inclinada = especie
            maximo = maximo_especie

    return especie_mas_inclinada, max(obtener_inclinaciones(lista_arboles, especie_mas_inclinada))

mas_inclinado = especimen_mas_inclinado(leer_parque(ruta_1, "RICCHIERI, PABLO, Tte. Gral."))

def especie_promedio_mas_inclinada(lista_arboles):
    promedio_maximo = 0.0
    conjunto_especies = especies(lista_arboles)
    
    for especie in conjunto_especies:
        inclinaciones_especie = obtener_inclinaciones(lista_arboles, especie)
        
        promedio_especie = sum(inclinaciones_especie) / len(inclinaciones_especie)
        
        if promedio_especie > promedio_maximo:
            especie_mas_inclinada = especie
            promedio_maximo = promedio_especie

    return especie_mas_inclinada, promedio_maximo

df_parques = pd.read_csv(ruta_1)
df_veredas = pd.read_csv(ruta_2)

df_tipas_parques = df_parques[df_parques["nombre_cientifico"] == "Tipuana tipu"][["columna_diametro", "altura_tot"]].copy
df_tipas_veredas = df_veredas[df_veredas['nombre_cientifico'] == 'Tipuana tipu'][['diametro_altura_pecho', 'altura_arbol']].copy()
df_tipas_parques = df_tipas_parques.rename(columns={
    'altura_tot': 'altura_arbol',
    'columna_diametro': 'diametro_altura_pecho'
})
df_tipas_parques["ambiente"] = "parque"
pd.concat([df_tipas_parques, df_tipas_veredas])
