import random
import pygame
import thorpy
import os

# Variables
BLACK, RED, WHITE, GRAY = (0,0,0), (255,0,0), (255,255,255), (169,169,169)
ANCHO, ALTO = 600, 600
columnas, filas = 6, 6

images_folder = "Cards"
image_files = [f for f in os.listdir(images_folder) if f.endswith(".png")]
images = [pygame.image.load(os.path.join(images_folder, img)) for img in image_files]

card_back_image = pygame.image.load(os.path.join(images_folder, "card_back.png"))

paired_images = images * 2
random.shuffle(paired_images)

#Inicializando Pygame
pygame.init()
screen = pygame.display.set_mode((ANCHO, ALTO), pygame.RESIZABLE)
pygame.display.set_caption("Encuentra pares")
clock = pygame.time.Clock()
small_font = pygame.font.Font("PixeloidSans.ttf", 26)

#Inicializando Thorpy
thorpy.init(screen, thorpy.themes.theme_human)
bg_gif = "Background.gif"
bg_anim = thorpy.AnimatedGif(bg_gif, frame_mod=2)
bg_anim.center_on(screen)
boton_empezar = thorpy.Button("Empezar")
boton_puntajes = thorpy.Button("Clasificaciones")
boton_salir = thorpy.Button("Salir")
Botones = thorpy.Group([boton_empezar, boton_puntajes,boton_salir])
Botones.center_on(screen)
menugroup = thorpy.Group([bg_anim, Botones], None)
updater = menugroup.get_updater()

boton_facil = thorpy.Button("Facil")
boton_normal = thorpy.Button("Normal")
boton_dificil = thorpy.Button("Dificil")

DifBotones = thorpy.Group([boton_facil, boton_normal, boton_dificil], "h")
DifBotones.center_on(screen)
DifBotonesUpdater = DifBotones.get_updater()

#Game State
running = True
game_state = "menu"
game_state_value = 0
tablero_nuevo = True
carta_1, carta_2 = 0, 0
sel_1, sel_2 = False, False

#Listas
opciones, espacios, cartas_usadas = [], [], []
cartas_correctas = [[False] * filas for _ in range(columnas)]

def change_game_state(game_state_value):
    global game_state
    if game_state_value == 0:
        game_state = "menu"
    elif game_state_value == 1:
        game_state = "dificultad"
    elif game_state_value == 2:
        game_state = "game"

def before_gui():
    screen.fill(WHITE)

def change_difficulty(difficulty : int):
    global columnas, filas, game_state
    if difficulty == 1:
        columnas, filas = 4,4
        game_state = "game"
    elif difficulty == 2:
        columnas, filas = 6,6
        game_state = "game"
    elif difficulty == 3:
        columnas, filas = 8,8
        game_state = "game"

def generar_tablero():
    global opciones, espacios, cartas_usadas
    for i in range(columnas * filas // 2):
        opciones.append(i)
    for i in range(columnas * filas):
        carta = opciones[random.randint(0, len(opciones)-1)]
        espacios.append(carta)
        if carta in cartas_usadas:
            cartas_usadas.remove(carta)
            opciones.remove(carta)
        else:
            cartas_usadas.append(carta)

    global paired_images
    paired_images = {}
    for i, value in enumerate(espacios):
        paired_images[value] = images[i % len(images)]


def dibujar_bg():
    top_menu = pygame.draw.rect(screen, BLACK, [0,0,  ANCHO, 100])
    bottom_menu = pygame.draw.rect(screen,BLACK, [0, ALTO - 100, ANCHO, 100], 0)
    tablero = pygame.draw.rect(screen, GRAY, [0,100, ANCHO, ANCHO - 200], 0)

def dibujar_cartas():
    global filas, columnas, paired_images
    board_list = []
    
    card_width, card_height = 50, 50
    margin_x, margin_y = 24, 112
    
    spacing_x = (ANCHO - 2 * margin_x - columnas * card_width) / (columnas - 1)
    spacing_y = (ALTO - 2 * margin_y - filas * card_height) / (filas - 1)
    
    for i in range(columnas):
        for j in range(filas):
            pos_x = margin_x + i * (card_width + spacing_x)
            pos_y = margin_y + j * (card_height + spacing_y)
            
            pos = pygame.math.Vector2(pos_x, pos_y)
            
            value = espacios[i * filas + j]
            is_flipped = value in cartas_usadas
            if is_flipped:
                card_image = paired_images[value]
            else:
                card_image = card_back_image

            board_list.append((pos, card_image, value, is_flipped))

            screen.blit(card_image, pos)

    return board_list

def revisar_cartas(carta_1, carta_2):
    global espacios
    if espacios[carta_1] == espacios[carta_2]:
        print("Cartas iguales")
    else:
        print("Cartas diferentes")

def handle_menu_events(events):
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
def handle_menu_state(events):
    handle_menu_events(events)
    updater.update(events=events,mouse_rel=mouse_rel)

def handle_difficulty_state(events):
    handle_menu_events(events)
    screen.fill(WHITE)
    DifBotonesUpdater.update(events=events, mouse_rel=mouse_rel)

def handle_game_state(events):
    global tablero_nuevo, sel_1, sel_2, carta_1, carta_2, running
    if tablero_nuevo:
        generar_tablero()
        tablero_nuevo = False
    dibujar_bg()
    tablero = dibujar_cartas()

    for event in events:
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(tablero)):
                pos, card_image, value, is_flipped = tablero[i]
                rect = pygame.Rect(pos, card_image.get_size())
                if rect.collidepoint(event.pos) and not sel_1 and not is_flipped:
                    sel_1 = True
                    carta_1 = i
                    print(f'Se seleccionó la carta {espacios[carta_1]}')
                elif rect.collidepoint(event.pos) and sel_1 and not sel_2 and i != carta_1 and not is_flipped:
                    sel_2 = True
                    carta_2 = i
                    print(f'Se seleccionó la carta {espacios[carta_2]}')

    if sel_1 and sel_2:
        revisar_cartas(carta_1, carta_2)
        sel_1 = False
        sel_2 = False

# Eventos botones
boton_empezar.at_unclick = change_game_state
boton_empezar.at_unclick_params = {"game_state_value":1}
boton_facil.at_unclick =  change_difficulty
boton_facil.at_unclick_params = {"difficulty": 1}
boton_normal.at_unclick =  change_difficulty
boton_normal.at_unclick_params = {"difficulty": 2}
boton_dificil.at_unclick =  change_difficulty
boton_dificil.at_unclick_params = {"difficulty": 3}

# Main Loop
thorpy.call_before_gui(before_gui)
while running:
    clock.tick(60) 
    events = pygame.event.get()
    mouse_rel = pygame.mouse.get_rel()

    if game_state == "menu":
        handle_menu_state(events)
    if game_state == "dificultad":
        handle_difficulty_state(events)
    if game_state == "game":
        handle_game_state(events)

    pygame.display.flip()

pygame.quit()
