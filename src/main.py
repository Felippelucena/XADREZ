import pygame
import sys
from const import *
from tabuleiro import Tabuleiro
from peca import Peça


def main():
    pygame.init()
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption('Xadrez')

    tabuleiro = Tabuleiro()
    peças = Peça(tela)
    relogio = pygame.time.Clock()
    
    
    
    while True:
        relogio.tick(60)
        tela.fill((255, 255, 255))

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Botão esquerdo do mouse
                    peças.selecionar_peça()    
                    
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:  # Botão esquerdo do mouse
                    peças.selecao()
                        
                
        tabuleiro.desenhar_tabuleiro(tela, peças.movimentos)
        peças.desenhar_peças()
          
        if peças.mouse_pressed:
            x, y = pygame.mouse.get_pos()
            tela.blit(peças.selecionado, (x-80, y-80))

        pygame.display.flip()

if __name__ == "__main__":
    main()