import random
import pygame
import thorpy
import os

# Variables
BLACK, RED, WHITE, GRAY, GREEN, BLUE = (0,0,0), (255,0,0), (255,255,255), (169,169,169), (0, 255, 0), (0, 0, 255)
ANCHO, ALTO = 600, 600
columnas, filas = 6, 6
puntaje = 0
best_score = 0
sel_rect_start_time = 0

images_folder = "Cards"
images_folder_set2 = "uno"

image_files_set1 = [f for f in os.listdir(images_folder) if f.endswith(".png")]
image_files_set2 = [f for f in os.listdir(images_folder_set2) if f.endswith(".png")]

images_set1 = [pygame.image.load(os.path.join(images_folder, img)) for img in image_files_set1]
images_set2 = [pygame.image.load(os.path.join(images_folder_set2, img)) for img in image_files_set2]

card_back_image = pygame.image.load("card_back.png")

selected_images = random.choice([images_set1, images_set2])

paired_images = selected_images * 2
random.shuffle(paired_images)

#Inicializando Pygame
pygame.init()
screen = pygame.display.set_mode((ANCHO, ALTO), pygame.RESIZABLE)
pygame.display.set_caption("Encuentra pares")
clock = pygame.time.Clock()
small_font = pygame.font.Font("PixeloidSans.ttf", 26)
title_font = pygame.font.Font("PixeloidSans.ttf", 32)
#Inicializando Thorpy
thorpy.init(screen, thorpy.themes.theme_human)
bg_gif = "Background.gif"
bg_anim = thorpy.AnimatedGif(bg_gif, frame_mod=2)
bg_anim.center_on(screen)
boton_empezar = thorpy.Button("Empezar")
boton_salir = thorpy.Button("Salir")
Botones = thorpy.Group([boton_empezar,boton_salir])
Botones.center_on(screen)
menugroup = thorpy.Group([bg_anim, Botones], None)
updater = menugroup.get_updater()

boton_facil = thorpy.Button("Facil")
boton_normal = thorpy.Button("Normal")
boton_dificil = thorpy.Button("Dificil")
boton_reiniciar = thorpy.Button("Reiniciar")
boton_reiniciar.move(60, 25)
boton_reiniciarUpdater = boton_reiniciar.get_updater()
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
pares = 0
game_over = False
in_delay = False
#Listas
opciones, espacios, cartas_usadas = [], [], []
cartas_correctas = []
carta_arriba = []
def quit():
    pygame.quit()
    exit()


def change_game_state(game_state_value):
    global game_state
    if game_state_value == 0:
        game_state = "menu"
    elif game_state_value == 1:
        game_state = "dificultad"
    elif game_state_value == 2:
        game_state = "game"

def reset_game():
    global opciones, espacios, cartas_usadas, cartas_correctas, tablero_nuevo, sel_1, sel_2, pares, game_over, puntaje
    global selected_images, images_set1, images_set2, paired_images
    opciones, espacios, cartas_usadas = [], [], []
    cartas_correctas = []
    tablero_nuevo = True
    sel_1 = False
    sel_2 = False
    pares = 0
    game_over = False
    puntaje = 0
    selected_images = random.choice([images_set1, images_set2])
    paired_images = selected_images * 2
    random.shuffle(paired_images)
    change_game_state(0)
def before_gui():
    screen.fill(WHITE)

def change_difficulty(difficulty : int):
    global columnas, filas, game_state, cartas_correctas, carta_arriba
    if difficulty == 1:
        columnas, filas = 4,4
        game_state = "game"
    elif difficulty == 2:
        columnas, filas = 6,6
        game_state = "game"
    elif difficulty == 3:
        columnas, filas = 8,8
        game_state = "game"
    cartas_correctas = [[0] * filas for _ in range(columnas)]
    carta_arriba = [False] * (columnas * filas)


