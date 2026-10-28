"""Pruebas de ListaEnlazada y TablaHash."""

import random

from estructuras import ListaEnlazada, TablaHash

# Serie de ejemplo de la situacion problema.
serie = [
    (1000000010, "en bodega"),
    (1000000024, "en reparto"),
    (1000000017, "en bodega"),
    (1000000005, "entregado"),
]

lista = ListaEnlazada()
tabla = TablaHash(7)
for guia, estado in serie:
    lista.insertar(guia, estado)
    tabla.insertar(guia, estado)

# Busqueda exitosa y busqueda infructuosa en ambas estructuras.
assert lista.buscar(1000000024) == "en reparto"
assert tabla.buscar(1000000024) == "en reparto"
assert lista.buscar(1000000005) == "entregado"
assert tabla.buscar(1000000005) == "entregado"
assert lista.buscar(1000000099) is None
assert tabla.buscar(1000000099) is None
assert lista.tamano == 4
assert tabla.tamano == 4

# Estructuras vacias: cualquier busqueda es infructuosa.
assert ListaEnlazada().buscar(10) is None
assert TablaHash(7).buscar(10) is None
assert TablaHash(7).factor_carga() == 0

# Colision forzada: con m = 7, las guias 10, 24 y 17 caen en la casilla 3.
tabla = TablaHash(7)
for guia in (10, 24, 17):
    assert tabla.hash(guia) == 3
    tabla.insertar(guia, "en bodega")

for guia in (10, 24, 17):
    assert tabla.buscar(guia) == "en bodega"
assert tabla.casillas[3].tamano == 3
assert all(
    tabla.casillas[i].tamano == 0 for i in range(tabla.m) if i != 3
)

# Una guia inexistente que cae en la misma casilla tambien debe dar None.
assert tabla.hash(31) == 3
assert tabla.buscar(31) is None
assert tabla.buscar(99) is None

# Factor de carga tras las tres inserciones.
assert tabla.factor_carga() == 3 / 7

# Al menos veinte colecciones aleatorias: lista y tabla deben coincidir
# tanto en guias existentes como en guias inexistentes.
random.seed(42)
estados = ["en bodega", "en reparto", "entregado", "devuelto"]
for _ in range(25):
    n = random.randint(1, 500)
    m = random.randint(1, 100)
    guias = random.sample(range(1000000000, 10000000000), n)

    lista = ListaEnlazada()
    tabla = TablaHash(m)
    for guia in guias:
        estado = random.choice(estados)
        lista.insertar(guia, estado)
        tabla.insertar(guia, estado)

    assert tabla.factor_carga() == n / m

    for guia in guias:
        assert lista.buscar(guia) == tabla.buscar(guia)
        assert tabla.buscar(guia) is not None

    existentes = set(guias)
    inexistentes = 0
    while inexistentes < 50:
        guia = random.randint(1000000000, 9999999999)
        if guia in existentes:
            continue
        assert lista.buscar(guia) is None, f"Guia inexistente {guia} en lista"
        assert tabla.buscar(guia) is None, f"Guia inexistente {guia} en tabla"
        inexistentes += 1

print("Todas las pruebas pasaron correctamente.")
