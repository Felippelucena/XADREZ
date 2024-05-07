import pygame
import sys
from const import *
from tabuleiro import Tabuleiro
from peca import Peca
from jogador import Jogador

def menu_inicial(tela):
    fonte = pygame.font.Font(None, 36)
    texto_novo_jogo = fonte.render("Novo Jogo", True, (0, 0, 0))
    retangulo_novo_jogo = texto_novo_jogo.get_rect(center=(TAMANHO // 2, TAMANHO // 2))

    while True:
        tela.fill((255, 255, 255))
        tela.blit(texto_novo_jogo, retangulo_novo_jogo)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Botão esquerdo do mouse
                    if retangulo_novo_jogo.collidepoint(event.pos):
                        return

def main():
    pygame.init()
    tela = pygame.display.set_mode((TAMANHO, TAMANHO))
    pygame.display.set_caption('Xadrez')

    menu_inicial(tela)

    tabuleiro = Tabuleiro()
    pecas = Peca(tela)
    jogador = Jogador(tela)
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
                    jogador.pegar_peça()    
                    
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:  # Botão esquerdo do mouse
                    jogador.soltar_peça()
            #reiniar peças quando apertar a tecla r
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    jogador.reiniciar_peças()

                    
        tabuleiro.desenhar_tabuleiro(tela, jogador.movimentos)
        pecas.desenhar_peças()
          
        if jogador.mouse_pressed:
            jogador.movendo_peça()

        pygame.display.flip()

if __name__ == "__main__":
    main()
