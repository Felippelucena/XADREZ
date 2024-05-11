import pygame
import sys
from menu_inicial import Menu_inicial
from partida import Partida
from const import *

def main():
    largura_tela = TAMANHO + TAMANHO/2
    altura_tela = TAMANHO
    pygame.init()
    tela = pygame.display.set_mode((largura_tela, altura_tela))
    pygame.display.set_caption('Xadrez')
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        tela.fill((255, 255, 255))
        
        menu_inicial = Menu_inicial(tela, largura_tela, altura_tela)
        menu_inicial.iniciar()
        
        partida = Partida(tela)
        partida.iniciar()
        
        pygame.display.flip()
        
if __name__ == "__main__":
    main()
