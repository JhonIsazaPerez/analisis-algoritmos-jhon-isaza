"""Experimentos de medicion: lista enlazada vs. tabla hash."""

import random
import time
from pathlib import Path

import matplotlib.pyplot as plt

from estructuras import ListaEnlazada, TablaHash

TAMANIOS = [100, 500, 1000, 5000, 10000, 20000, 50000]
N_FIJO = 20000
ALFAS = [0.25, 0.5, 1, 2, 4, 10]
BUSQUEDAS = 200
REPETICIONES_LISTA = 5
REPETICIONES_TABLA = 201
MUESTRA_VERIFICACION = 100
SEMILLA = 42
ESTADOS = ["en bodega", "en reparto", "entregado", "devuelto"]
CARPETA_GRAFICAS = Path(__file__).parent / "graficas"

COLORES = {
    "Lista enlazada": "#2a78d6",
    "Tabla hash": "#eb6834",
}


def generar_guias_inexistentes(
    existentes: set[int], cantidad: int, semilla: int = 7
) -> list[int]:
    """Genera guias de diez digitos que no estan en la coleccion.

    Args:
        existentes: guias almacenadas en las estructuras.
        cantidad: cuantas guias inexistentes generar.
        semilla: semilla del generador, para reproducir la medicion.

    Returns:
        Una lista con `cantidad` guias que no pertenecen a `existentes`.
    """
    azar = random.Random(semilla)
    inexistentes: list[int] = []
    while len(inexistentes) < cantidad:
        guia = azar.randint(10**9, 10**10 - 1)
        if guia not in existentes:
            inexistentes.append(guia)
    return inexistentes


def generar_envios(n: int, semilla: int = SEMILLA) -> list[tuple[int, str]]:
    """Genera n envios con guias distintas de diez digitos.

    Args:
        n: cantidad de envios.
        semilla: semilla del generador aleatorio.

    Returns:
        Lista de n tuplas (guia, estado) con guias sin repetir.
    """
    azar = random.Random(semilla)
    guias = azar.sample(range(10**9, 10**10), n)
    return [(guia, azar.choice(ESTADOS)) for guia in guias]


def es_primo(numero: int) -> bool:
    """Indica si un entero es primo, por division de prueba.

    Args:
        numero: entero a evaluar.

    Returns:
        True si el numero es primo.
    """
    if numero < 2:
        return False
    divisor = 2
    while divisor * divisor <= numero:
        if numero % divisor == 0:
            return False
        divisor += 1
    return True


def primo_cercano(objetivo: float) -> int:
    """Busca el primo mas cercano a un valor objetivo.

    Args:
        objetivo: valor alrededor del cual se busca el primo.

    Returns:
        El primo mas cercano a `objetivo` (el menor si hay empate).
    """
    centro = max(2, round(objetivo))
    distancia = 0
    while True:
        if es_primo(centro - distancia):
            return centro - distancia
        if es_primo(centro + distancia):
            return centro + distancia
        distancia += 1


def construir(
    envios: list[tuple[int, str]], m: int
) -> tuple[ListaEnlazada, TablaHash]:
    """Construye una lista y una tabla con los mismos envios.

    Args:
        envios: tuplas (guia, estado) a insertar.
        m: numero de casillas de la tabla.

    Returns:
        La lista enlazada y la tabla hash ya cargadas.
    """
    lista = ListaEnlazada()
    tabla = TablaHash(m)
    for guia, estado in envios:
        lista.insertar(guia, estado)
        tabla.insertar(guia, estado)
    return lista, tabla


def verificar(
    lista: ListaEnlazada, tabla: TablaHash, envios: list[tuple[int, str]]
) -> None:
    """Comprueba que lista y tabla devuelven el mismo estado en una muestra.

    Args:
        lista: lista enlazada cargada.
        tabla: tabla hash cargada con los mismos envios.
        envios: envios insertados en ambas estructuras.
    """
    azar = random.Random(SEMILLA)
    muestra = azar.sample(envios, min(MUESTRA_VERIFICACION, len(envios)))
    for guia, estado in muestra:
        assert lista.buscar(guia) == estado, f"Lista falla en {guia}"
        assert tabla.buscar(guia) == estado, f"Tabla falla en {guia}"


def tiempo_medio(
    estructura: ListaEnlazada | TablaHash,
    guias: list[int],
    repeticiones: int,
) -> float:
    """Mide el tiempo medio por busqueda de un lote de guias.

    Solo se cronometran las busquedas. El lote se repite varias veces
    y se toma el minimo: el ruido del sistema solo suma tiempo, asi que
    el minimo es la estimacion mas estable del costo real.

    Args:
        estructura: lista o tabla sobre la que se busca.
        guias: guias a buscar (inexistentes en la estructura).
        repeticiones: cuantas veces se cronometra el lote completo.

    Returns:
        Tiempo medio por busqueda, en microsegundos.
    """
    tiempos = []
    for _ in range(repeticiones):
        inicio = time.perf_counter()
        for guia in guias:
            estructura.buscar(guia)
        tiempos.append(time.perf_counter() - inicio)
    return min(tiempos) / len(guias) * 1e6


