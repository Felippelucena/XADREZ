import pygame
from const import *


class Tabuleiro:
    def __init__(self):
        self.oi = 'oi'

    def desenhar_tabuleiro(self, tela, movimentos):
        
        FONTE = pygame.font.SysFont('arial', 20, True, False)
        casas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        
        #Desenhar tabuleiro
        for row in range(8):
            for col in range(8):
                if (row, col) in movimentos:
                    cor = (238, 90, 75)
                    id_cor = (255, 255, 255)
                elif (row + col) % 2 == 0:
                    cor = (234, 235, 200)
                    id_cor = (119, 154, 88)
                else:
                    cor = (119, 154, 88)
                    id_cor = (234, 235, 200)
                pygame.draw.rect(tela, cor, (col * TAMANHO_QUADRADO+100, row * TAMANHO_QUADRADO+100, TAMANHO_QUADRADO, TAMANHO_QUADRADO))
                
        #Desenhar ids das linhas e colunas
        for row in range(8):              
            if (row + col) % 2 == 0:
                cor = (234, 235, 200)
                id_cor = (119, 154, 88)
            else:
                cor = (119, 154, 88)
                id_cor = (234, 235, 200)              
            id_row = FONTE.render(f'{8-row}', True, cor)
            tela.blit(id_row, (105, 105+(row*100)))
            id_col = FONTE.render(f'{casas[row]}', True, id_cor)
            tela.blit(id_col, (185+(row*100), 875))    
