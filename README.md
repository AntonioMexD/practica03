# El Problema de los pacíficos y verdugos
# Autores
- Jesus Ricardo Pelaez Sarabia
- Jhoselin Solangel Quiroga Quispe
- Antonio Medina Padilla
## Docente
Msc. Lic. Víctor Rodríguez Estévez

## Resumen
Este trabajo explora la resolución del problema de los pacíficos y verdugos utilizando los algoritmos de búsqueda no informada (DFS) y A*. Se implementa un agente que evalúa la eficacia de ambos métodos en encontrar soluciones válidas para el problema de transferencia segura a través de un río.
## Introducción
El problema de los pacíficos y verdugos es un clásico de la teoría de búsqueda en inteligencia artificial. En este problema, un grupo de pacíficos (misioneros o mapus) y verdugos (caníbales) deben cruzar un río utilizando un bote que solo puede llevar hasta dos personas a la vez. La condición crucial es que en cualquier momento, en ninguna de las dos orillas del río, el número de verdugos debe ser mayor que el número de pacíficos, para evitar que los pacíficos sean devorados.
El objetivo de este trabajo es implementar y comparar dos métodos de búsqueda para resolver este problema: búsqueda en profundidad (DFS) y búsqueda A*. La búsqueda en profundidad explora los estados de manera exhaustiva y es útil para problemas con soluciones que se encuentran en la profundidad del árbol de búsqueda. Por otro lado, la búsqueda A* utiliza una heurística para guiar la búsqueda de manera más eficiente, reduciendo el espacio de búsqueda al priorizar los caminos que parecen más prometedores.
En este trabajo, se planea:
Implementar el algoritmo DFS para explorar las posibles soluciones al problema y analizar su eficiencia en términos de profundidad y nodos explorados.
Implementar el algoritmo A* utilizando una heurística adecuada para mejorar la eficiencia de la búsqueda y comparar su rendimiento con el de DFS.
Evaluar y comparar los resultados obtenidos con ambos algoritmos para determinar cuál es más efectivo en la resolución del problema de los pacíficos y verdugos.
El enfoque permitirá entender mejor las capacidades y limitaciones de ambos métodos en la resolución de problemas complejos de búsqueda.

## Fundamentación teórica
En el campo de la inteligencia artificial (IA), la resolución de problemas mediante agentes de búsqueda es una técnica fundamental. Un agente de búsqueda se define como un sistema que recorre un espacio de estados, explorando diferentes posibilidades hasta encontrar una solución que satisfaga las condiciones establecidas en un problema. En este contexto, los agentes de búsqueda pueden utilizar diversos algoritmos, los cuales se clasifican en informados y no informados, dependiendo del conocimiento adicional que utilicen para guiar la búsqueda hacia el objetivo (Russell & Norvig, 2020).
La búsqueda no informada se caracteriza por no utilizar ninguna información específica sobre la cercanía al objetivo. Esto implica que los algoritmos exploran el espacio de búsqueda de manera exhaustiva, sin dirección o indicio de qué caminos son más prometedores. Entre los algoritmos de búsqueda no informada más comunes se encuentra la búsqueda en profundidad (DFS). DFS es un algoritmo que explora los caminos en el espacio de estados tan profundamente como sea posible antes de retroceder y probar caminos alternativos. Este método es útil en situaciones donde la solución está ubicada en una rama profunda del árbol de búsqueda, aunque puede ser ineficiente si el espacio de búsqueda es muy grande o contiene ciclos, ya que DFS podría revisitar estados previamente explorados sin encontrar una solución (Russell & Norvig, 2020).
El uso de DFS en el problema de los pacíficos y verdugos, una variante del problema de los misioneros y caníbales, es un ejemplo clásico de cómo los algoritmos de búsqueda no informada pueden ser aplicados en la práctica. En este problema, un grupo de pacíficos y verdugos debe cruzar un río utilizando un bote que solo puede llevar hasta dos personas a la vez, con la restricción de que en ningún momento debe haber más verdugos que pacíficos en cualquier orilla. DFS es adecuado para explorar las múltiples combinaciones posibles, aunque su eficiencia depende en gran medida de cómo se estructure el espacio de búsqueda y cómo se representan los estados del problema.
Teoría de la representación de problemas
La representación de problemas es un componente crítico en la resolución de problemas mediante agentes de búsqueda. La representación efectiva de un problema incluye la definición clara de los estados, las acciones disponibles, las transiciones entre estados y los estados objetivos. En el caso de los pacíficos y verdugos, un estado puede representarse como una tupla de valores que indica el número de pacíficos y verdugos en la orilla izquierda del río y la posición del bote. Las acciones disponibles incluyen las posibles combinaciones de personas que pueden cruzar el río en el bote, mientras que las transiciones reflejan el cambio en el estado del problema después de cada acción realizada (Russell & Norvig, 2020).
Una representación bien diseñada del problema permite que el agente de búsqueda explore el espacio de estados de manera eficiente, evitando la generación de estados redundantes o inválidos. En el caso de DFS, donde el agente no tiene una guía heurística para dirigirse al objetivo, la representación del problema juega un papel crucial para reducir la cantidad de estados que necesitan ser explorados. Esto se logra definiendo restricciones que eliminen estados no válidos, como aquellos donde los verdugos superan en número a los pacíficos en una orilla, lo que ayuda a evitar la expansión innecesaria del árbol de búsqueda.
La búsqueda no informada, como DFS, es adecuada para problemas donde la solución no requiere una evaluación constante del costo del camino o cuando no se dispone de una heurística adecuada. Sin embargo, su éxito y eficiencia dependen en gran medida de la calidad de la representación del problema, lo que subraya la importancia de una buena abstracción y modelado del espacio de estados (Russell & Norvig, 2020).

