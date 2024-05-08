import pygame
import copy
from peca import Peca
from partida import *

class Jogador:
    def __init__(self, tela):
        self.tela = tela
        self.movimentos = []
        self.peça_selecionada = None
        self.mouse_pressed = False
        self.imagens = IMAGENS
        
    def pegar_peça(self):
        pecas = Peca(self.tela)
        x, y = pygame.mouse.get_pos()
        row = (y // TAMANHO_QUADRADO)
        col = (x // TAMANHO_QUADRADO)
        if row >= 0 and row < 8 and col >= 0 and col < 8:
            self.mouse_pressed = True
            if POSICAO_PECAS[row][col] != " " and POSICAO_PECAS[row][col] in VEZ_DE_JOGAR:
                self.peça_selecionada = [POSICAO_PECAS[row][col], row, col,pygame.transform.scale(pygame.image.load(self.imagens[POSICAO_PECAS[row][col]]), (TAMANHO_QUADRADO*1.5, TAMANHO_QUADRADO*1.5)) ]
                self.movimentos = pecas.movimentos_possiveis((row, col))
                VOLTAR.append(copy.deepcopy(POSICAO_PECAS))
                POSICAO_PECAS[row][col] = " "
            else: 
                self.mouse_pressed = False
    
    def movendo_peça(self):
            x, y = pygame.mouse.get_pos()
            self.tela.blit(self.peça_selecionada[3], (x-TAMANHO_QUADRADO/1.5, y-TAMANHO_QUADRADO/1.5))
            
    def soltar_peça(self):
        self.mouse_pressed = False
        if self.peça_selecionada != None:
            x, y = pygame.mouse.get_pos()
            row = (y // TAMANHO_QUADRADO)
            col = (x // TAMANHO_QUADRADO)
            if row >= 0 and row < 9 and col >= 0 and col < 9 and (row, col) in self.movimentos:
                self.trocar_jogador()
                self.salvar_movimento(row, col)
            else:
                POSICAO_PECAS[self.peça_selecionada[1]][self.peça_selecionada[2]] = self.peça_selecionada[0]
                VOLTAR.pop()
            self.peça_selecionada = None
            self.movimentos = []
            
    
    def salvar_movimento(self, row, col):
        POSICAO_PECAS[row][col] = self.peça_selecionada[0]
        HISTORICO.append(f'{self.peça_selecionada[0]}{CASAS[col]}{abs(row-8)}')
        ULTIMO_MOVIMENTO[:] = [(self.peça_selecionada[1],self.peça_selecionada[2]), (row, col)]
        
    def trocar_jogador(self):
        if VEZ_DE_JOGAR[0] == "P":
            VEZ_DE_JOGAR[:] = ["p", "t", "c", "b", "q", "r"]
        else:
            VEZ_DE_JOGAR[:] = ["P", "T", "C", "B", "Q", "R"]

                