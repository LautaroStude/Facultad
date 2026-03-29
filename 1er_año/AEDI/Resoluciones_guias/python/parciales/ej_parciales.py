from queue import Queue as Cola
def nivel_ocupacion_aux(lista:list[bool]) -> float:
    ocupadas:int = 0
    for elemento in lista:
        if elemento:
            ocupadas += 1
    res = ocupadas/len(lista)
    return res

print("ej1 aux", nivel_ocupacion_aux([True, False, True]))

def nivel_ocupacion(m:list[list[bool]]) -> list[int]:
    res:list[int] = []
    for linea in m:
        res.append(nivel_ocupacion_aux(linea))
    return res

print("ej1", nivel_ocupacion([[True, False, True],[False,False,False],[True,False,False]]))

def cambiar_matriz(m:list[list [int]]) -> list[list[int]]:
    copia = m.copy()
    for i in range(len(m)):
        if i < (len(m) - 1):
            m[i] = copia[i + 1]
        else:
            m[i] = copia[0]
    return m

print("ej2", cambiar_matriz([[1,2],[3,4],[5,6],[7,8]]))

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

print("ej3", promedio_de_salidas({"l":[1,2,3,61,54], "h":[2,3,4,53,12]}))

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


cola = Cola()
cola.put(("Ana", "comun"))
cola.put(("Juli", "vip"))
cola.put(("Fede", "vip"))
cola.put(("asdasd","comun"))
print((reordenar_cola_priorizando_vips(cola)).queue)

