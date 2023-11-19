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

#Lista
col = 6
filas = 6
puntaje = []
pares = []
espacios = []
cartas_usadas = []
screen = pygame.display.set_mode((ANCHO, ALTO), pygame.RESIZABLE)
pygame.display.set_caption("Match Card")
clock = pygame.time.Clock()
thorpy.set_default_font("arial", 20)
thorpy.init(screen, thorpy.theme_human)

# Genera las listas de la tabla y revisa si un par ya ha sido encontrado
def generar_tablero():
    global pares
    global espacios
    global cartas_usadas
    for i in range(col * filas // 2):
        pares.append(i)
    for i in range(col * filas):
        carta = pares[random.randint(0, len(pares) - 1)]
        espacios.append(carta)
        if carta in cartas_usadas:
            cartas_usadas.remove(carta)
            pares.remove(carta)
        else:
            cartas_usadas.append(carta)

def dibujar_bg():
    top_menu = pygame.draw.rect(screen, black, [0,0,  ANCHO, 100])
    tablero = pygame.draw.rect(screen, gray, [0,100, ANCHO, ANCHO - 200], 0)
    bottom_menu = pygame.draw.rect(screen,black, [0, ALTO - 100, ANCHO, 100], 0)


def dibujar_cartas():

    board_list = []
    for i in range(col):
        for j in range(filas):
            carta = pygame.draw.rect(screen, white, [i * 75 + 75, j* 65 + 112, 50, 50], 0,4)
            board_list.append(carta)
    
    return board_list


running = True

while running:
    clock.tick(60) 
    screen.fill(white)
    dibujar_bg()
    dibujar_cartas()

    if tablero_nuevo == True:
        generar_tablero()
        print(espacios)
        tablero_nuevo = False
    #Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

   # if pygame.mouse.get_pressed()[0]:
   #     square = pygame.draw.rect(screen, black, (x,y, 100,100))

    pygame.display.flip()
pygame.quit()