import pygame
from logica import MAPA_INICIAL, FILAS, COLUMNAS, META

TAMANO_CELDA = 15
ANCHO = COLUMNAS * TAMANO_CELDA
ALTO = FILAS * TAMANO_CELDA + 70

NEGRO = (30, 35, 45)
BLANCO = (245, 247, 250)
AZUL = (45, 120, 230)
ROJO = (230, 75, 75)
VERDE = (45, 180, 100)
GRIS = (190, 198, 208)
GRIS_TEXTO = (110, 118, 130)
VERDE_CLARO = (215, 243, 226)

ventana = None
reloj = None


def iniciar():
    global ventana, reloj
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Laberinto para dos jugadores")
    reloj = pygame.time.Clock()


def cerrar():
    pygame.quit()


def dibujar_juego(posicion_j1, posicion_j2, restante, mensaje):
    fuente = pygame.font.SysFont("Arial", 22, bold=True)
    fuente_pequena = pygame.font.SysFont("Arial", 17)

    ventana.fill(BLANCO)

    for fila in range(FILAS):
        for columna in range(COLUMNAS):
            x = columna * TAMANO_CELDA
            y = fila * TAMANO_CELDA
            if MAPA_INICIAL[fila][columna] == 1:
                color = NEGRO
            else:
                color = BLANCO
            pygame.draw.rect(ventana, color, (x, y, TAMANO_CELDA, TAMANO_CELDA))
            pygame.draw.rect(ventana, GRIS, (x, y, TAMANO_CELDA, TAMANO_CELDA), 1)


    mx = META[1] * TAMANO_CELDA
    my = META[0] * TAMANO_CELDA
    pygame.draw.rect(ventana, VERDE, (mx + 3, my + 3, TAMANO_CELDA - 6, TAMANO_CELDA - 6))

    x1 = posicion_j1[1] * TAMANO_CELDA + TAMANO_CELDA // 2
    y1 = posicion_j1[0] * TAMANO_CELDA + TAMANO_CELDA // 2
    pygame.draw.circle(ventana, AZUL, (x1, y1), TAMANO_CELDA // 3)

    x2 = posicion_j2[1] * TAMANO_CELDA + TAMANO_CELDA // 2
    y2 = posicion_j2[0] * TAMANO_CELDA + TAMANO_CELDA // 2
    pygame.draw.circle(ventana, ROJO, (x2, y2), TAMANO_CELDA // 3)

    barra_y = FILAS * TAMANO_CELDA
    pygame.draw.rect(ventana, (225, 230, 238), (0, barra_y, ANCHO, 70))

    segundos = int(restante)
    if segundos < 0:
        segundos = 0
    texto = fuente.render("Tiempo: " + str(segundos) + " s", True, NEGRO)
    ventana.blit(texto, (12, barra_y + 8))

    ayuda = fuente_pequena.render("Azul: W A S D | Rojo: flechas", True, NEGRO)
    ventana.blit(ayuda, (220, barra_y + 12))

    if mensaje != "":
        aviso = fuente.render(mensaje, True, VERDE)
        ventana.blit(aviso, (ANCHO // 2 - aviso.get_width() // 2, barra_y + 38))

    pygame.display.flip()
    reloj.tick(60)


def mostrar_ranking(ranking):
    fuente_titulo = pygame.font.SysFont("Arial", 30, bold=True)
    fuente_fila = pygame.font.SysFont("Arial", 21, bold=True)
    fuente_fecha = pygame.font.SysFont("Arial", 15)

    id_actual = 0
    if ranking is not None:
        for partida in ranking:
            if partida["id"] > id_actual:
                id_actual = partida["id"]

    seguir = True
    while seguir:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                seguir = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE or evento.key == pygame.K_RETURN:
                    seguir = False

        ventana.fill(BLANCO)

        titulo = fuente_titulo.render("RANKING DEL LABERINTO", True, NEGRO)
        ventana.blit(titulo, (ANCHO // 2 - titulo.get_width() // 2, 20))

        if ranking is None:
            aviso = fuente_fila.render("No se pudo generar el ranking.", True, ROJO)
            ventana.blit(aviso, (20, 100))
            aviso = fuente_fila.render("Compila cpp_datos (ver README).", True, ROJO)
            ventana.blit(aviso, (20, 130))
        elif len(ranking) == 0:
            aviso = fuente_fila.render("Todavía no hay partidas.", True, GRIS_TEXTO)
            ventana.blit(aviso, (20, 100))
        else:
            y = 75
            cantidad = 0
            for partida in ranking:
                if cantidad == 10:
                    break

               
                if partida["id"] == id_actual:
                    pygame.draw.rect(ventana, VERDE_CLARO, (10, y - 4, ANCHO - 20, 50))

                texto = str(partida["puesto"]) + ". Partida " + str(partida["id"])
                imagen = fuente_fila.render(texto, True, NEGRO)
                ventana.blit(imagen, (20, y))

                if partida["resultado"] == "JUGADOR 1":
                    nombre = "Jugador 1"
                    color = AZUL
                elif partida["resultado"] == "JUGADOR 2":
                    nombre = "Jugador 2"
                    color = ROJO
                elif partida["resultado"] == "EMPATE":
                    nombre = "Empate"
                    color = VERDE
                else:
                    nombre = "Sin ganador"
                    color = GRIS_TEXTO
                imagen = fuente_fila.render(nombre, True, color)
                ventana.blit(imagen, (230, y))

                if partida["resultado"] != "SIN GANADOR":
                    tiempo = str(round(partida["tiempo"], 2)) + " s"
                else:
                    tiempo = "-"
                imagen = fuente_fila.render(tiempo, True, NEGRO)
                ventana.blit(imagen, (ANCHO - 20 - imagen.get_width(), y))

                imagen = fuente_fecha.render(partida["fecha"], True, GRIS_TEXTO)
                ventana.blit(imagen, (20, y + 26))

                y = y + 52
                cantidad = cantidad + 1

        ayuda = fuente_fecha.render("Presiona ENTER o ESC para salir", True, GRIS_TEXTO)
        ventana.blit(ayuda, (ANCHO // 2 - ayuda.get_width() // 2, ALTO - 25))

        pygame.display.flip()
        reloj.tick(30)