## Metodología
El desarrollo del agente para resolver el problema de los pacíficos y verdugos implicó varios pasos clave, organizados en fases para garantizar una implementación eficiente y efectiva. A continuación, se describen los pasos realizados, las mejoras aplicadas al código, y la estructura general del proyecto.
Definición del Problema y Representación de Estados
Identificación de Estados y Acciones: El primer paso fue definir cómo representar cada estado del problema, donde un estado está compuesto por el número de pacíficos y verdugos en la orilla izquierda del río y la posición del bote (orilla izquierda o derecha). Las acciones posibles incluyen las combinaciones de personas que pueden cruzar el río en el bote, respetando la capacidad máxima del mismo.
Restricciones: Se establecieron las restricciones clave del problema, como la regla de que en ninguna orilla puede haber más verdugos que pacíficos, a menos que no haya pacíficos presentes. Esto fue crucial para evitar estados no válidos.
Implementación de la Búsqueda en Profundidad (DFS)
Exploración del Espacio de Estados: Se implementó un algoritmo de búsqueda en profundidad (DFS) para explorar el espacio de estados, buscando una secuencia de acciones que lleve desde el estado inicial al estado meta, donde todos los pacíficos y verdugos han cruzado el río.
Manejo de Ciclos y Estados Repetidos: Se implementaron mecanismos para evitar la expansión de ciclos y la repetición de estados ya visitados, lo que ayudó a reducir el tiempo de ejecución y el consumo de memoria.
Implementación de la Búsqueda A*
Definición de la Heurística: Se desarrolló una función heurística para la búsqueda A*, la cual estima el número total de movimientos restantes necesarios para trasladar a todos los pacíficos y verdugos al otro lado del río. La heurística se diseñó para ser admisible, garantizando que nunca sobreestima el costo real hasta el objetivo.
Optimización de la Búsqueda: La búsqueda A* Fue implementada para priorizar los estados con menor costo estimado total (suma del costo hasta el estado actual más la heurística). Esto permitió encontrar soluciones más rápidamente en comparación con DFS.
Evaluación de los Algoritmos
Comparación de Resultados: Se ejecutaron ambos algoritmos (DFS y A*) en el mismo conjunto de problemas, y se compararon en términos de número de nodos explorados, tiempo de ejecución y calidad de la solución. A* demostró ser más eficiente al encontrar soluciones con menos exploración de nodos, gracias a la guía de la heurística.
Análisis de Rendimiento: Se realizaron pruebas con diferentes configuraciones del problema (variando el número de pacíficos y verdugos) para analizar cómo cada algoritmo se comportaba en términos de eficiencia y escalabilidad.
Mejoras y Optimización
Validación de Estados: Se mejoró la función que valida los estados, asegurando que solo se expandan estados válidos, lo que evitó la generación de caminos inválidos.
Refinamiento de la Heurística: Se ajustó la heurística utilizada en A* para mejorar la precisión y reducir el número de estados explorados innecesariamente. Esto implicó pruebas iterativas y ajustes basados en el rendimiento observado.
Manejo de la Memoria: Se optimizó el manejo de memoria, especialmente en DFS, donde se garantizó que los estados se almacenarán de manera eficiente, evitando desbordamientos de la pila en problemas de gran profundidad.
Diagrama de flujo
Para visualizar los procesos de búsqueda en DFS y A*, ayudando a entender las diferencias en sus estrategias de exploración.

<img width="628" alt="Captura de pantalla 2024-09-01 a la(s) 9 28 46 p  m" src="https://github.com/user-attachments/assets/4753738e-7770-41af-8f40-2a100ec9bee6">

