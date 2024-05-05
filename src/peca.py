import pygame
from const import *

class Peça:
    def __init__(self, tela):
        self.tabuleiro = [
            ["t", "c", "b", "q", "r", "b", "c", "t"],
            ["p", "p", "p", "p", "p", "p", "p", "p"],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            ["T", "C", "B", "Q", "R", "B", "C", "T"]
        ]
        self.imagens = {
                "P": "assets/b_peao.png", "B": "assets/b_bispo.png", "C": "assets/b_cavalo.png",
                "T": "assets/b_torre.png", "Q": "assets/b_rainha.png", "R": "assets/b_rei.png",
                "p": "assets/p_peao.png", "b": "assets/p_bispo.png", "c": "assets/p_cavalo.png",
                "t": "assets/p_torre.png", "q": "assets/p_rainha.png", "r": "assets/p_rei.png"
                }
        self.tela = tela
        self.selecionado = None
        self.movimentos = []
        self.peça_selecionada = None
        self.mouse_pressed = False

    def desenhar_peças(self):
        
        #imagem do peao dentro da pasta assets:

        for row in range(8):
            for col in range(8):
                peça = self.tabuleiro[row][col]
                if peça != " ":
                    # Carrega a imagem correspondente à peça
                    imagem = pygame.image.load(self.imagens[peça])
                    # Redimensiona a imagem para o tamanho do quadrado do tabuleiro
                    imagem = pygame.transform.scale(imagem, (TAMANHO_QUADRADO, TAMANHO_QUADRADO))
                    # Desenha a imagem na posição (row, col)
                    self.tela.blit(imagem, (col * TAMANHO_QUADRADO+100, row * TAMANHO_QUADRADO+100))

    def movimentos_possiveis(self, origem):
        row, col = origem
        peça = self.tabuleiro[row][col]

        movimentos = []

        if peça == "P":  # Peão branco
            # Verifica movimento para frente
            if self.tabuleiro[row - 1][col] == " ":
                movimentos.append((row - 1, col))
                # Verifica movimento duplo no primeiro movimento
                if row == 6 and self.tabuleiro[row - 2][col] == " ":
                    movimentos.append((row - 2, col))
            # Verifica captura na diagonal
            if col > 0 and self.tabuleiro[row - 1][col - 1].islower():
                movimentos.append((row - 1, col - 1))
            if col < 7 and self.tabuleiro[row - 1][col + 1].islower():
                movimentos.append((row - 1, col + 1))

        # Implemente lógica para outras peças (Bispo, Cavalo, Torre, Rainha, Rei)

        return movimentos
    
    def mover_peça(self, origem, destino):
        row_origem, col_origem = origem
        row_destino, col_destino = destino

        peça = self.tabuleiro[row_origem][col_origem]

        # Atualiza a posição da peça no tabuleiro
        self.tabuleiro[row_destino][col_destino] = peça
        self.tabuleiro[row_origem][col_origem] = " "

        # Exemplo de implementação de promoção de peão (opcional)
        if peça == "P" and row_destino == 0:  # Peão branco alcançou a última linha
            self.tabuleiro[row_destino][col_destino] = "Q"  # Promove para Rainha

        # Implemente lógica para outras situações especiais, como roque, en passant, captura de peças, etc.
        
    def selecionar_peça(self):
        x, y = pygame.mouse.get_pos()
        row = y // TAMANHO_QUADRADO
        col = x // TAMANHO_QUADRADO
        self.mouse_pressed = True
        if self.tabuleiro[row-1][col-1] != " ":                
            self.selecionado = pygame.transform.scale(pygame.image.load(self.imagens[self.tabuleiro[row-1][col-1]]), (TAMANHO_QUADRADO*1.5, TAMANHO_QUADRADO*1.5))
            self.peça_selecionada = self.tabuleiro[row-1][col-1]
            self.movimentos = self.movimentos_possiveis((row-1, col-1))
            self.tabuleiro[row-1][col-1] = " "
        else: 
            self.mouse_pressed = False
            
    def selecao(self):
        self.mouse_pressed = False
        if self.peça_selecionada != None:
            x, y = pygame.mouse.get_pos()
            row = y // TAMANHO_QUADRADO
            col = x // TAMANHO_QUADRADO
            self.tabuleiro[row-1][col-1] = self.peça_selecionada
            self.peça_selecionada = None
            self.movimentos = []