import pygame
import time
from logica import (INICIO_J1, INICIO_J2, mover_jugador,
                    comprobar_resultado, guardar_resultado, obtener_ranking)
import interfaz

DURACION_PARTIDA = 120   
PAUSA_FINAL = 2          
NOMBRE_J1 = "Jugador 1"
NOMBRE_J2 = "Jugador 2"


def jugar():
    interfaz.iniciar()

    posicion_j1 = INICIO_J1
    posicion_j2 = INICIO_J2
    inicio = time.time()
    resultado = None
    tiempo_final = 0
    momento_fin = 0
    jugando = True
    cerro_ventana = False

    while jugando:
        if resultado is None:
            transcurrido = time.time() - inicio
        else:
            transcurrido = tiempo_final
        restante = DURACION_PARTIDA - transcurrido

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                jugando = False
                cerro_ventana = True

            if evento.type == pygame.KEYDOWN and resultado is None:
                if evento.key == pygame.K_UP:
                    posicion_j1 = mover_jugador(posicion_j1, (-1, 0), posicion_j2)
                if evento.key == pygame.K_DOWN:
                    posicion_j1 = mover_jugador(posicion_j1, (1, 0), posicion_j2)
                if evento.key == pygame.K_LEFT:
                    posicion_j1 = mover_jugador(posicion_j1, (0, -1), posicion_j2)
                if evento.key == pygame.K_RIGHT:
                    posicion_j1 = mover_jugador(posicion_j1, (0, 1), posicion_j2)

                if evento.key == pygame.K_w:
                    posicion_j2 = mover_jugador(posicion_j2, (-1, 0), posicion_j1)
                if evento.key == pygame.K_s:
                    posicion_j2 = mover_jugador(posicion_j2, (1, 0), posicion_j1)
                if evento.key == pygame.K_a:
                    posicion_j2 = mover_jugador(posicion_j2, (0, -1), posicion_j1)
                if evento.key == pygame.K_d:
                    posicion_j2 = mover_jugador(posicion_j2, (0, 1), posicion_j1)


        if resultado is None:
            resultado = comprobar_resultado(posicion_j1, posicion_j2)

            if resultado is not None:
                tiempo_final = transcurrido
            elif restante <= 0:
                resultado = "EMPATE"
                tiempo_final = DURACION_PARTIDA

            if resultado is not None:
                guardar_resultado(NOMBRE_J1, NOMBRE_J2, resultado,
                                  tiempo_final, DURACION_PARTIDA)
                momento_fin = time.time()

        if resultado is None:
            mensaje = ""
        else:
            mensaje = resultado

        interfaz.dibujar_juego(posicion_j1, posicion_j2, restante, mensaje)


        if resultado is not None:
            if time.time() - momento_fin >= PAUSA_FINAL:
                jugando = False

    if resultado is not None and not cerro_ventana:
        ranking = obtener_ranking()
        interfaz.mostrar_ranking(ranking)

    interfaz.cerrar()


jugar()
