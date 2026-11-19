import os
import subprocess
from datetime import datetime

RUTA = os.path.dirname(os.path.abspath(__file__))
ARCHIVO_HISTORIAL = os.path.join(RUTA, "historial.csv")
CARPETA_CPP = os.path.join(RUTA, "..", "cpp_datos")

MAPA_INICIAL = [
    [3,4,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
    [0,1,0,1,0,1,0,1,1,1,0,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,1,1,0],
    [0,1,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0,1,0,1,0,1,0],
    [0,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,0,1,0,1,0,1,0,1,0],
    [0,1,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0,1,0],
    [0,1,0,1,1,1,0,1,1,1,0,1,1,1,1,1,0,1,0,1,1,1,1,1,0,1,0,1,0,1,1,1,1,1,0,1,0,1,0],
    [0,1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,1,0,0,0,1,0,0,0,1,0,1,0],
    [0,1,1,1,0,1,1,1,1,1,1,1,0,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,0,1,1,1,0,1,0],
    [0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0],
    [0,1,0,1,1,1,1,1,1,1,0,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,1,1,0,1,0,1,0,1,1,1,1],
    [0,1,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,1,0,0,0],
    [1,1,0,1,0,1,0,1,1,1,1,1,1,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1,0,1,0],
    [0,0,0,1,0,1,0,0,0,1,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0],
    [0,1,1,1,1,1,1,1,0,1,0,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,0,0,1,0,1,0],
    [1,1,1,1,1,1,0,1,1,1,1,1,0,0,1,1,0,1,1,1,0,1,0,1,0,1,1,1,1,1,1,1,0,1,0,1,0,1,0],
    [0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,1,0,1,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0],
    [0,1,1,1,0,1,1,1,0,1,1,1,1,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1,0,1,1],
    [0,1,0,0,0,1,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,1,0],
    [0,1,0,1,0,1,0,1,1,1,0,1,0,1,1,1,0,1,1,1,1,1,0,1,1,1,0,1,0,1,0,1,0,1,1,1,0,1,0],
    [0,0,0,1,0,1,0,0,0,0,0,1,0,0,0,1,0,1,0,0,0,1,0,0,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,0,1,0,1,1,1,0],
    [0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0,1,0,1,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0],
    [1,0,1,1,0,1,1,1,1,1,1,1,0,1,0,1,1,1,1,1,0,1,0,1,1,1,1,1,0,1,0,1,1,1,1,1,0,1,1],
    [0,0,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,1,0],
    [0,1,0,1,1,1,1,1,1,1,0,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,0,1,1,1,1,1,0,1,0,1,0],
    [0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0,0,0],
    [0,1,1,1,0,1,0,1,0,1,1,1,0,1,0,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,1],
    [0,0,0,1,0,1,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,1,0,1,1,1,0,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0],
    [0,1,0,0,0,1,0,1,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,1,0],
    [0,1,1,1,0,1,0,1,1,1,0,1,1,1,0,1,0,1,0,1,1,1,1,1,1,1,0,1,0,1,0,1,1,1,1,1,0,1,1],
    [0,1,0,0,0,1,0,0,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0,1,0,0,0,1,0,1,0,1,0,0,0,1,0,0,0],
    [0,1,0,1,0,1,1,1,0,1,0,1,0,1,0,1,1,1,0,1,0,1,0,1,0,1,1,1,0,1,0,1,0,1,0,1,1,1,0],
    [0,1,0,1,0,0,0,1,0,0,0,1,0,1,0,0,0,1,0,0,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0,1,0,1,0],
    [0,1,0,1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,0,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0],
    [0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0],
    [0,1,0,1,0,1,0,1,0,1,0,1,1,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,0],
    [0,1,0,0,0,1,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5],
]

FILAS = len(MAPA_INICIAL)
COLUMNAS = len(MAPA_INICIAL[0])
INICIO_J1 = (0, 0)
INICIO_J2 = (0, 1)
META = (38, 38)


def es_transitable(fila, columna):
    if fila < 0 or fila >= FILAS:
        return False
    if columna < 0 or columna >= COLUMNAS:
        return False
    if MAPA_INICIAL[fila][columna] == 1:
        return False
    return True


def mover_jugador(posicion, movimiento, otra_posicion):
    nueva_fila = posicion[0] + movimiento[0]
    nueva_columna = posicion[1] + movimiento[1]
    nueva_posicion = (nueva_fila, nueva_columna)

    if not es_transitable(nueva_fila, nueva_columna):
            return posicion

    if nueva_posicion == otra_posicion and nueva_posicion != META:
        return posicion

    return nueva_posicion


def comprobar_resultado(posicion_j1, posicion_j2):
    j1_llego = (posicion_j1 == META)
    j2_llego = (posicion_j2 == META)

    if j1_llego and j2_llego:
        return "EMPATE"
    if j1_llego:
        return "JUGADOR 1"
    if j2_llego:
        return "JUGADOR 2"
    return None


def guardar_resultado(jugador1, jugador2, resultado, tiempo, limite):
    archivo_nuevo = (not os.path.exists(ARCHIVO_HISTORIAL)
                     or os.path.getsize(ARCHIVO_HISTORIAL) == 0)

    archivo = open(ARCHIVO_HISTORIAL, "a", encoding="utf-8")

    if archivo_nuevo:
        archivo.write("fecha,jugador1,jugador2,resultado,tiempo_segundos,limite_segundos\n")

    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    linea = fecha + "," + jugador1 + "," + jugador2 + "," + resultado + ","
    linea = linea + str(round(tiempo, 2)) + "," + str(limite) + "\n"
    archivo.write(linea)
    archivo.close()


def obtener_ranking():
    programa = os.path.join(CARPETA_CPP, "ranking.exe")
    if not os.path.exists(programa):
        programa = os.path.join(CARPETA_CPP, "ranking")
    if not os.path.exists(programa):
        return None

    try:
        salida = subprocess.run([programa, ARCHIVO_HISTORIAL],
                                capture_output=True, text=True)
    except OSError:
        return None

    ranking = []
    for linea in salida.stdout.splitlines():
        partes = linea.strip().split("|")
        if len(partes) == 5:
            partida = {
                "puesto": int(partes[0]),
                "id": int(partes[1]),
                "resultado": partes[2],
                "tiempo": float(partes[3]),
                "fecha": partes[4],
            }
            ranking.append(partida)
    return ranking
