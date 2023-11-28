import thorpy

def dificultad_facil():
    global columnas, filas
    columnas = 4
    filas = 4

def dificultad_normal():
    global columnas, filas
    columnas = 6
    filas = 6

def dificultad_dificil():
    global columnas, filas
    columnas = 8
    filas = 8

def iniciar_juego():
    global tablero_nuevo
    tablero_nuevo = True