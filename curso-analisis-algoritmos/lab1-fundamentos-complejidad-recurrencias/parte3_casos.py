"""Experimento de la Parte 3: peor caso, mejor caso y caso promedio.

Ejecuta insertion sort sobre los tres escenarios de entrada de Tamiza
(aleatorio, casi ordenado, orden inverso), para una serie de tamanos de
entrada, y grafica el numero de comparaciones y el tiempo de ejecucion
de cada escenario.
"""

import time
from pathlib import Path

import matplotlib.pyplot as plt

from algoritmos import insertion_sort
from datos import generar_aleatorio, generar_casi_ordenado, generar_inverso

TAMANIOS = [100, 200, 400, 800, 1600, 3200, 6400]
CARPETA_GRAFICAS = Path(__file__).parent / "graficas"

ESCENARIOS = {
    "A - Aleatorio": generar_aleatorio,
    "B - Casi ordenado": generar_casi_ordenado,
    "C - Orden inverso": generar_inverso,
}

COLORES = {
    "A - Aleatorio": "#2a78d6",
    "B - Casi ordenado": "#eb6834",
    "C - Orden inverso": "#1baf7a",
}


def ejecutar_experimento() -> dict[str, dict[str, list[float]]]:
    """Corre insertion sort sobre los tres escenarios y cada tamano.

    Returns:
        Un diccionario por nombre de escenario, con las listas de
        tiempo (segundos) y comparaciones registradas por tamano.
    """
    resultados = {nombre: {"tiempo": [], "comparaciones": []} for nombre in ESCENARIOS}

    for n in TAMANIOS:
        print(f"n = {n}")
        for nombre, generador in ESCENARIOS.items():
            datos = generador(n)

            inicio = time.perf_counter()
            _, comparaciones = insertion_sort(datos)
            duracion = time.perf_counter() - inicio

            resultados[nombre]["tiempo"].append(duracion)
            resultados[nombre]["comparaciones"].append(comparaciones)
            print(f"  {nombre}: {duracion:.6f} s, {comparaciones} comparaciones")

    return resultados


def _graficar(resultados, clave, titulo, etiqueta_y, nombre_archivo):
    fig, ax = plt.subplots(figsize=(8, 5))

    for nombre, datos in resultados.items():
        ax.plot(
            TAMANIOS,
            datos[clave],
            marker="o",
            markersize=6,
            linewidth=2,
            color=COLORES[nombre],
            label=nombre,
        )

    ax.set_title(titulo)
    ax.set_xlabel("Tamano de entrada (n, numero de registros)")
    ax.set_ylabel(etiqueta_y)
    ax.grid(True, color="#e1e0d9", linewidth=0.8)
    ax.set_axisbelow(True)
    for spine in ("top", "right"):
        ax.spines[spine].set_visible(False)
    ax.legend(frameon=False)

    fig.tight_layout()
    fig.savefig(CARPETA_GRAFICAS / nombre_archivo, dpi=150)
    plt.close(fig)


def graficar_comparaciones(resultados: dict) -> None:
    """Genera graficas/parte3_comparaciones.png."""
    _graficar(
        resultados,
        clave="comparaciones",
        titulo="Insertion sort: comparaciones vs. tamano de entrada",
        etiqueta_y="Numero de comparaciones",
        nombre_archivo="parte3_comparaciones.png",
    )


def graficar_tiempo(resultados: dict) -> None:
    """Genera graficas/parte3_tiempo.png."""
    _graficar(
        resultados,
        clave="tiempo",
        titulo="Insertion sort: tiempo de ejecucion vs. tamano de entrada",
        etiqueta_y="Tiempo de ejecucion (segundos)",
        nombre_archivo="parte3_tiempo.png",
    )


def main() -> None:
    """Punto de entrada del script."""
    CARPETA_GRAFICAS.mkdir(exist_ok=True)
    resultados = ejecutar_experimento()
    graficar_comparaciones(resultados)
    graficar_tiempo(resultados)
    print(f"Graficas guardadas en {CARPETA_GRAFICAS}")


if __name__ == "__main__":
    main()
