import pygame, sys
pygame.init()

size = (800,600)
screen = pygame.display.set_mode(size)

fondo = pygame.image.load("fondo.png")
fondo = pygame.transform.scale(fondo,(800,600))
imagen1 = pygame.image.load("rojo.png")
imagen1 = pygame.transform.scale(imagen1,(100,100))
imagen2 = pygame.image.load("verde.png")
imagen2 = pygame.transform.scale(imagen2,(150,150))




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.blit(fondo,(0,0))
    screen.blit(imagen1,(100,250))
    screen.blit(imagen2,(150,250))
    pygame.display.flip()