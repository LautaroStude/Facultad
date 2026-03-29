#punto 1
def pertenece(s:list, e:int):
    if e in s:
        res:bool = True
    else:
        res = False
    return res

def divide_a_todos(s:list, e:int):
    res:bool = True
    for elemento in s:
        if (elemento % e) != 0:
            res = False
    return res

def suma_total(s:list):
    suma:int = 0
    for elemento in s:
        suma += elemento
    return suma

def ordenador(lista: list):
    copia = []
    for elem in lista:
        copia.append(elem)
    n = len(copia)
    for i in range(n):
        for j in range(0, n - i - 1):
            if copia[j] > copia[j + 1]:
                temp = copia[j]
                copia[j] = copia[j + 1]
                copia[j + 1] = temp
    return copia

def longitud_palabra(s:list):
    res:bool = False
    for palabra in s:
        if len(palabra) >= 7:
            res = True
    return res

def capicua(palabra:str):
    res:bool = False
    i:int = 0
    while i < (len(palabra) - 1):
        if palabra[i] == palabra[(len(palabra) - i) - 1]:
            res = True
        i += 1
    return res

def contrasena(contra:str):
    if tiene_minuscula(contra) and tiene_mayuscula(contra) and tiene_digito(contra) and len(contra) > 8:
        res:bool = "Verde"
    elif len(contra) < 5:
        res = "Roja"
    else:
        res = "Amarilla"
    return res

def tiene_minuscula(contra:str):
    res:bool = False
    for letra in contra:
        if letra.islower():
            res = True
    return res

def tiene_mayuscula(contra:str):
    res:bool = False
    for letra in contra:
        if letra.isupper():
            res = True
    return res

def tiene_digito(contra:str):
    res:bool = False
    for letra in contra:
        if letra.isdigit():
            res = True
    return res

def movimientos_cuenta(movimientos:list[tuple[str, int]]):
    saldo = 0 
    if movimientos[0][0] == "R":
        saldo = "no es posible"
    else:
        for i in range (len(movimientos)):
            if saldo == "no es posible":
                return saldo
            elif movimientos[i][0] == "I":
                saldo = saldo + movimientos[i][1]
            elif movimientos[i][0] == "R" and saldo > movimientos[i][1]:
                saldo = saldo - movimientos[i][1]
            else:
                saldo = "no es posible"
    return saldo

def cant_vocales(palabra:str):
    contador:int = 0
    for letra in palabra:
        if letra in ["a","e","i","o","u","A","E","I","O","U"]:
            contador += 1
    if contador >= 3:
        res:bool = True
    else:
        res = False
    return res

def ceros_en_pares_inout(lista:list[int]):
    i:int = 0
    while i < (len(lista) - 1):
        lista[i] = 0
        i += 2
    return lista

def ceros_en_pares_in(lista:list):
    nueva_lista:list = lista.copy()
    i:int = 0
    while i < (len(lista) - 1):
        nueva_lista[i] = 0
        i += 2
    return nueva_lista

def borrar_vocales_concatenar(palabra:str):
    nueva_palabra:str = ""
    for letra in palabra:
        if letra in "aeiouAEIOU":
            nueva_palabra = nueva_palabra + ""
        else:
            nueva_palabra = nueva_palabra + letra 
    return nueva_palabra

def da_vuelta_str(palabra:str):
    nueva_palabra:str = ""
    i:int = len(palabra) - 1
    while i >= 0:
        nueva_palabra = nueva_palabra + palabra[i]
        i -= 1
    return nueva_palabra

def eliminar_repetidos(palabra:str):
    contador = 0
    nueva_palabra = ""
    for letra in palabra:
        if letra in palabra[(contador + 1):]:
            nueva_palabra = nueva_palabra
        else:
            nueva_palabra = nueva_palabra + letra
        contador += 1
    return nueva_palabra

#preguntar si es legal acceder a la otra parte de la lista como [1:]
#no es legal cambiar
#print(eliminar_repetidos("hoodsalaa"))

#ej3
def aprobado(notas:list):
    res:int = 1
    if (sum(notas))/len(notas) >= 7:
        for nota in notas:
            if nota >= 4 and res != 3:
                res = 1
            else:
                res = 3
    elif (sum(notas))/len(notas) >= 4:
        for nota in notas:
            if nota >= 4 and res != 3:
                res = 2
            else:
                res = 3
    else:
        res = 3
    return res

#ej4
def construir_lista():
    booleano:bool = True
    lista:list = [] 
    while booleano:
        nombre_alumno:str = input("Ingresar nombre, caso cotrario ingresar listo: ")
        if nombre_alumno.lower() == "listo":
            lista = lista
            booleano = False
        else:
            lista.append(nombre_alumno)
            print(lista)
    return lista

def historial_monedero():
    credito:int = 0
    booleano:bool = True
    lista:list = []
    while booleano:
        accion:str = input("C para cargar, D para descontar y X para finalizar: ")
        if accion == "C":
            credito = credito + int(input("monto a cargar: "))
        elif accion == "D":
            descontar:int = int(input("monto a descontar: "))
            if descontar < credito:
                credito = credito - descontar
            else: 
                return "monto no disponible"
        elif accion == "X":
            return credito

#ej5
def pertenece_a_cada_uno(s:list[list[int]], e:int):
    lista_bool:list = []
    for i in range(len(s)):
        if pertenece(s[i], e):
            lista_bool.append(True)
        else:
            lista_bool.append(False)
    return lista_bool 

def es_matriz(s:list[list[int]]):
    res:bool = True
    longitud_primer_lista:int = len(s[0])
    for i in range(len(s)):
        if len(s[i]) == longitud_primer_lista and res:
            res = True
        else:
            res = False
    return res

def filas_ordenadas(m:list[list[int]]):
    lista_bool:list = []
    for fila in m:
        if fila == ordenador(fila):
            lista_bool.append(True)
        else:
            lista_bool.append(False)
    return lista_bool

def columna(m:list[list[int]], numero_columna:int):
    columna:list = []
    for fila in m:
        columna.append(fila[numero_columna])
    return columna

def columnas_ordenadas(m:list[list[int]]):
    lista_bool:list = []
    for i in range(len(m[0])):
        if columna(m, i) == ordenador(columna(m, i)):
           lista_bool.append(True)
        else:
            lista_bool.append(False)
    return lista_bool

def traspuesta(m:list[list[int]]):
    matriz_nueva:list[list[int]] = []
    for i in range(len(m[0])):
        matriz_nueva.append(columna(m, i))
    return matriz_nueva

print(traspuesta([[1,2,3],[4,5,6],[7,8,9]]))

