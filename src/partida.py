POSICAO_PECAS = [
            ["t", "c", "b", "q", "r", "b", "c", "t"],
            ["p", "p", "p", "p", "p", "p", "p", "p"],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            ["T", "C", "B", "Q", "R", "B", "C", "T"]
        ]
IMAGENS =  {
            "P": "assets/b_peao.png", "B": "assets/b_bispo.png", "C": "assets/b_cavalo.png",
            "T": "assets/b_torre.png", "Q": "assets/b_rainha.png", "R": "assets/b_rei.png",
            "p": "assets/p_peao.png", "b": "assets/p_bispo.png", "c": "assets/p_cavalo.png",
            "t": "assets/p_torre.png", "q": "assets/p_rainha.png", "r": "assets/p_rei.png"
        }
VEZ_DE_JOGAR = ["P", "T", "C", "B", "Q", "R"]
CASAS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
TAMANHO = 800
TAMANHO_QUADRADO = TAMANHO // 8
HISTORICO = []
ULTIMO_MOVIMENTO = []
VOLTAR = []

import pygame
import sys
from tabuleiro import Tabuleiro
from peca import Peca
from jogador import Jogador
from menu_partida import Menu_partida

class Partida:
    def __init__(self, tela):
        self.tela = tela
        self.tabuleiro = Tabuleiro()
        self.pecas = Peca(tela)
        self.jogador = Jogador(tela)
        self.relogio = pygame.time.Clock()
        self.partida = True
        self.menu_partida = Menu_partida()
        
    def iniciar(self): 
        while self.partida == True:
            self.relogio.tick(60)
            self.tela.fill((255, 255, 255))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Botão esquerdo do mouse
                        self.jogador.pegar_peça() 
                        if self.menu_partida.botao_voltar.collidepoint(event.pos):
                            self.voltar_jogada()
                        elif self.menu_partida.botao_reiniciar.collidepoint(event.pos):
                            self.reiniciar_partida()
                        elif self.menu_partida.botao_ver_movimentos.collidepoint(event.pos):
                            self.tabuleiro.ver_movimentos = not self.tabuleiro.ver_movimentos
                           
                        
                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:  # Botão esquerdo do mouse
                        self.jogador.soltar_peça()

                            
            self.tabuleiro.desenhar_tabuleiro(self.tela, self.jogador.movimentos)
            self.pecas.desenhar_peças()
            self.menu_partida.desenhar(self.tela)
            
            if self.jogador.mouse_pressed:
                self.jogador.movendo_peça()

            pygame.display.flip()
    
    def voltar_jogada(self):
        if VOLTAR != []:
            if VEZ_DE_JOGAR[0] == "P":
                VEZ_DE_JOGAR[:] = ["p", "t", "c", "b", "q", "r"]
            else:
                VEZ_DE_JOGAR[:] = ["P", "T", "C", "B", "Q", "R"]

            POSICAO_PECAS[:] = VOLTAR.pop()
            HISTORICO.pop()
            ULTIMO_MOVIMENTO.clear()
            
    def reiniciar_partida(self,):
        POSICAO_PECAS[:] = [
            ["t", "c", "b", "q", "r", "b", "c", "t"],
            ["p", "p", "p", "p", "p", "p", "p", "p"],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            ["T", "C", "B", "Q", "R", "B", "C", "T"]
        ]
        VEZ_DE_JOGAR[:] = ["P", "T", "C", "B", "Q", "R"]
        HISTORICO.clear()
        VOLTAR.clear()
        ULTIMO_MOVIMENTO[:] = []
        
        