"""Experimento de la Parte 4: validacion experimental de la complejidad.

Mide el tiempo de ejecucion de insertion sort y merge sort sobre el
escenario A (aleatorio) de Tamiza, para los mismos tamanos de entrada
de la Parte 3, y grafica ambas curvas en los mismos ejes.
"""

import statistics
import time
from pathlib import Path

import matplotlib.pyplot as plt

from algoritmos import insertion_sort, merge_sort
from datos import generar_aleatorio
from parte3_casos import REPETICIONES, TAMANIOS

CARPETA_GRAFICAS = Path(__file__).parent / "graficas"

ALGORITMOS = {
    "Insertion sort": insertion_sort,
    "Merge sort": merge_sort,
}

COLORES = {
    "Insertion sort": "#2a78d6",
    "Merge sort": "#eb6834",
}


def ejecutar_experimento() -> dict[str, list[float]]:
    """Mide el tiempo de cada algoritmo sobre el escenario A, por tamano.

    Cada medicion se repite REPETICIONES veces sobre el mismo lote de
    datos y se reporta el promedio, para suavizar el ruido de medicion.

    Returns:
        Un diccionario por nombre de algoritmo con la lista de tiempos
        promedio (segundos) registrados para cada tamano en TAMANIOS.
    """
    resultados = {nombre: [] for nombre in ALGORITMOS}

    for n in TAMANIOS:
        print(f"n = {n}")
        datos = generar_aleatorio(n)

        for nombre, algoritmo in ALGORITMOS.items():
            tiempos = []
            for _ in range(REPETICIONES):
                inicio = time.perf_counter()
                algoritmo(datos)
                tiempos.append(time.perf_counter() - inicio)

            duracion_promedio = statistics.mean(tiempos)
            resultados[nombre].append(duracion_promedio)
            print(f"  {nombre}: {duracion_promedio:.6f} s (promedio de {REPETICIONES})")

    return resultados


def graficar_tiempo(resultados: dict) -> None:
    """Genera graficas/parte4_tiempo.png."""
    fig, ax = plt.subplots(figsize=(8, 5))

    for nombre, tiempos in resultados.items():
        ax.plot(
            TAMANIOS,
            tiempos,
            marker="o",
            markersize=6,
            linewidth=2,
            color=COLORES[nombre],
            label=nombre,
        )

    ax.set_title("Insertion sort vs. merge sort: tiempo de ejecucion (escenario A)")
    ax.set_xlabel("Tamano de entrada (n, numero de registros)")
    ax.set_ylabel(f"Tiempo de ejecucion (segundos, promedio de {REPETICIONES} repeticiones)")
    ax.grid(True, color="#e1e0d9", linewidth=0.8)
    ax.set_axisbelow(True)
    for spine in ("top", "right"):
        ax.spines[spine].set_visible(False)
    ax.legend(frameon=False)

    fig.tight_layout()
    fig.savefig(CARPETA_GRAFICAS / "parte4_tiempo.png", dpi=150)
    plt.close(fig)


def main() -> None:
    """Punto de entrada del script."""
    CARPETA_GRAFICAS.mkdir(exist_ok=True)
    resultados = ejecutar_experimento()
    graficar_tiempo(resultados)
    print(f"Grafica guardada en {CARPETA_GRAFICAS}")


if __name__ == "__main__":
    main()
