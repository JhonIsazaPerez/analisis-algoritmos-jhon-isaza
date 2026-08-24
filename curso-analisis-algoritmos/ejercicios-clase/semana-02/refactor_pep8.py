def calcular_promedio(numeros: list[float]) -> float:
    """Calcula el promedio de una lista de números.

    Args:
        numeros: Lista de valores numéricos a promediar.

    Returns:
        El promedio (media aritmética) de los valores de la lista.
    """
    suma = 0
    for numero in numeros:
        suma = suma + numero
    return suma / len(numeros)


def main() -> None:
    lista_numeros = [1, 2, 3, 4, 5]
    print(calcular_promedio(lista_numeros))


if __name__ == "__main__":
    main()
