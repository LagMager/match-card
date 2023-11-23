import random
import pygame, thorpy

#Inicializar modulos
pygame.init()


# Variables
black = (0,0,0)
red = (255,0,0)
white = (255,255,255)
gray = (169,169,169)
ANCHO = 600
ALTO = 600
tablero_nuevo = True
carta_1 = 0
carta_2 = 0
sel_1 = False
sel_2 = False

#Lista
columnas = 6
filas = 6
puntaje = []
opciones = []
espacios = []
cartas_usadas = []

#Logica
screen = pygame.display.set_mode((ANCHO, ALTO), pygame.RESIZABLE)
pygame.display.set_caption("Match Card")
clock = pygame.time.Clock()
thorpy.set_default_font("arial", 20)
thorpy.init(screen, thorpy.theme_human)
small_font = pygame.font.Font("PixeloidSans.ttf", 26)

# Genera las listas de pares, y revisa si un par ya fue encontrado
def generar_tablero():
    global opciones
    global espacios
    global cartas_usadas
    for i in range(columnas * filas // 2):
        opciones.append(i)
    for i in range(columnas * filas):
        carta = opciones[random.randint(0, len(opciones) - 1)]
        espacios.append(carta)
        if carta in cartas_usadas:
            cartas_usadas.remove(carta)
            opciones.remove(carta)
        else:
            cartas_usadas.append(carta)

def dibujar_bg():
    top_menu = pygame.draw.rect(screen, black, [0,0,  ANCHO, 100])
    tablero = pygame.draw.rect(screen, gray, [0,100, ANCHO, ANCHO - 200], 0)
    bottom_menu = pygame.draw.rect(screen,black, [0, ALTO - 100, ANCHO, 100], 0)


def dibujar_cartas():
    global filas
    global columnas
    board_list = []
    for i in range(columnas):
        for j in range(filas):
            carta = pygame.draw.rect(screen, white, [i * 75 + 12, j * 65 + 112, 50, 50], 0, 4)
            board_list.append(carta)
            piece_text = small_font.render(f'{espacios[i * filas + j]}', True, gray)
            screen.blit(piece_text, (i * 75 + 20, j * 65 + 120))
    return board_list


running = True

while running:
    clock.tick(60) 
    screen.fill(white)

    if tablero_nuevo == True:
        generar_tablero()
        print(espacios)
        tablero_nuevo = False
    
    dibujar_bg()
    tablero = dibujar_cartas()
    #Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(tablero)):
                carta = tablero[i]
                if carta.collidepoint(event.pos) and not sel_1:
                    sel_1 = True
                    carta_1 = i
                    print(f'Se seleccionó la carta {espacios[carta_1]}')
                elif carta.collidepoint(event.pos) and sel_1 and not sel_2 and i != carta_1:
                    sel_2 = True
                    carta_2 = i
                    print(f'Se seleccionó la carta {espacios[carta_2]}')

    if sel_1 and sel_2:
        if espacios[carta_1] == espacios[carta_2]:
            print("¡Coinciden!")
        else:
            print("No coinciden")

        sel_1 = False
        sel_2 = False

    pygame.display.flip()

pygame.quit()
if sel_1 and sel_2:
    if espacios[carta_1] == espacios[carta_2]:
        print("Match!")
    else:
        print("No match!")
    sel_1 = False
    sel_2 = False


    pygame.display.flip()
pygame.quit()
