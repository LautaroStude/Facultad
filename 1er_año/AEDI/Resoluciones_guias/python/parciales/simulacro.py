from queue import Queue as Cola

# Ejercicio 1
def cantidad_parejas_que_suman(s: list[int], n: int) -> int:
    contador:int = 0
    for i in range(len(s)):
        if i < (len(s) - 1):
            for j in range(i+1, len(s)):
                if s[i] + s[j] == n:
                    contador += 1
    return contador

# Ejercicio 2 
def pasar_por_autoservicio(clientes: Cola[tuple[str, str, int]]) -> str:
    aux = Cola()
    copia = Cola()
    lista_nombres = []
    while not clientes.empty():
        tupla = clientes.get()
        aux.put(tupla)
        copia.put(tupla)
    
    while not aux.empty():
        res = aux.get()
        if res[1] != "efectivo" and res[2] <= 15:
            lista_nombres.append(res[0])

    while not copia.empty():
        elemento = copia.get()
        if len(lista_nombres) > 0:
            if elemento[0] != lista_nombres[0]:
                clientes.put(elemento)
        else:
            clientes.put(elemento)

    if len(lista_nombres) > 0:
        final = lista_nombres[0]
        
    else:
        final = ""
    
    return final

# Ejercicio 3 

def obtener_columna(m:list[list[int]], col:int) -> list[int]:
    columna = []
    for i in range(len(m)):
        columna.append(m[i][col])
    return columna

def invertir(matriz:list[list[int]], columna:int) -> list[list[int]]:
    columna_a_cambiar = []
    for i in range(len(matriz)):
        columna_a_cambiar.append(matriz[i][columna])

    i = len(matriz) - 1
    j = len(matriz[0]) - 1
    k = 0
    while j >= 0:
        while i >= (-1):
            if j == columna:
                if i == (-1):
                    i = 0
                matriz[i][j] = columna_a_cambiar[k]
                k += 1
                if i == 0:
                    i = -1
            i -= 1
        i = len(matriz) - 1
        j -= 1
    return matriz

def intercambiar_e_invertir_columnas(A: list[list[int]], col1: int, col2: int) -> None:
    columna1 = obtener_columna(A, col1)
    columna2 = obtener_columna(A, col2)
    
    for i in range(len(A)):
        for j in range(len(A[0])):
            if j == col1:
                A[i][j] = columna2[i]
    for h in range(len(A)):
        for k in range(len(A[0])):
            if k == col2:
                A[h][k] = columna1[h]
    
    invertir(A, col1)
    invertir(A, col2)

    return A

print(intercambiar_e_invertir_columnas(([[1,2],[3,4]]), 0, 1))


# Ejercicio 4
def mantuvieron_residencia(censo1: dict[str, str], censo2: dict[str, str]) -> dict[str, int]:
    dict_res = {}
    for clave in censo1:
        if censo1[clave] not in dict_res and censo1[clave] == censo2[clave]:
            dict_res[censo1[clave]] = 1
        elif censo1[clave] in dict_res and censo1[clave] == censo2[clave]:
            dict_res[censo1[clave]] += 1
    return dict_res
