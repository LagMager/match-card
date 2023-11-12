import pygame

black = (0,0,0)
red = (255,0,0)
white = (255,255,255)


pygame.init()
screen = pygame.display.set_mode((800,400))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


    mouse_pos = pygame.mouse.get_pos()
    x = mouse_pos[0]
    y = mouse_pos[1]
    screen.fill(white)

    square = pygame.draw.rect(screen, red, (x,y, 100,100))

    if pygame.mouse.get_pressed()[0]:
        square = pygame.draw.rect(screen, black, (x,y, 100,100))

    pygame.display.update()
    clock.tick(60)
