import random
from queue import LifoQueue as Pila
from queue import Queue as Cola

print("\nParte 1 Pilas")
def generar_nros_al_azar(cantidad:int, desde:int, hasta:int) -> Pila[int]:
    p = Pila()
    for i in range(cantidad):
        p.put(random.randint(desde, hasta))
    return p

p = generar_nros_al_azar(12,1,20)
h = generar_nros_al_azar(12,30,90)
print("ej1", p.queue, h.queue)


def cantidad_elementos(p:Pila) -> int:
    cantidad = 0
    for i in p.queue:
        cantidad += 1
    return cantidad

print("ej2", cantidad_elementos(p))

def buscar_el_maximo(p:Pila) -> int:
    max = 0
    aux = Pila()
    while not p.empty():
        n = p.get()
        if n > max:
            max = n
        aux.put(n)
    while not aux.empty():
        p.put(aux.get())

    return max

print("ej3", buscar_el_maximo(p))

def buscar_nota_maxima(p:Pila[tuple[str, int]]) -> tuple[str, int]:
    max = ("", 0)
    aux = Pila()
    while not p.empty():
        tupla = p.get()
        if tupla[1] > max[1]:
            max = tupla
        aux.put(tupla)
    while not aux.empty():
        p.put(aux.get())

    return max

def tokenizar(expresion: str) -> Pila:
    operadores = "+-*/"
    pila = Pila()
    token = ""
    
    for caracter in expresion:
        if caracter == ' ':
            if token != "":
                pila.put(token)
                token = ""
        elif caracter in operadores:
            if token != "":
                pila.put(token)
                token = ""
            pila.put(caracter)
        else:
            token = token + caracter
    
    if token != "":
        pila.put(token)
    
    return pila

def evauluar_expresion(expresion:str) -> float:
    pila:Pila = tokenizar(expresion)
    token_ordenado:Pila = Pila()
    
    while not pila.empty():
        n = pila.get()
        token_ordenado.put(n)

    pila_evaluacion = Pila()
    operadores = "+-*/"
    
    while not token_ordenado.empty():
        token = token_ordenado.get()
        
        if token in operadores:
            operando2 = pila_evaluacion.get()
            operando1 = pila_evaluacion.get()
            
            if token == '+':
                resultado = operando1 + operando2
            elif token == '-':
                resultado = operando1 - operando2
            elif token == '*':
                resultado = operando1 * operando2
            elif token == '/':
                resultado = operando1 / operando2 
            
            pila_evaluacion.put(resultado)
        else:
            pila_evaluacion.put(float(token))
    

    return pila_evaluacion.get()

print("aux6", tokenizar("3 10 + 5 * 2 -").queue)
print("ej6", evauluar_expresion("3 10 + 5 * 2 -"))

def copiar(pila: Pila) -> Pila:
    aux = Pila()
    copia = Pila()

    while not pila.empty():
        e = pila.get()
        aux.put(e)

    while not aux.empty():
        e = aux.get()
        pila.put(e)
        copia.put(e)
    return copia

def invertir(pila: Pila) -> Pila:
    aux1 = Pila()
    aux2 = Pila()

    while not pila.empty():
        e = pila.get()
        aux1.put(e)

    while not aux1.empty():
        e = aux1.get()
        aux2.put(e)
        pila.put(e)  

    return aux2

def intercalar(c1: Pila, c2: Pila) -> Pila:
    res = Pila()

    copia1 = copiar(c1)
    copia2 = copiar(c2)

    copia1 = invertir(copia1)
    copia2 = invertir(copia2)

    while not copia1.empty() and not copia2.empty():
        e1 = copia1.get()
        e2 = copia2.get()
        res.put(e1)
        res.put(e2)

    res = invertir(res)
    return res

print("ej7", intercalar(p, h).queue)



print("\nParte 2 Colas")

def generar_nros_al_azar_cola(cantidad:int, desde:int, hasta:int) -> Cola:
    c:Cola = Cola()
    for i in range(cantidad):
        c.put(random.randint(desde, hasta))
    return c

t = generar_nros_al_azar_cola(12, 43, 89)
print("ej8", t.queue)

def cant_elementos_cola(c:Cola) -> int:
    cantidad = 0
    for i in c.queue:
        cantidad += 1
    return cantidad

print("ej9",cant_elementos_cola(t))

def buscar_el_maximo_cola(c:Cola) -> int:
    max = 0
    aux = Cola()

    while not c.empty():
        n = c.get()
        if n > max:
            max = n 
        aux.put(n)
    while not aux.empty():
        p = aux.get()
        c.put(p)

    return max

print("ej10", buscar_el_maximo_cola(t))

def buscar_nota_minima(c:Cola[tuple[str, int]]) -> tuple[str, int]:
    min = ("", 10)
    aux = Cola()

    while not c.empty():
        tupla = c.get()
        if tupla[1] < min[1]:
            min = tupla
        aux.put(tupla)
    while not aux.empty():
        n = aux.get()
        c.put(n)
    return min