def experimento_a() -> dict[str, list[float]]:
    """Mide lista vs. tabla (alfa cerca de 2) para cada n en TAMANIOS.

    Returns:
        Por estructura, la lista de tiempos medios (microsegundos).
    """
    resultados: dict[str, list[float]] = {nombre: [] for nombre in COLORES}
    print("Experimento A: lista vs. tabla")
    for n in TAMANIOS:
        envios = generar_envios(n)
        m = primo_cercano(n / 2)
        lista, tabla = construir(envios, m)
        verificar(lista, tabla, envios)

        existentes = {guia for guia, _ in envios}
        inexistentes = generar_guias_inexistentes(existentes, BUSQUEDAS)
        for guia in inexistentes:
            assert lista.buscar(guia) is None and tabla.buscar(guia) is None

        t_lista = tiempo_medio(lista, inexistentes, REPETICIONES_LISTA)
        t_tabla = tiempo_medio(tabla, inexistentes, REPETICIONES_TABLA)
        resultados["Lista enlazada"].append(t_lista)
        resultados["Tabla hash"].append(t_tabla)
        print(
            f"  n = {n:>6}  m = {m:>6}  alfa = {tabla.factor_carga():.3f}  "
            f"lista = {t_lista:10.2f} us  tabla = {t_tabla:6.3f} us"
        )
    return resultados


def experimento_b() -> tuple[list[float], list[float]]:
    """Mide la tabla con n = N_FIJO y distintos m (distintos alfa).

    Returns:
        Los alfas reales obtenidos y el tiempo medio (microsegundos)
        de cada uno.
    """
    envios = generar_envios(N_FIJO)
    existentes = {guia for guia, _ in envios}
    inexistentes = generar_guias_inexistentes(existentes, BUSQUEDAS)

    alfas_reales: list[float] = []
    tiempos: list[float] = []
    print(f"Experimento B: tabla con n = {N_FIJO} y distintos alfa")
    for alfa in ALFAS:
        m = primo_cercano(N_FIJO / alfa)
        tabla = TablaHash(m)
        for guia, estado in envios:
            tabla.insertar(guia, estado)
        for guia, estado in envios[:MUESTRA_VERIFICACION]:
            assert tabla.buscar(guia) == estado

        t_tabla = tiempo_medio(tabla, inexistentes, REPETICIONES_TABLA)
        alfas_reales.append(tabla.factor_carga())
        tiempos.append(t_tabla)
        print(
            f"  m = {m:>6}  alfa = {tabla.factor_carga():6.3f}  "
            f"tabla = {t_tabla:6.3f} us"
        )
    return alfas_reales, tiempos


def estilizar(ax: plt.Axes) -> None:
    """Aplica rejilla suave y quita los bordes superior y derecho.

    Args:
        ax: ejes de matplotlib a estilizar.
    """
    ax.grid(True, which="major", color="#e1e0d9", linewidth=0.8)
    ax.set_axisbelow(True)
    for spine in ("top", "right"):
        ax.spines[spine].set_visible(False)


def graficar_lista_vs_tabla(resultados: dict[str, list[float]]) -> None:
    """Genera graficas/lista_vs_tabla.png.

    Args:
        resultados: tiempos medios por estructura del experimento A.
    """
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
        for x, y in zip(TAMANIOS, tiempos):
            ax.annotate(
                f"{y:.2f}" if y < 10 else f"{y:.0f}",
                (x, y),
                textcoords="offset points",
                xytext=(0, 8),
                ha="center",
                fontsize=8,
                color="#444441",
            )
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_title(
        "Busqueda de guias inexistentes: lista enlazada vs. tabla hash "
        "(alfa ~ 2)"
    )
    ax.set_xlabel("Numero de guias n (escala logaritmica)")
    ax.set_ylabel("Tiempo medio por busqueda (microsegundos, escala log)")
    estilizar(ax)
    ax.legend(frameon=False)
    fig.tight_layout()
    fig.savefig(CARPETA_GRAFICAS / "lista_vs_tabla.png", dpi=150)
    plt.close(fig)


def graficar_tiempo_vs_alfa(alfas: list[float], tiempos: list[float]) -> None:
    """Genera graficas/tiempo_vs_alfa.png.

    Args:
        alfas: factores de carga reales de cada tabla.
        tiempos: tiempo medio por busqueda de cada tabla.
    """
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(
        alfas,
        tiempos,
        marker="o",
        markersize=6,
        linewidth=2,
        color=COLORES["Tabla hash"],
        label=f"Tabla hash (n = {N_FIJO})",
    )
    for x, y in zip(alfas, tiempos):
        ax.annotate(
            f"{y:.2f}",
            (x, y),
            textcoords="offset points",
            xytext=(0, 8),
            ha="center",
            fontsize=8,
            color="#444441",
        )
    ax.set_title(
        "Tabla hash: tiempo de busqueda infructuosa vs. factor de carga"
    )
    ax.set_xlabel("Factor de carga alfa = n / m (guias por casilla)")
    ax.set_ylabel("Tiempo medio por busqueda (microsegundos)")
    ax.set_ylim(bottom=0)
    estilizar(ax)
    ax.legend(frameon=False)
    fig.tight_layout()
    fig.savefig(CARPETA_GRAFICAS / "tiempo_vs_alfa.png", dpi=150)
    plt.close(fig)


def main() -> None:
    """Punto de entrada del script."""
    CARPETA_GRAFICAS.mkdir(exist_ok=True)
    resultados = experimento_a()
    graficar_lista_vs_tabla(resultados)
    alfas, tiempos = experimento_b()
    graficar_tiempo_vs_alfa(alfas, tiempos)
    print(f"Graficas guardadas en {CARPETA_GRAFICAS}")


if __name__ == "__main__":
    main()
