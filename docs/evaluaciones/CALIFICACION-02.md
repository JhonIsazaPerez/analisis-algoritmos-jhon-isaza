# Retroalimentación — Laboratorio 2: Dividir y vencer

**Estudiante:** Jhon Alejandro Isaza Pérez · **Laboratorio:** Laboratorio evaluativo 02 — Dividir y vencer
**Fecha límite:** 2026-10-21 23:59 · **Versión revisada:** commit `f52f6cd`

Excelente trabajo, el laboratorio está muy completo y bien sustentado con sus propias mediciones.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 19 / 20 |
| Calidad de la explicación teórica | 20 / 20 |
| Corrección de la implementación | 25 / 25 |
| Calidad del análisis de las gráficas | 25 / 25 |
| Documentación y organización del informe | 7 / 10 |
| **Total** | **96 / 100** |
| **Nota (0–5)** | **4.80** |

## 1. Corrección conceptual (19 / 20)
**Lo que hizo bien:**
- Identifica con sus datos que divide y vencerás empieza a ganar entre n=10 y n=50, y explica por qué en n=10 pierde (el costo de las llamadas recursivas).
- Compara con el máximo de un arreglo: combinar cuesta `Θ(1)`, la recurrencia da `Θ(n)` y por eso dividir no mejora nada.
- Recomienda divide y vencerás y declara que lo de 1.000.000 de registros es una estimación, sin usar regla de tres lineal.

**Lo que puede mejorar:**
- Las estimaciones (18.6 horas y 6.9 segundos) salen de ajustar una constante con solo dos puntos. Convendría mencionar que son aproximadas por esa razón.

## 2. Calidad de la explicación teórica (20 / 20)
**Lo que hizo bien:**
- Plantea `T(n) = 2T(n/2) + Θ(n)` explicando de dónde sale cada término y verifica el caso 2 del método maestro.
- Justifica el `Θ(n²)` de la fuerza bruta sumando las iteraciones de los dos ciclos.

## 3. Corrección de la implementación (25 / 25)
**Lo que hizo bien:**
- Las tres funciones dan resultados correctos, resuelven los tres casos y no llaman a la fuerza bruta.
- Las pruebas cubren todos los casos pedidos, incluido uno cruzado, y 25 listas aleatorias.
- Código ordenado, con type hints y docstrings en cada función.

## 4. Calidad del análisis de las gráficas (25 / 25)
**Lo que hizo bien:**
- La gráfica tiene título, ejes rotulados, leyenda y ambas curvas en los mismos ejes, con 7 tamaños.
- Calcula el factor al duplicar n (4.08× y 2.27×) y lo compara bien con `Θ(n²)` y `Θ(n log n)`; las cifras coinciden con la tabla y la gráfica.

## 5. Documentación y organización del informe (7 / 10)
**Lo que hizo bien:**
- El informe sigue el orden pedido, tiene instrucciones de reproducción, enlaces al código en cada parte y la gráfica se ve.
- Hay varios commits con mensajes descriptivos.

**Lo que puede mejorar:**
- No siguió la estructura de carpetas acordada: el laboratorio quedó dentro de `curso-analisis-algoritmos/laboratorios/lab2-divide-y-vencer/`, una carpeta anidada. Debe estar en `lab2-divide-y-vencer/` o en `laboratorios/lab2-divide-y-vencer/` desde la raíz del repositorio.

## ¿El código funciona?
Sí. Las pruebas pasan, ambas soluciones coinciden con un resultado de referencia en listas aleatorias, y la medición corre completa y genera la gráfica.

## Para el próximo laboratorio
- Ubique la carpeta del laboratorio en la raíz del repositorio o dentro de `laboratorios/`, sin carpetas anidadas.
- Aclare que las estimaciones a gran escala son aproximadas y de qué datos salen.
- Mantenga commits pequeños y descriptivos, como ya lo hace.