curso = Cola()
curso.put(["a", 2])
curso.put(["b", 3])
print("ej11", buscar_nota_minima(curso))

from queue import Queue

def copiar(cola: Cola) -> Cola:
    aux = Cola()
    copia = Cola()

    while not cola.empty():
        e = cola.get()
        aux.put(e)
        copia.put(e)

    while not aux.empty():
        cola.put(aux.get())

    return copia

def intercalar(c1: Cola, c2: Cola) -> Cola:
    res = Cola()

    copia1 = copiar(c1)
    copia2 = copiar(c2)

    while not copia1.empty() and not copia2.empty():
        e1 = copia1.get()
        e2 = copia2.get()
        res.put(e1)
        res.put(e2)

    return res

def pacientes_urgentes(c:Cola[tuple[int, str, str]]) -> int:
    aux = Cola()
    urgentes = 0

    while not c.empty():
        a = c.get()
        if a[0] < 4:
            urgentes += 1 
        aux.put(a)
    
    while not aux.empty():
        b = aux.get()
        c.put(b)
    return urgentes

pacientes = Cola()
pacientes.put([1, "a", "b"])
pacientes.put([5, "r", "t"])
pacientes.put([7, "q", "n"])
print("ej14", pacientes_urgentes(pacientes))

def artencion_a_clientes(c:Cola[tuple[str, int, bool, bool]]):
    cola_res:Cola = Cola()
    aux:Cola = Cola()

    while not c.empty():
        e = c.get()
        if e[3]:
            cola_res.put(e)
        aux.put(e)
    
    while not aux.empty():
        p = aux.get()
        if e[2]:
            cola_res.put(p)
        c.put(p)

    while not c.empty():
        e = c.get()
        if not e[3] and not e[2]:
            cola_res.put(e)
        aux.put(e)

    while not aux.empty():
        c.put(aux.get())

    return cola_res

print("\nParte 3 Diccionarios")

def calcular_promedio_por_estudiante(notas:list[tuple[str, int]]) -> dict[str, float]:
    dicccionario = {}
    for elemento in notas:
        if elemento[0] not in dicccionario:
            dicccionario[elemento[0]] = elemento[1]
        else:
            dicccionario[elemento[0]] = dicccionario[elemento[0]] + elemento[1]

    for clave in dicccionario:
        dicccionario[clave] = dicccionario[clave] / (cant_veces(notas, clave))
    
    return dicccionario

def cant_veces(lista:list[tuple[str, int]], nombre:str) -> int:
    contador = 0
    for elemento in lista:
        if elemento[0] == nombre:
            contador += 1
    return contador


print("ej16", calcular_promedio_por_estudiante([("a",6),("a",9),("b",4),("b",3),("b",1)]))

def pasar_a_lista(diccionario:dict[str, Pila]) -> dict[str, list]:
    for clave in diccionario:
        diccionario[clave] = diccionario[clave].queue
    return diccionario

def historiales(lista:list[tuple[str, str]]) -> dict[str, Pila]:
    diccionario:dict = {}
    for elemento in lista:
        if elemento[0] not in diccionario:
            diccionario[elemento[0]] = Pila()

        diccionario[elemento[0]].put(elemento[1])

    return diccionario

ejemplo1 = (historiales([("usuario1", "adsadds"),("usuario2","fafa"),("usuario1", "dasa")]))
print("ej17 crear historial", pasar_a_lista(ejemplo1))

def sacar_historial(diccionario:dict[str: Pila], usuario:str) -> dict[str, Pila]:
    for clave in diccionario:
        if clave == usuario and not diccionario[clave].empty():
            (diccionario[clave]).get()
    return diccionario

ejemplo2 = (historiales([("usuario1", "adsadds"),("usuario2","fafa"),("usuario1", "dasa")]))
sacar_del_historial = (sacar_historial(ejemplo2, "usuario1"))
print("ej17 eliminar de historial", pasar_a_lista(sacar_del_historial))

def agregar_producto(diccionario:dict[str, dict[str, int | float]], nombre:str, precio:float, cantidad:int):
    diccionario[nombre] = {"precio":precio, "cantidad":cantidad}
    return diccionario

inventario = {}
inventario = agregar_producto(inventario, "Manzanas", 150.50, 10)
print("ej18 parte 1", inventario)
inventario = agregar_producto(inventario, "Leche", 250.0, 5)
inventario = agregar_producto(inventario, "Pan", 80.0, 15)
print("ej18 parte 1", inventario)

def actualizar_stock(diccionario:dict[str, dict[str, int | float]], nombre:str, cantidad:int):
    for clave in diccionario:
        if nombre == clave:
            diccionario[clave]["cantidad"] = cantidad
    return diccionario

inventario = actualizar_stock(inventario, "Pan", 40)
print("ej18 parte 2", inventario)

def actualizar_precio(diccionario:dict[str, dict[str, int | float]], nombre:str, precio:float):
    for clave in diccionario:
        if nombre == clave:
            diccionario[clave]["precio"] = precio
    return diccionario

