"""Pruebas de subarreglo_fuerza_bruta y subarreglo_maximo."""

import random

from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo

# Serie de ocho dias de la situacion problema: la mejor racha suma 17.
serie = [-3, 5, -2, 8, -6, 3, 9, -4]
assert subarreglo_fuerza_bruta(serie)[2] == 17
assert subarreglo_maximo(serie, 0, len(serie) - 1)[2] == 17

# Un solo elemento positivo y uno negativo.
un_elemento = [42]
assert subarreglo_fuerza_bruta(un_elemento)[2] == 42
assert subarreglo_maximo(un_elemento, 0, 0)[2] == 42

un_elemento_negativo = [-7]
assert subarreglo_fuerza_bruta(un_elemento_negativo)[2] == -7
assert subarreglo_maximo(un_elemento_negativo, 0, 0)[2] == -7

# Todos los valores negativos: la mejor racha es el menos negativo.
todos_negativos = [-5, -2, -8, -1, -9]
assert subarreglo_fuerza_bruta(todos_negativos)[2] == -1
assert subarreglo_maximo(todos_negativos, 0, len(todos_negativos) - 1)[2] == -1

# Todos los valores positivos: la mejor racha es la serie completa.
todos_positivos = [3, 1, 4, 1, 5, 9, 2]
suma_total = sum(todos_positivos)
assert subarreglo_fuerza_bruta(todos_positivos)[2] == suma_total
assert subarreglo_maximo(todos_positivos, 0, len(todos_positivos) - 1)[2] == suma_total

# Caso clasico donde el mejor tramo cruza el punto medio: con 9 elementos,
# medio = (0 + 8) // 2 = 4, y la mejor racha es el tramo [3, 6] = [4, -1, 2, 1],
# que incluye tanto el indice 4 (mitad izquierda) como el 5 y 6 (mitad derecha).
cruzado = [2, -1, -3, 4, -1, 2, 1, -5, 4]
assert subarreglo_fuerza_bruta(cruzado)[2] == 6
assert subarreglo_maximo(cruzado, 0, len(cruzado) - 1)[2] == 6

# Ninguna funcion debe modificar la lista recibida.
original = list(cruzado)
subarreglo_fuerza_bruta(cruzado)
subarreglo_maximo(cruzado, 0, len(cruzado) - 1)
assert cruzado == original, "Las funciones no deben modificar la lista recibida"

# Al menos veinte listas aleatorias: ambas funciones deben coincidir en la suma.
random.seed(42)
for _ in range(25):
    n = random.randint(1, 60)
    datos = [random.randint(-50, 50) for _ in range(n)]

    suma_fuerza_bruta = subarreglo_fuerza_bruta(datos)[2]
    suma_divide_venceras = subarreglo_maximo(datos, 0, len(datos) - 1)[2]

    assert suma_fuerza_bruta == suma_divide_venceras, (
        f"Discrepancia para datos={datos}: "
        f"fuerza_bruta={suma_fuerza_bruta}, divide_venceras={suma_divide_venceras}"
    )

print("Todas las pruebas pasaron correctamente.")
