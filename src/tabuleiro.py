import pygame
from const import *


class Tabuleiro:
    def __init__(self):
        self.oi = 'oi'

    def desenhar_tabuleiro(self, tela, movimentos):
        
        FONTE = pygame.font.SysFont('arial', 15, True, False)
        casas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        
        #Desenhar tabuleiro
        for row in range(8):
            for col in range(8):
                if (row + col) % 2 == 0:
                    cor = (234, 235, 200)
                    id_cor = (119, 154, 88)
                else:
                    cor = (119, 154, 88)
                    id_cor = (234, 235, 200)
                pygame.draw.rect(tela, cor, (col * TAMANHO_QUADRADO, row * TAMANHO_QUADRADO, TAMANHO_QUADRADO, TAMANHO_QUADRADO))
                
        #Desenhar ids das linhas e colunas
        for row in range(8):              
            if (row + col) % 2 == 0:
                cor = (234, 235, 200)
                id_cor = (119, 154, 88)
            else:
                cor = (119, 154, 88)
                id_cor = (234, 235, 200)              
            id_row = FONTE.render(f'{8-row}', True, cor)
            tela.blit(id_row, (TAMANHO_QUADRADO/10, TAMANHO_QUADRADO/10+(row*TAMANHO_QUADRADO)))
            id_col = FONTE.render(f'{casas[row]}', True, id_cor)
            tela.blit(id_col, (TAMANHO_QUADRADO/10+(row*TAMANHO_QUADRADO), (TAMANHO_QUADRADO*8-TAMANHO_QUADRADO/3))) 
        
        '''for row in range(8):
            for col in range(8):
                if (row, col) in movimentos:
                    if (row + col) % 2 == 0:
                        cor = (150, 90, 85)
                    else:
                        cor = (120, 70, 65)
                    pygame.draw.rect(tela, cor, (col * TAMANHO_QUADRADO, row * TAMANHO_QUADRADO, TAMANHO_QUADRADO, TAMANHO_QUADRADO))'''