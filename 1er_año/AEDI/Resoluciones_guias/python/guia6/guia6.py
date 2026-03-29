import math 

def imprimir_hola_mundo():
    print("hola mundo")

def imprimir_un_verso(frase: str):
    print(frase)

def factorial_2():
    return 2*1

def perimetro():
    return 2*math.pi

#ej2 ----------------------------    

def imprimir_saludo(nombre:str):
    print("hola " + nombre)

def raiz_cuadrada_de(numero:int):
    return sqrt(numero)

def fahrenheit_a_celsius(t:float):
    return ((t-32)*5)/9

def imprimir_dos_veces(estribillo:str):
    print (estribillo + "\n" + estribillo)

def es_multiplo_de(numero:int, multiplo:int):
    return ((multiplo % numero) == 0)

def es_par(numero:int):
    return (numero % 2) == 0

def cantidad_de_pizzas(comensales:int, min_cant_de_porciones:int):
    porciones:int = comensales * min_cant_de_porciones
    if (porciones % 8) == 0:
        res:int = porciones/8
    else:
        res = (porciones % 8) + 1  
    return res  

#ej3 --------------------------

def alguno_es_0(numero1:int, numero2:int):
    if numero1 == 0:
        res = "primer numero"
    elif numero2 == 0:
        res = "segundo numero"
    else:
        res = "ninguno"
    return res

def ambos_0(numero1:int, numero2:int):
    if (numero1 == 0) and (numero2 == 0):
        res = "ambos son 0"
    else:
        res = "ambos no son 0"
    return res

def es_nombre_largo(nombre:str):
    if len(nombre) < 3:
        res = False
    elif len(nombre) <= 8 and len(nombre) >= 3:
        res = True
    else:
        res = False
    return res

def es_bisiesto(año:int):
    if año % 4 == 0:
        res = True
    else:
        res = False
    return res

#ej5 ---------------------------

def devolver_el_doble_si_es_par(numero:int):
    if numero % 2 == 0:
        res = numero * 2
    else:
        res = numero
    return res

def devolver_valor_si_es_par_sino_el_que_sigue(numero:int):
    if numero % 2 == 0:
        res = numero
    else:
        res = numero + 1
    return res

#ej6 ----------------------------
def uno_al_diez():
    i:int = 1
    while i < 10:
        print(i)
        i += 1
    return i

def diez_a_cuarenta_pares():
    i = 10
    while i < 40:
        print(i)
        i += 2
    return i

def eco():
    i = 0
    while i < 10:
        print("eco")
        i += 1
    
def cuenta_regresiva(desde:int):
    primer_numero:int = desde
    while primer_numero >= 1:
        print("desde")
        primer_numero -= 1
    