import pygame

# Variables
black = (0,0,0)
red = (255,0,0)
white = (255,255,255)

WIDTH = 600
HEIGHT = 400

pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Match Card")
clock = pygame.time.Clock()



def dibujar_bg():
    top_menu = pygame.draw.rect(screen, black, [0,0, WIDTH, 50])

running = True
while running:
    clock.tick(60) 
    screen.fill(white)
    dibujar_bg()

    #Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


    mouse_pos = pygame.mouse.get_pos()
    x = mouse_pos[0]
    y = mouse_pos[1]

    square = pygame.draw.rect(screen, red, (x,y, 100,100))

    if pygame.mouse.get_pressed()[0]:
        square = pygame.draw.rect(screen, black, (x,y, 100,100))

    pygame.display.update()
