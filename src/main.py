import pygame
import sys
from const import *
from tabuleiro import Tabuleiro
from peca import Peça


def main():
    pygame.init()
    tela = pygame.display.set_mode((TAMANHO, TAMANHO))
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
                    peças.pegar_peça()    
                    
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:  # Botão esquerdo do mouse
                    peças.soltar_peça()                        
                
        tabuleiro.desenhar_tabuleiro(tela, peças.movimentos)
        peças.desenhar_peças()
          
        if peças.mouse_pressed:
            x, y = pygame.mouse.get_pos()
            tela.blit(peças.peça_selecionada[3], (x-TAMANHO_QUADRADO/1.5, y-TAMANHO_QUADRADO/1.5))

        pygame.display.flip()

if __name__ == "__main__":
    main()