import pygame, sys
pygame.init()

size = (800,600)
screen = pygame.display.set_mode(size)

fondo = pygame.image.load("fondo.png")
fondo = pygame.transform.scale(fondo,(800,600))
imagen1 = pygame.image.load("rojo.png")
imagen1 = pygame.transform.scale(imagen1,(100,100))
imagen2 = pygame.image.load("verde.png")
imagen2 = pygame.transform.scale(imagen2,(100,100))
imagen3 = pygame.image.load("amarillo.png")
imagen3 = pygame.transform.scale(imagen3,(100,100))
imagen4 = pygame.image.load("Azul.png")
imagen4 = pygame.transform.scale(imagen4,(100,100))



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.blit(fondo,(0,0))
    screen.blit(imagen1,(100,250))
    screen.blit(imagen1,(100,400))
    screen.blit(imagen1,(100,100))
    screen.blit(imagen2,(250,250))
    screen.blit(imagen2,(250,400))
    screen.blit(imagen2,(250,100))
    screen.blit(imagen3,(400,250))
    screen.blit(imagen3,(400,400))
    screen.blit(imagen3,(400,100))
    screen.blit(imagen4,(550,250))
    screen.blit(imagen4,(550,400))
    screen.blit(imagen4,(550,100))
    pygame.display.flip()