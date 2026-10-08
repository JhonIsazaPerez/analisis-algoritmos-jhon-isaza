"""Algoritmos de ordenamiento instrumentados para el Laboratorio 1."""


def insertion_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de insercion.

    No modifica la lista recibida: trabaja sobre una copia.

    Args:
        datos: lista de indices de riesgo a ordenar.

    Returns:
        Una tupla con la lista ordenada y el numero total de
        comparaciones entre elementos realizadas durante el proceso.
    """
    resultado = list(datos)
    comparaciones = 0

    for i in range(1, len(resultado)):
        actual = resultado[i]
        j = i - 1
        while j >= 0:
            comparaciones += 1
            if resultado[j] > actual:
                resultado[j + 1] = resultado[j]
                j -= 1
            else:
                break
        resultado[j + 1] = actual

    return resultado, comparaciones


def merge_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de mezcla.

    No modifica la lista recibida: trabaja sobre una copia.

    Args:
        datos: lista de indices de riesgo a ordenar.

    Returns:
        Una tupla con la lista ordenada y el numero total de
        comparaciones entre elementos realizadas durante el proceso.
    """
    resultado = list(datos)
    comparaciones = _dividir(resultado, 0, len(resultado) - 1)
    return resultado, comparaciones


def _dividir(datos: list[int], inicio: int, fin: int) -> int:
    """Divide recursivamente el tramo [inicio, fin] y mezcla los resultados.

    Args:
        datos: lista sobre la que se ordena el tramo, modificada in place.
        inicio: indice inicial (incluido) del tramo a dividir.
        fin: indice final (incluido) del tramo a dividir.

    Returns:
        El numero de comparaciones realizadas al mezclar este tramo.
    """
    if inicio >= fin:
        return 0

    medio = (inicio + fin) // 2
    comparaciones = _dividir(datos, inicio, medio)
    comparaciones += _dividir(datos, medio + 1, fin)
    comparaciones += _mezclar(datos, inicio, medio, fin)
    return comparaciones


def _mezclar(datos: list[int], inicio: int, medio: int, fin: int) -> int:
    """Mezcla dos tramos ordenados [inicio, medio] y [medio+1, fin].

    Modifica `datos` in place para dejar el tramo [inicio, fin] ordenado.

    Args:
        datos: lista que contiene ambos tramos, modificada in place.
        inicio: indice inicial (incluido) del primer tramo.
        medio: indice final (incluido) del primer tramo; el segundo
            tramo empieza en medio + 1.
        fin: indice final (incluido) del segundo tramo.

    Returns:
        El numero de comparaciones entre elementos de los dos tramos.
    """
    izquierda = datos[inicio:medio + 1]
    derecha = datos[medio + 1:fin + 1]

    i = j = 0
    k = inicio
    comparaciones = 0

    while i < len(izquierda) and j < len(derecha):
        comparaciones += 1
        if izquierda[i] <= derecha[j]:
            datos[k] = izquierda[i]
            i += 1
        else:
            datos[k] = derecha[j]
            j += 1
        k += 1

    while i < len(izquierda):
        datos[k] = izquierda[i]
        i += 1
        k += 1

    while j < len(derecha):
        datos[k] = derecha[j]
        j += 1
        k += 1

    return comparaciones
