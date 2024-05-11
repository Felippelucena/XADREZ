import pygame
from const import *



class Tabuleiro:
    def __init__(self):
        self.ver_movimentos = False
        self.posicao_pecas = [
            ["t", "c", "b", "d", "r", "b", "c", "t"],
            ["p", "p", "p", "p", "p", "p", "p", "p"],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            ["T", "C", "B", "D", "R", "B", "C", "T"]
        ]

    def desenhar_tabuleiro(self, tela, movimentos, ultimo_movimento):
        
        fonte = pygame.font.SysFont('arial', TAMANHO_QUADRADO//5, True, False)
        
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
            if (row-1) % 2 == 0:
                cor = (234, 235, 200)
                id_cor = (119, 154, 88)
            else:
                cor = (119, 154, 88)
                id_cor = (234, 235, 200)              
            id_row = fonte.render(f'{8-row}', True, cor)
            tela.blit(id_row, (TAMANHO_QUADRADO/10, TAMANHO_QUADRADO/10+(row*TAMANHO_QUADRADO)))
            id_col = fonte.render(f'{CASAS[row]}', True, id_cor)
            tela.blit(id_col, (TAMANHO_QUADRADO/10+(row*TAMANHO_QUADRADO), (TAMANHO_QUADRADO*8-TAMANHO_QUADRADO/3))) 
        
        for row in range(8):
            for col in range(8):
                if (row, col) in ultimo_movimento:
                    if (row + col) % 2 == 0:
                        cor = (140, 230, 185)
                    else:
                        cor = (70, 120, 95)
                    pygame.draw.rect(tela, cor, (col * TAMANHO_QUADRADO, row * TAMANHO_QUADRADO, TAMANHO_QUADRADO, TAMANHO_QUADRADO))
                if  self.ver_movimentos and (row, col) in movimentos:
                    if (row + col) % 2 == 0:
                        cor = (70, 120, 95)#(119, 154, 88)
                    else:
                        cor = (140, 230, 185)#(234, 235, 200)
                    pygame.draw.rect(tela, cor, (col * TAMANHO_QUADRADO+TAMANHO_QUADRADO/10, row * TAMANHO_QUADRADO+TAMANHO_QUADRADO/10, TAMANHO_QUADRADO/1.25, TAMANHO_QUADRADO/1.25),TAMANHO_QUADRADO//10)

                