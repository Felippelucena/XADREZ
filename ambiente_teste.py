import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

largura = 620
altura = 480

x = largura/2-20
y = altura/2-20
x2 =500
y2 = 400
cont = 0

tela = pygame.display.set_mode((largura, altura))


relogio = pygame.time.Clock() # Inicia o Controle de FPS
fonte = pygame.font.SysFont('Segoe UI Symbol', 30, True, False)

while True:
    relogio.tick(60) #seta 60 Frames por segundo
    tela.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
            
    if pygame.key.get_pressed()[K_LEFT]:
        x -= 8
    if pygame.key.get_pressed()[K_RIGHT]:
        x += 8
    if pygame.key.get_pressed()[K_UP]:
        y -= 8
    if pygame.key.get_pressed()[K_DOWN]:
        y += 8
    
    if x > largura-40:
        x = largura-40
    
    if x < 0:
        x = 0
        
    if y > altura-40:
        y = altura-40
    
    if y < 0:
        y = 0
                    
    jogador = pygame.draw.rect(tela, (248, 89, 103), (x, y, 40, 40))
    objeto = pygame.draw.rect(tela, (89, 103, 230), (x2, y2, 40, 40))
    contador = fonte.render(f'Pontos:{cont}', True, (255, 255, 255))
    tela.blit(contador, (10, 10))
    
    if jogador.colliderect(objeto):
        x2 = randint(0, largura-40)
        y2 = randint(0, altura-40)
        cont += 1
        
    pygame.display.update()
    