## Resultados

<img width="620" alt="Captura de pantalla 2024-09-01 a la(s) 9 30 46 p  m" src="https://github.com/user-attachments/assets/78bea4a0-52a7-4987-be19-899af93bfa6f">

## Discusión
Al comparar los resultados obtenidos con los algoritmos de búsqueda en profundidad (DFS) y búsqueda A* para resolver el problema de los pacíficos y verdugos, se observa que ambos algoritmos encontraron la misma solución. La secuencia de estados visitados en ambas búsquedas es idéntica, lo que sugiere que, en este caso particular, tanto DFS como A* fueron capaces de explorar el espacio de búsqueda de manera efectiva y llegar al mismo resultado.
Eficiencia de Búsqueda
A pesar de que los resultados son equivalentes en términos de la solución encontrada, los dos algoritmos difieren significativamente en su enfoque y eficiencia.
DFS: Este algoritmo explora un camino hasta el final antes de retroceder y probar caminos alternativos. Si bien DFS es eficaz para encontrar soluciones en problemas donde la solución está en una rama profunda del árbol, no es óptimo en términos de tiempo y recursos en problemas donde el espacio de estados es grande o existen muchos caminos posibles. En este caso, DFS funcionó adecuadamente, pero en problemas más complejos o con un espacio de búsqueda más amplio, podría haber explorado muchas ramas inútiles antes de encontrar la solución.
A*: A diferencia de DFS, A utiliza una heurística para guiar la búsqueda hacia la solución de manera más eficiente. En el problema de los pacíficos y verdugos, A* logró encontrar la misma solución que DFS, pero lo hizo de manera más dirigida, evitando la exploración innecesaria de ramas poco prometedoras. La función heurística utilizada en A* permitió priorizar los estados que parecían más cercanos al objetivo, lo que generalmente resulta en una búsqueda más rápida y con menos nodos explorados.
Comparación de Rendimiento
Consumo de Memoria: DFS tiende a consumir menos memoria que A*, ya que solo almacena los nodos en el camino actual y retrocede cuando es necesario. Sin embargo, A*, aunque consume más memoria debido al almacenamiento de todos los nodos en la frontera de búsqueda (frontera de prioridad), es más eficiente en evitar caminos inútiles y en asegurar que se expanda el camino óptimo.
Velocidad de Búsqueda: En este caso, ambos algoritmos llegaron a la solución con la misma secuencia de movimientos, pero en general, A* es más rápido en encontrar soluciones, especialmente en problemas más complejos, gracias a su heurística que guía la búsqueda de manera más informada.
Referencias
Russell, S., & Norvig, P. (2020). Artificial Intelligence: A Modern Approach (4th ed.). Pearson.
Calificación y Fecha de entrega
Evaluando el proceso : Estrategia de pensamiento metacognitiva: "Identificar y corregir errores". Piensa si la práctica te ha emocionado y crees que tiene utilidad para tu aprendizaje.
Para ello califica de 1 a 5 la práctica:
1. Nada 2. Regular 3. Ni mucho ni poco 4. Mucho 5. Bastante
"Reconocer lo que no se ha hecho bien o lo que falta". Si has puntuado 3 o menos, indícame qué crees que tengo que cambiar en el diseño de la práctica para mejorar.
"La educación no sólo se genera dentro del espacio escolar, también se debe, proporcionar herramientas de educación en el hogar, como Ing. de Sistemas, también esta en nuestras manos ayudar en estas herramientas, empecemos a pensar en la Inteligencia Artificial, para el desarrollo integral de la humanidad...."
## Conclusiones
Contrastar lo estudiado en la teoría y lo experimentado en la práctica.
Consistencia con la Teoría: La implementación práctica sigue de cerca los conceptos teóricos presentados. La clase AgenteMapu define un espacio de estados, una función sucesor, un estado inicial y un estado objetivo, como se sugiere en la teoría.

Aplicación de Algoritmos: Ambos algoritmos de búsqueda (DFS y A*) se utilizan de acuerdo con sus características teóricas: DFS explora en profundidad sin garantizar la mejor solución, mientras que A* usa una heurística para encontrar una solución más eficiente en términos de costos.

Diferencias Prácticas: Aunque la teoría menciona que DFS puede no ser completo si la profundidad del árbol es infinita, en la práctica, la implementación de buscar_profundidad sigue siendo completa dado que el problema es finito y tiene un espacio de estados limitado.

Validez de la Heurística: La heurística utilizada en A* Es simple pero válida, ya que representa el número de personas restantes que deben cruzar el río, alineándose con la teoría de que una heurística adecuada debe guiar al agente hacia el objetivo.


