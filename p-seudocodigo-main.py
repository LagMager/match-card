"""
Nombres: Maycol Andres Taquez
         Andres Perea
         Sebastian 

Correo: maycol.taquez@correounivalle.edu.co

Paso 1: Analisis del problema
Descripción:
Desarrolle un programa en Python para el juego de parejas teniendo en cuenta los siguientes 
requerimientos:
1. Desarrolle la lógica del juego por medio de funciones, utilice vectores, estructuras de decisión
y estructuras repetitivas.
2. Desarrolle la GUIs del juego, utilizando etiquetas, campos de entrada, botones, listas 
desplegables y otros que considere necesarios.
3. El programa tiene un tablero de 4x4 para encontrar las parejas de imágenes. Por defecto se 
debe cargar una imagen de base para que el usuario pueda ir descubriendo las parejas de 
imágenes.
4. Debajo del tablero de imágenes se debe incluir un campo texto y un botón para que el jugador 
indique qué imagen desea abrir para encontrar la pareja.
5. Cree una función que permita cargar la imagen de base cuando se inicie el programa. Las 
imágenes ocultas deben cargarse en forma aleatoria cada vez que se inicie el juego.
6. Escriba una función que permita ir descubriendo las imágenes. Cuando el usuario encuentre 
una pareja de imágenes, el sistema debe desactivarlas como se ve en las capturas de 
pantalla. En caso contrario, el programa debe volver a ocultar las imágenes cargando la 
imagen de base.
7. Cuando el jugador encuentre todas las parejas se debe imprimir un mensaje donde se 
indique que el jugador ganó. Esto se debe mostrar en una etiqueta al final del tablero. 
Adicionalmente, debe imprimir el número de intentos fallidos y el número total de intentos.

Entradas: Clic derecho, Click izquierdo
Salidas: Ejecutar acción de botones (Empezar(Facil, normal, dificil), Clasificaciones, Salir ), seleccionar y voltear cartas.

Paso 2: Algoritmo en Pseudocódigo

# Importar módulos pygame, random, thorpy

# Definir colores
black = (0, 0, 0)
red = (255, 0, 0)
white = (255, 255, 255)
gray = (169, 169, 169)

# Definir dimensiones de la ventana
ANCHO = 600
ALTO = 600

# Numero de filas y columnas de las cartas. 
columnas = 6
filas = 6

Iniciar_Pygame()

pantalla = crear_pantalla(ANCHO, ALTO, redimensionable)
configurar_titulo_ventana("Encuentra pares")
reloj = pygame.time.Clock()
fuente_pequena = cargar_fuente("PixeloidSans.ttf", 26)


Inicializar ThorPy ("screen", "theme_human")
bg_gif = Definir la ruta del archivo GIF "Background.gif"
bg_anim = crear una animación GIF(bg_gif, frame_mod=2)
Centrar bg_anim en la pantalla
Boton_empezar = Crear botón ("Empezar")
Boton_puntajes = Crear botón ("Clasificaciones")
Boton_salir = Crear botón ("Salir")
Botonnes = Crear un grupo de botones con los botones anteriores (Boton_empezar, Boton_puntajes, Boton_salir)
Centrar el grupo de botones en la pantalla
menugroup = Crear un grupo ([bg_anim, Botones], None)
updater = Obtener el actualizador del grupo

boton_facil = Crear botón ("Facil")
boton_normal = Crear botón ("Normal")
boton_dificil = Crear botón ("Dificil")

DifBotones = Crear grupo([boton_facil, boton_normal, boton_dificil], "h")
centrar Difbotones en la pantalla
DifBotonesUpdater = Actualizar DifBotones

running = Verdadero
game_state = "menu"
game_state_value = 0
tablero_nuevo = Verdadero
carta_1, carta_2 = 0, 0
sel_1, sel_2 = Falso, Falso

opciones, espacios, cartas_usadas = [], [], []
cartas_correctas = [[False] * filas for _ in range(columnas)]


change_game_state(game_state_value)
    Variable global game_state 
    Si game_state_value = 0, entonces
        Asignar "menu" a game_state
    Si game_state_value = 1, entonces
        Asignar "dificultad" a game_state
    Si game_state_value = 2, entonces
        Asignar "game" a game_state
Fin

before_gui()
    Llenar la pantalla (WHITE)
Fin


change_difficulty(difficulty: entero)
    variables globales columnas, filas, game_state
    Si difficulty = 1, entonces
        Asignar 4 a columnas y filas
        Asignar "game" a game_state
    Si difficulty = 2, entonces
        Asignar 6 a columnas y filas
        Asignar "game" a game_state
    Si difficulty = 3, entonces
        Asignar 8 a columnas y filas
        Asignar "game" a game_state
Fin

generar_tablero()
    Variables Globales: opciones, espacios, cartas_usadas

    Para i rango(columnas * filas // 2)
        opciones[i]
    Fin Para

    Para i rango(columnas * filas)
        carta = opciones[aleatorio_entre(0, longitud(opciones) - 1)]
        espacios[carta]

        Si carta está en cartas_usadas
            cartas_usadas.eliminar(carta)
            opciones.eliminar(carta)
        Sino
            cartas_usadas.agregar(carta)
        Fin Si
    Fin Para
Fin 

dibujar_bg()
    top_menu = dibujar_rectángulo(screen, negro, [0, 0, ANCHO, 100])
    tablero = dibujar_rectángulo(screen, gris, [0, 100, ANCHO, ANCHO - 200], 0)
    bottom_menu = dibujar_rectángulo(screen, negro, [0, ALTO - 100, ANCHO, 100], 0)
Fin 

dibujar_cartas()
    Variables Globales: filas, columnas
    board_list = []
    card_width, card_height = dimensiones (50, 50)
    margin_x, margin_y = 12, 112
    
    espaciado_x = (ANCHO - 2 * margin_x - columnas * card_width) / (columnas - 1)
    espaciado_y = (ALTO - 2 * margin_y - filas * card_height) / (filas - 1)
    
    Para i rango(columnas)
        Para j rango(filas)
            pos_x = margin_x + i * (card_width + espaciado_x)
            pos_y = margin_y + j * (card_height + espaciado_y)
            
            pos = Vector2(coordenadas (pos_x, pos_y))
            size = Vector2(dimensiones (card_width, card_height))
            
            carta = dibujar_rectángulo(screen, blanco, (*pos, *size), 0, 4)
            board_list[carta]

            piece_text = renderizar_texto(f'{espacios[i * columnas + j]}', Verdadero, gris)
            text_pos = [pos[0] + 20, pos[1] + 8]
            screen.blit(piece_text, text_pos)
            
        Fin Para
    retornar (board_list)
    Fin Para

revisar_cartas(carta_1, carta_2):
    global espacios
    if espacios[carta_1] == espacios[carta_2]:
        continuar
Fin

handle_menu_events(events):
    para event en events:
        si tipo de evento == pygame.QUIT:
            cerrar_pygame()
Fin

handle_menu_state(events):
    Ejecutar handle_menu_events con el parámetro events
    Actualizar el updater (eventos, desplazamiento del ratón (mouse_rel))
Fin

handle_difficulty_state(events):
    Ejecutar handle_menu_events con el parámetro events
    Llenar la pantalla (WHITE)
    Actualizar DifBotonesUpdater (eventos, desplazamiento del ratón (mouse_rel))
Fin

handle_game_state(events):
    Variables globales tablero_nuevo, sel_1, sel_2, carta_1, carta_2, running
    si tablero_nuevo es verdadero, entonces
        generar_tablero()
        tablero_nuevo = Falso
    dibujar_bg()
    tablero = dibujar_cartas()
    
    Para cada evento en pygame.event.get()
        Si tipo de evento = QUIT
            running = Falso
        Fin Si
        Si tipo de evento = MOUSEBUTTONDOWN
            Para i rango(longitud(tablero))
                carta = tablero[i]
                Si carta colisiona con (event.pos) y no sel_1
                    sel_1 = Verdadero
                    carta_1 = i
                    mostrar("Se seleccionó la carta", espacios[carta_1])
                Sino Si carta colisiona con (event.pos) y sel_1 y no sel_2 y i no es igual a carta_1
                    sel_2 = Verdadero
                    carta_2 = i
                    mostrar("Se seleccionó la carta", espacios[carta_2])
                Fin Si
            Fin Para
        Fin Si
    Fin para
    
    si sel_1 y sel_2 son verdaderas:
        revisar_cartas(sel_1, sel_2)
        sel_1 = Falso
        sel_2 = Falso
    Fin si
Fin

Asignar la función change_game_state a la acción de hacer clic sin soltar del botón_empezar
Asignar los parámetros {"game_state_value": 1} a los parámetros de la acción de hacer clic sin soltar del botón_empezar

Asignar la función change_difficulty a la acción de hacer clic sin soltar del botón_facil
Asignar los parámetros {"difficulty": 1} a los parámetros de la acción de hacer clic sin soltar del botón_facil

Asignar la función change_difficulty a la acción de hacer clic sin soltar del botón_normal
Asignar los parámetros {"difficulty": 2} a los parámetros de la acción de hacer clic sin soltar del botón_normal

Asignar la función change_difficulty a la acción de hacer clic sin soltar del botón_dificil
Asignar los parámetros {"difficulty": 3} a los parámetros de la acción de hacer clic sin soltar del botón_dificil


Llamar a la función before_gui utilizando thorpy.call_before_gui

Mientras running sea verdadero
    Fotogramas por segundo(60)
    events = Obtener la lista de eventos con pygame.event.get()
    mouse_rel = Obtener el desplazamiento del ratón con pygame.mouse.get_rel()

    Si el estado del juego = "menu", entonces
      Ejecutar handle_menu_state (eventos)
    Si el estado del juego = "dificultad", entonces
      Ejecutar handle_difficulty_state (eventos)
    Si el estado del juego = "game", entonces
      Ejecutar handle_game_state (eventos)

    Actualizar la pantalla()
Fin mientras

cerrar_pygame()



  





"""