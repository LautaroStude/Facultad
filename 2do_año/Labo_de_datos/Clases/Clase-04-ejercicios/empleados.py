empleado_01 = [
    [20222333, 45, 2, 20000],
    [33456234, 40, 0, 25000],
    [45432345, 41, 1, 10000]
]

def superanSalarioActividad01(matriz, umbral):
    matriz_filtrada = []
    
    for empleado in matriz:
        salario = empleado[3]
        
        if salario > umbral:
            matriz_filtrada.append(empleado)
            
    return matriz_filtrada

resultado = superanSalarioActividad01(empleado_01, 15000)

for fila in resultado:
    print(fila)


empleado_02 = [
    [20222333, 45, 2, 20000],
    [33456234, 40, 0, 25000],
    [45432345, 41, 1, 10000],
    [43967304, 37, 0, 12000],
    [42236276, 36, 0, 18000]
]

resultado_02 = superanSalarioActividad01(empleado_02, 15000)

for fila in resultado_02:
    print(fila)


empleado_03 = [
    [20222333, 20000, 45, 2],
    [33456234, 25000, 40, 0],
    [45432345, 10000, 41, 1],
    [43967304, 12000, 37, 0],
    [42236276, 18000, 36, 0]
]

def superanSalarioActividad03(matriz, umbral):
    matriz_filtrada = []
    
    for empleado in matriz:
        dni = empleado[0]
        salario = empleado[1]
        edad = empleado[2]
        hijos = empleado[3]
        
        if salario > umbral:
            fila_formateada = [dni, edad, hijos, salario]
            matriz_filtrada.append(fila_formateada)
            
    return matriz_filtrada

resultado_03 = superanSalarioActividad03(empleado_03, 15000)

for fila in resultado_03:
    print(fila)


empleado_04 = [
    [20222333, 33456234, 45432345, 43967304, 42236276],
    [20000, 25000, 10000, 12000, 18000],
    [45, 40, 41, 37, 36],
    [2, 0, 1, 0, 0]
]

def superanSalarioActividad04(matriz, umbral):
    matriz_filtrada = []
    
    cantidad_empleados = len(matriz[0])
    
    for i in range(cantidad_empleados):
        salario = matriz[1][i]
        
        if salario > umbral:
            dni = matriz[0][i]
            edad = matriz[2][i]
            hijos = matriz[3][i]
            
            fila_formateada = [dni, edad, hijos, salario]
            matriz_filtrada.append(fila_formateada)
            
    return matriz_filtrada

resultado_04 = superanSalarioActividad04(empleado_04, 15000)

for fila in resultado_04:
    print(fila)