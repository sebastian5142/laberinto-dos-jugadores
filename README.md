# Laberinto para dos jugadores

## Descripción
Juego local para dos personas en el mismo computador. Cada jugador recorre un laberinto de 39x39, evita las paredes y trata de llegar a la meta antes que el otro. La partida tiene un límite de 120 segundos. Al terminar, el programa en C++ calcula el ranking y se muestra en una ventana.

## Requisitos
- Python 3
- Pygame (`python -m pip install pygame`)
- Compilador de C++ (g++) compatible con C++11 o superior

## Estructura
```
ProyectoJuego/
├── python_juego/
│   ├── juego.py        (programa principal, controles y cronómetro)
│   ├── interfaz.py     (ventanas y eventos con Pygame)
│   ├── logica.py       (mapa, movimientos, resultado y guardado del CSV)
│   └── historial.csv   (partidas guardadas)
├── cpp_datos/
│   ├── main.cpp        (lee el CSV y arma la lista enlazada)
│   ├── ranking.cpp     (ordena la lista y genera el ranking)
│   └── nodo.h          (estructuras Resultado y Nodo)
├── LICENSE
└── README.md
```

## Ejecución
1. Abrir una terminal dentro de la carpeta `cpp_datos` y compilar (solo una vez, o cada vez que se cambie el código C++):
   - Windows: `g++ -std=c++11 main.cpp ranking.cpp -o ranking.exe`
   - Linux/macOS: `g++ -std=c++11 main.cpp ranking.cpp -o ranking`
2. Abrir una terminal dentro de la carpeta `python_juego` y ejecutar: `python juego.py`
3. Controles: el Jugador 1 (azul) usa las flechas; el Jugador 2 (rojo) usa W, A, S y D.
4. Cuando un jugador llega a la meta (o se acaba el tiempo), la partida se guarda en `historial.csv` y aparece el ranking. Se cierra con ENTER o ESC.

## Cómo se comunican Python y C++
Python guarda cada partida en `historial.csv`. Al terminar, Python ejecuta el programa de C++, que lee ese archivo, arma una lista enlazada, la ordena y escribe el resultado. Python lee esa respuesta y la dibuja en la ventana.

## Formato del CSV
`fecha,jugador1,jugador2,resultado,tiempo_segundos,limite_segundos`

El resultado es `JUGADOR 1`, `JUGADOR 2` o `EMPATE`. Cada fila es una partida y su número de partida es el orden en que aparece en el archivo.

## Criterios del ranking
Primero van las partidas con ganador, ordenadas de menor a mayor tiempo de llegada. Al final quedan las partidas sin ganador (empate por tiempo). Para cada partida se muestra el número de partida, el ganador, el tiempo de llegada y la fecha.

## Dependencias y créditos
- Python: lenguaje del juego.
- Pygame: biblioteca externa para ventana, eventos y gráficos. Sitio: https://www.pygame.org/
- C++ estándar: lectura de archivos, lista enlazada y ordenamiento.
- Herramientas de IA: se usó Claude (Anthropic) como apoyo para escribir y corregir el código base. El equipo lo revisó, lo probó y es responsable de su contenido. (Ajustar este texto según el trabajo real del equipo y las reglas de la institución.)

## Integrantes y responsabilidades
- Sebastián: lógica e interfaz gráfica (`logica.py`, `interfaz.py`, `juego.py`) e integración de módulos.
- Cristian: `ranking.cpp`, README, licencia y documentación de conflictos.
- Mateo: `main.cpp`, `nodo.h`, `historial.csv` y lista enlazada.
