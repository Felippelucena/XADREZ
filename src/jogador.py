import pygame
import copy
from const import *

class Jogador:
    def __init__(self, tela):
        self.tela = tela
        self.movimentos = []
        self.origem_peca_selecionada = None
        self.esquerdo_pressionado = False
        self.direito_pressionado = False
        self.imagens = IMAGENS
        self.jogador_atual = ["P", "T", "C", "B", "D", "R"]
        
    def pegar_peça(self, posicao_pecas, historico, pecas, ultimo_movimento):
        x, y = pygame.mouse.get_pos()
        lin = (y // TAMANHO_QUADRADO)
        col = (x // TAMANHO_QUADRADO)
        if lin >= 0 and lin < 8 and col >= 0 and col < 8 and posicao_pecas[lin][col] != " " and posicao_pecas[lin][col] in self.jogador_atual:
            self.esquerdo_pressionado = True
            self.origem_peca_selecionada = [posicao_pecas[lin][col], lin, col,pygame.transform.scale(pygame.image.load(self.imagens[posicao_pecas[lin][col]]), (TAMANHO_QUADRADO*1.5, TAMANHO_QUADRADO*1.5)) ]
            self.movimentos = pecas.movimentos_possiveis((lin, col), posicao_pecas, ultimo_movimento)
            historico.append(copy.deepcopy(posicao_pecas))
            posicao_pecas[lin][col] = " "
    
    def movendo_peça(self):
            x, y = pygame.mouse.get_pos()
            self.tela.blit(self.origem_peca_selecionada[3], (x-TAMANHO_QUADRADO/1.5, y-TAMANHO_QUADRADO/1.5))
            
    def soltar_peça(self, posicao_pecas, historico, dados_historico,ultimo_movimento, pecas):
        self.esquerdo_pressionado = False
        if self.origem_peca_selecionada != None:
            x, y = pygame.mouse.get_pos()
            lin = (y // TAMANHO_QUADRADO)
            col = (x // TAMANHO_QUADRADO)
            if lin >= 0 and lin < 9 and col >= 0 and col < 9 and (lin, col) in self.movimentos:
                posicao_pecas[lin][col] = self.origem_peca_selecionada[0]
                self.trocar_jogador()
                pecas.promocao_peao(lin, col, posicao_pecas, self.origem_peca_selecionada[0])
                pecas.el_passant(lin, col, posicao_pecas, ultimo_movimento, self.origem_peca_selecionada[0])
                
                dados_historico.append([self.origem_peca_selecionada[0], self.origem_peca_selecionada[1], self.origem_peca_selecionada[2], col, lin])
                ultimo_movimento[:] = [(self.origem_peca_selecionada[1],self.origem_peca_selecionada[2]), (lin, col)]
                self.origem_peca_selecionada = None
                self.movimentos = []
                return True
            else:
                posicao_pecas[self.origem_peca_selecionada[1]][self.origem_peca_selecionada[2]] = self.origem_peca_selecionada[0]
                historico.pop()
                self.origem_peca_selecionada = None
                self.movimentos = []

    def trocar_jogador(self):
        if self.jogador_atual[0] == "P":
            self.jogador_atual[:] = ["p", "t", "c", "b", "d", "r"]
        else:
            self.jogador_atual[:] = ["P", "T", "C", "B", "D", "R"]

    def criar_seta(self):
        pass