inventario = actualizar_precio(inventario, "Pan", 200.0)
print("ej18 parte 3", inventario)

def calcular_valor_inventario(diccionario:dict[str, dict[str, int | float]]) -> float:
    total = 0
    for clave in diccionario:
        total = total + diccionario[clave]["cantidad"] * diccionario[clave]["precio"]
    return total

valor_total = calcular_valor_inventario(inventario)
print("ej18 parte 4", valor_total)

print("\nParte 4 Archivos")

def contar_lineas(archivo:str) -> int:
    with open(archivo, 'r', encoding='utf-8') as contenido:
        lista = contenido.readlines()
        longitud = len(lista)
    return longitud

print("ej19 parte 1", contar_lineas("texto.txt"))

def existe_palabra(archivo:str, palabra:str) -> bool:
    with open(archivo, "r", encoding="utf-8") as contenido:
        lista = contenido.readlines()
        res = False
        for elemento in lista:
            if palabra in elemento:
                res = True
    return res

print("ej19 parte 2", existe_palabra("texto.txt", "dsasdadqwgfs"))

def cantidad_de_apariciones(archivo:str, palabra:str) -> int:
    with open(archivo, "r", encoding="utf-8") as contenido:
        contador = 0
        lista = contenido.readlines()
        for elemento in lista:
            palabra_temp:str = ''
            for letra in elemento:
                if letra == ' ' or letra == '\n':
                    if palabra_temp == palabra:
                        contador += 1
                    palabra_temp = ''
                else:
                    palabra_temp = palabra_temp + letra
    return contador

print("ej19 parte 3", cantidad_de_apariciones("texto.txt", "as"))

def agrupar_por_longitud(archivo:str) -> dict[int, int]:
    with open(archivo, "r", encoding="utf-8") as contenido:
        lista = contenido.readlines()
        diccionario = {}
        for elemento in lista:
            palabra_temp = ""
            for letra in elemento:
                if letra == " " or letra == "\n":
                    if len(palabra_temp) not in diccionario:
                        diccionario[len(palabra_temp)] = 1
                    else:
                        diccionario[len(palabra_temp)] = diccionario[len(palabra_temp)] + 1
                    palabra_temp = ""
                else:
                    palabra_temp = palabra_temp + letra
    return diccionario

print("ej20", agrupar_por_longitud("texto.txt"))

def clonar_sin_comentarios(archivo_entrada:str, archivo_salida:str):
    lista_nueva = []
    with open(archivo_entrada, "r", encoding="utf-8") as contenido:
        lista = contenido.readlines()
        for linea in lista:
            if not linea[0] == "#":
                lista_nueva.append(linea)
    with open(archivo_salida, "w", encoding="utf-8") as salida:
        salida.writelines(lista_nueva)
    return "archivo cambiado"

print("ej22", clonar_sin_comentarios("ej_comentarios_entrada22.txt", "ej_comentarios_salida22.txt"))

def invertir_lineas(archivo_entrada:str, archivo_salida:str):
    with open(archivo_entrada, "r", encoding="utf-8") as contenido:
        lista = contenido.readlines()
        for i in range(len(lista)):
            copia = lista[i].copy
            lista[i] = lista[len(lista) - i - 1]
            lista[len(lista) - i - 1] = copia
    return lista

#print(invertir_lineas("ej_comentarios_entrada23.txt", "ej_comentarios_salida23.txt"))

def agregar_frase_al_final(archivo:str, frase:str):
    with open(archivo, "r", encoding="utf-8") as contenido:
        lista = contenido.readlines()
        lista.append(frase)
    with open(archivo, "w", encoding="utf-8") as cambiado:
        cambiado.writelines(lista)
    return "archivo cambiado"

#lo mismo al principio

def obtener_lu(linea):
    lu = ""
    i = 0
    while i < len(linea) and linea[i] != ',':
        lu += linea[i]
        i += 1
    return lu

def obtener_nota(linea):
    nota = ""
    i = len(linea) - 1
    while i >= 0 and linea[i] != ',':
        if linea[i] != '\n' and linea[i] != ' ':
            nota = linea[i] + nota
        i -= 1
    return float(nota)

def promedio_estudiante(lineas, lu):
    suma = 0
    cantidad = 0
    for linea in lineas:
        lu_actual = obtener_lu(linea)
        if lu_actual == lu:
            nota = obtener_nota(linea)
            suma += nota
            cantidad += 1
    return suma / cantidad 

def calcular_promedio_por_estudiante(nombre_archivo_notas, nombre_archivo_promedios):
    with open(nombre_archivo_notas, "r") as archivo:
        lineas = archivo.readlines()

    lus = []
    for linea in lineas:
        lu = obtener_lu(linea)
        if lu not in lus:
            lus.append(lu)

    with open(nombre_archivo_promedios, "w") as promedios:
        for lu in lus:
            promedio = promedio_estudiante(lineas, lu)
            promedios.write(lu + "," + str(promedio) + "\n")
    return "archivo creado"