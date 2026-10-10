"""Experimento de medicion: fuerza bruta vs. divide y venceras."""

import random
import statistics
import time
from pathlib import Path

import matplotlib.pyplot as plt

from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo

TAMANIOS = [10, 50, 100, 500, 1000, 4000, 8000]
REPETICIONES = 3
SEMILLA = 42
CARPETA_GRAFICAS = Path(__file__).parent / "graficas"

COLORES = {
    "Fuerza bruta": "#2a78d6",
    "Divide y venceras": "#eb6834",
}


def generar_datos(n: int, semilla: int = SEMILLA) -> list[int]:
    """Genera n variaciones diarias de caja, enteras y reproducibles.

    Args:
        n: cantidad de dias (tamano del lote).
        semilla: semilla del generador aleatorio.

    Returns:
        Lista de n enteros entre -100 y 100.
    """
    generador = random.Random(semilla)
    return [generador.randint(-100, 100) for _ in range(n)]


def ejecutar_experimento() -> dict[str, list[float]]:
    """Mide el tiempo de ambos algoritmos para cada tamano de entrada.

    Usa el mismo lote de datos para los dos algoritmos en cada tamano,
    verifica que ambos devuelvan la misma suma, y repite cada medicion
    REPETICIONES veces para reportar el tiempo promedio.

    Returns:
        Un diccionario por nombre de algoritmo con la lista de tiempos
        promedio (segundos) para cada tamano en TAMANIOS.
    """
    resultados = {"Fuerza bruta": [], "Divide y venceras": []}

    for n in TAMANIOS:
        datos = generar_datos(n)

        tiempos_fb = []
        suma_fb = None
        for _ in range(REPETICIONES):
            inicio = time.perf_counter()
            _, _, suma_fb = subarreglo_fuerza_bruta(datos)
            tiempos_fb.append(time.perf_counter() - inicio)

        tiempos_dc = []
        suma_dc = None
        for _ in range(REPETICIONES):
            inicio = time.perf_counter()
            _, _, suma_dc = subarreglo_maximo(datos, 0, len(datos) - 1)
            tiempos_dc.append(time.perf_counter() - inicio)

        assert suma_fb == suma_dc, (
            f"Discrepancia en n={n}: fuerza_bruta={suma_fb}, divide_venceras={suma_dc}"
        )

        promedio_fb = statistics.mean(tiempos_fb)
        promedio_dc = statistics.mean(tiempos_dc)
        resultados["Fuerza bruta"].append(promedio_fb)
        resultados["Divide y venceras"].append(promedio_dc)
        print(
            f"n = {n}: fuerza bruta {promedio_fb:.6f} s (prom. {REPETICIONES}), "
            f"divide y venceras {promedio_dc:.6f} s (prom. {REPETICIONES}), "
            f"suma coincide = {suma_fb}"
        )

    return resultados


def graficar(resultados: dict[str, list[float]]) -> None:
    """Genera graficas/tiempo_vs_n.png."""
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

    ax.set_title("Subarreglo maximo: fuerza bruta vs. divide y venceras")
    ax.set_xlabel("Tamano de entrada (n, numero de dias)")
    ax.set_ylabel(f"Tiempo de ejecucion (segundos, promedio de {REPETICIONES} repeticiones)")
    ax.grid(True, color="#e1e0d9", linewidth=0.8)
    ax.set_axisbelow(True)
    for spine in ("top", "right"):
        ax.spines[spine].set_visible(False)
    ax.legend(frameon=False)

    fig.tight_layout()
    fig.savefig(CARPETA_GRAFICAS / "tiempo_vs_n.png", dpi=150)
    plt.close(fig)


def main() -> None:
    """Punto de entrada del script."""
    CARPETA_GRAFICAS.mkdir(exist_ok=True)
    resultados = ejecutar_experimento()
    graficar(resultados)
    print(f"Grafica guardada en {CARPETA_GRAFICAS}")


if __name__ == "__main__":
    main()
