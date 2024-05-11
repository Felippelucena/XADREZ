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
        self.dados_historico = []
        self.historico = []
        self.ultimo_movimento = []
        
        
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
                        self.jogador.pegar_peça(self.tabuleiro.posicao_pecas, self.historico, self.pecas) 
                        if self.menu_partida.botao_voltar.collidepoint(event.pos):
                            self.voltar_jogada()
                        elif self.menu_partida.botao_reiniciar.collidepoint(event.pos):
                            self.reiniciar_partida()
                        elif self.menu_partida.botao_ver_movimentos.collidepoint(event.pos):
                            self.tabuleiro.ver_movimentos = not self.tabuleiro.ver_movimentos
                           
                        
                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:  # Botão esquerdo do mouse
                        self.jogador.soltar_peça( self.tabuleiro.posicao_pecas, self.historico, self.dados_historico, self.ultimo_movimento, self.menu_partida)

                            
            self.tabuleiro.desenhar_tabuleiro(self.tela, self.jogador.movimentos, self.ultimo_movimento)
            self.pecas.desenhar_peças(self.tabuleiro.posicao_pecas)
            self.menu_partida.desenhar(self.tela)
            
            if self.jogador.mouse_pressed:
                self.jogador.movendo_peça()

            pygame.display.flip()
    
    def voltar_jogada(self):
        if self.historico != []:
            self.jogador.trocar_jogador()
            self.tabuleiro.posicao_pecas[:] = self.historico.pop()
            self.dados_historico.pop()
            self.menu_partida.texto_histotico.pop()
            self.ultimo_movimento.clear()
            
    def reiniciar_partida(self):
        if self.historico != []:
            self.tabuleiro.posicao_pecas[:] = self.historico[0]
            self.jogador.jogador_atual[:] = ["P", "T", "C", "B", "D", "R"]
            self.dados_historico.clear()
            self.historico.clear()
            self.ultimo_movimento.clear()
            self.menu_partida.texto_histotico.clear()
            