def generar_tablero():
    global opciones, espacios, cartas_usadas
    opciones = list(range(columnas * filas // 2)) * 2
    random.shuffle(opciones)
    
    espacios = []
    for i in range(columnas * filas):
        carta = opciones.pop()
        espacios.append(carta)
        cartas_usadas.append(carta)

    # Now, associate each value with an image
    global paired_images
    paired_images = {}
    for i, value in enumerate(espacios):
        paired_images[value] = selected_images[i % len(selected_images)] 

def dibujar_bg():
    tablero = pygame.draw.rect(screen, GRAY, [0,0, ANCHO, ALTO], 0)
    score_text = small_font.render(f'Turnos: {puntaje}', True, WHITE)
    screen.blit(score_text, (120, 15))
    best_text = small_font.render(f'Mejor intento: {best_score}', True, WHITE)
    screen.blit(best_text, (300, 15))
def dibujar_cartas():
    global filas, columnas, paired_images, sel_1, sel_2, carta_arriba
    board_list = []
    
    card_width, card_height = 50, 50
    margin_x, margin_y = 24, 50
    
    spacing_x = (ANCHO - 2 * margin_x - columnas * card_width) / (columnas - 1)
    spacing_y = (ALTO - 2 * margin_y - filas * card_height) / (filas - 1)
    
    for i in range(columnas):
        for j in range(filas):
            pos_x = margin_x + i * (card_width + spacing_x)
            pos_y = margin_y + j * (card_height + spacing_y)
            
            pos = pygame.math.Vector2(pos_x, pos_y)

            index = i * filas + j
            value = espacios[index]
            card_image = card_back_image if not carta_arriba[index] else paired_images[value]
            board_list.append((pos, card_image))
    
            if cartas_correctas[j][i] == 1:
                rect = pygame.Rect((pos_x + 8, pos_y), (card_width - 2, card_height + 14))
                pygame.draw.rect(screen, GREEN, rect)
            else:
                if sel_1 and carta_1 == index or sel_2 and carta_2 == index:
                    sel_rect = pygame.Rect((pos_x + 8, pos_y), (card_width - 2, card_height + 14))
                    pygame.draw.rect(screen, BLUE, sel_rect, 3)
            screen.blit(card_image, pos)
    return board_list


def revisar_cartas(carta_1, carta_2):
    global espacios, cartas_correctas, puntaje, pares, carta_arriba
    if espacios[carta_1] == espacios[carta_2]:
        col1 = carta_1 // filas
        col2 = carta_2 // filas
        fil1 = carta_1 - (carta_1 // filas * filas)
        fil2 = carta_2 - (carta_2 // filas * filas)
        if cartas_correctas[fil1][col1] == 0 and cartas_correctas[fil2][col2] == 0:
            cartas_correctas[fil1][col1] = 1
            cartas_correctas[fil2][col2] = 1
            puntaje += 1
            pares += 1
            print(cartas_correctas)
    else:
            carta_arriba[carta_1] = False
            carta_arriba[carta_2] = False
            puntaje += 1

def handle_menu_events(events):
    for event in events:
        if event.type == pygame.QUIT:
            quit()
def handle_menu_state(events):
    handle_menu_events(events)
    updater.update(events=events,mouse_rel=mouse_rel)

def handle_difficulty_state(events):
    handle_menu_events(events)
    screen.fill(WHITE)
    DifBotonesUpdater.update(events=events, mouse_rel=mouse_rel)

def handle_game_state(events):
    global tablero_nuevo, sel_1, sel_2, carta_1, carta_2, cartas_correctas, running, game_over, sel_rect_start_time, carta_arriba, in_delay, puntaje, best_score
    if tablero_nuevo:
        generar_tablero()
        tablero_nuevo = False
    dibujar_bg()
    tablero = dibujar_cartas()

    for event in events:
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and not in_delay:
            for i in range(len(tablero)):
                pos, card_image = tablero[i]
                rect = pygame.Rect(pos, card_image.get_size())
                if not game_over:
                    if rect.collidepoint(event.pos):
                        if not carta_arriba[i]:
                            carta_arriba[i] = True
                        elif sel_1 and carta_1 == i and sel_2 and carta_2 == i:
                            carta_arriba[i] = False

                        if not sel_1:
                            sel_1 = True
                            carta_1 = i
                            sel_rect_start_time = pygame.time.get_ticks()  # Record the start time of the delay
                        elif sel_1 and not sel_2 and i != carta_1:
                            sel_2 = True
                            carta_2 = i




    boton_reiniciarUpdater.update(events=events, mouse_rel=mouse_rel)

    if sel_1 and sel_2:
        current_time = pygame.time.get_ticks()
        in_delay = True
        if current_time - sel_rect_start_time < 2000:
            pos, card_image = tablero[carta_1]
            sel_rect_1 = pygame.Rect((pos[0] + 8, pos[1]), (50 - 2, 50 + 14))
            pos, card_image = tablero[carta_2]
            sel_rect_2 = pygame.Rect((pos[0] + 8, pos[1]), (50 - 2, 50 + 14))

            pygame.draw.rect(screen, BLUE, sel_rect_1, 3)
            pygame.draw.rect(screen, BLUE, sel_rect_2, 3)

        else:
            in_delay = False
            revisar_cartas(carta_1, carta_2)
            sel_1 = False
            sel_2 = False

    if sel_1:
        pos, card_image = tablero[carta_1]
        sel_rect_1 = pygame.Rect((pos[0] + 8, pos[1]), (50 - 2, 50 + 14))
        pygame.draw.rect(screen, BLUE, sel_rect_1, 3)

    if sel_2:
        pos, card_image = tablero[carta_2]
        sel_rect_2 = pygame.Rect((pos[0] + 8, pos[1]), (50 - 2, 50 + 14))
        pygame.draw.rect(screen, BLUE, sel_rect_2, 3)

    if pares == filas * columnas // 2:
        game_over = True
        winner = pygame.draw.rect(screen, BLACK, [10, ALTO - 300,ANCHO - 20, 80], 0, 5)
        winner_text = small_font.render(f"Ganaste en {puntaje} movimientos", True, WHITE)
        screen.blit(winner_text, (120,ALTO - 280))
        if best_score < puntaje or best_score == 0:
            best_score = puntaje



# Eventos botones
boton_empezar.at_unclick = change_game_state
boton_empezar.at_unclick_params = {"game_state_value":1}
boton_facil.at_unclick =  change_difficulty
boton_facil.at_unclick_params = {"difficulty": 1}
boton_normal.at_unclick =  change_difficulty
boton_normal.at_unclick_params = {"difficulty": 2}
boton_dificil.at_unclick =  change_difficulty
boton_dificil.at_unclick_params = {"difficulty": 3}
boton_reiniciar.at_unclick = reset_game
boton_salir.at_unclick = quit
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