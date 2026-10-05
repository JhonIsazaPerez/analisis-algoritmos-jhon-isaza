# Retroalimentación — Laboratorio 01: Fundamentos, complejidad y recurrencias

**Estudiante:** Jhon Alejandro Isaza Pérez · **Laboratorio:** Plataforma Tamiza — ordenamiento de 1.200.000 registros
**Fecha límite:** 2026-10-04 23:59 · **Versión revisada:** commit `55c112f`

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 13 / 25 |
| Calidad de la explicación teórica | 21 / 25 |
| Corrección de la implementación | 18 / 20 |
| Calidad del análisis de las gráficas | 12 / 20 |
| Documentación y organización del informe | 5 / 10 |
| **Total** | **69 / 100** |
| **Nota (0–5)** | **3.45** |

## 1. Corrección conceptual (13 / 25)
**Lo que hizo bien:**
- Distingue entre resultado correcto y resultado a tiempo, y nombra la ventana nocturna como la restricción que se incumple.
- Explica que un servidor el doble de rápido solo divide el tiempo por dos, pero no cambia cómo crece el trabajo.
- Da un segundo ejemplo propio (la app de cotizaciones) con cantidad de datos y límite de tiempo.
- Relaciona el tiempo de ejecución con el gasto de energía repetido cada noche.

**Lo que puede mejorar:**
- En la Parte 1 aparecen datos de otro caso ("lista de reabastecimiento", "líneas de venta", 450.000 líneas) que no son de Tamiza. Revise que cada respuesta hable del caso que se pide.
- En la Parte 2 faltan al menos dos perjuicios concretos a personas identificables: solo menciona de forma general que un paciente de alto riesgo podría quedar sin llamar.
- No responde con claridad quién asume el costo del error; deja la pregunta abierta.
- No desarrolla la obligación especial que impone que el orden de la lista decida a quién se llama primero.
- La Parte 2 tiene frases confusas que cuesta seguir; vale la pena releerla y ordenarla.

## 2. Calidad de la explicación teórica (21 / 25)
**Lo que hizo bien:**
- Define mejor, peor y promedio indicando sobre qué se toma el mínimo, el máximo y el promedio, y justifica usar el peor caso por la ventana estricta.
- Plantea la recurrencia de merge sort explicando cada término y la resuelve con el método maestro, verificando la condición del caso 2.
- Hace el cálculo línea a línea de insertion sort para los tres casos y presenta la tabla de complejidades.

**Lo que puede mejorar:**
- La predicción de 3.1 se contradice: dice que A (aleatorio) sería el mejor caso "porque los datos ya están ordenados", pero A no está ordenado. Léala con calma antes de dejarla escrita.
- Faltó declarar el sentido del orden. Tamiza necesita de mayor a menor riesgo, y su laboratorio ordena de menor a mayor sin decirlo.

## 3. Corrección de la implementación (18 / 20)
**Lo que hizo bien:**
- `insertion_sort` y `merge_sort` ordenan bien los tres escenarios, no cambian la lista recibida y cuentan solo comparaciones entre elementos.
- No usa `sorted()` ni `list.sort()`; la mezcla de merge sort es propia y recursiva.
- Los generadores producen listas del tamaño pedido, sin repetidos, con semilla; el 2 % del escenario B queda al final.
- Tiene docstrings y type hints, y el código sigue el estilo PEP 8.

**Lo que puede mejorar:**
- Las funciones auxiliares tienen docstring más corto que el estilo Google completo (sin `Args`).
- Cada tiempo se midió una sola vez; repetir la medición y promediar da curvas más estables.

## 4. Calidad del análisis de las gráficas (12 / 20)
**Lo que hizo bien:**
- Las tres gráficas existen, tienen título, ejes rotulados, leyenda y están incrustadas en el informe.
- Identifica con datos que C es el peor caso, B el mejor y A se parece al promedio, y contrasta con su predicción.
- En 4.2 describe lo que hace cada curva y verifica que coincide con Θ(n²) y Θ(n log n).

**Lo que puede mejorar:**
- El concepto técnico de 4.3 es demasiado corto (pedía entre 400 y 600 palabras) y no tiene el desarrollo esperado.
- No hay extrapolación a 1.200.000 registros: solo dice que "cabe con margen". Faltan el razonamiento, los números estimados para cada algoritmo y declarar que es una estimación.
- No discute ninguna consideración distinta del tiempo (memoria extra de merge sort, estabilidad, mantenimiento).
- Dice "más de 40 veces" sin indicar de dónde sale; cite la gráfica y el tamaño concreto.
- En el análisis de la Parte 3 las gráficas de comparaciones y tiempo no se comentan una por una.

## 5. Documentación y organización del informe (5 / 10)
**Lo que hizo bien:**
- El informe está ordenado por partes, con instrucciones para reproducir y enlaces a `parte3_casos.py`, `parte4_complejidad.py`, `algoritmos.py` y `datos.py`.
- Tiene más de cinco commits descriptivos del laboratorio.

**Lo que puede mejorar:**
- No siguió la estructura de carpetas acordada: el laboratorio quedó dentro de una carpeta `curso-analisis-algoritmos/` en vez de estar en la raíz del repositorio o en `laboratorios/`.
- Quedaron además carpetas vacías de otros temas (`benchmarks`, `laboratorios`) dentro de esa carpeta anidada.

## ¿El código funciona?
Sí. Los dos scripts corren sin errores, ordenan correctamente los tres escenarios y generan las tres gráficas.

## Para el próximo laboratorio
- Ubicar la carpeta del laboratorio en la raíz del repositorio o en `laboratorios/`, con el nombre acordado.
- Revisar que cada respuesta hable del caso del enunciado y que responda cada pregunta puntual (quién asume el costo, qué obligación impone el orden).
- Declarar desde el inicio el sentido del ordenamiento y mantenerlo en las predicciones.
- Escribir el concepto técnico completo: recomendación, estimación a 1.200.000 registros declarada como estimación y una consideración más allá del tiempo.
- Repetir las mediciones varias veces y promediarlas.
