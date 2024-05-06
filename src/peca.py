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
        self.movimentos = []
        self.peça_selecionada = None
        self.mouse_pressed = False


    def desenhar_peças(self):
        for row in range(8):
            for col in range(8):
                peça = self.tabuleiro[row][col]
                if peça != " ":
                    # Carrega a imagem correspondente à peça
                    imagem = pygame.image.load(self.imagens[peça])
                    # Redimensiona a imagem para o tamanho do quadrado do tabuleiro
                    imagem = pygame.transform.scale(imagem, (TAMANHO_QUADRADO, TAMANHO_QUADRADO))
                    # Desenha a imagem na posição (row, col)
                    self.tela.blit(imagem, (col * TAMANHO_QUADRADO, row * TAMANHO_QUADRADO))

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
        
        if peça == "p": # Peão preto
            # Verifica movimento para frente
            if self.tabuleiro[row + 1][col] == " ":
                movimentos.append((row + 1, col))
                # Verifica movimento duplo no primeiro movimento
                if row == 1 and self.tabuleiro[row + 2][col] == " ":
                    movimentos.append((row + 2, col))
            # Verifica captura na diagonal
            if col > 0 and self.tabuleiro[row + 1][col - 1].isupper():
                movimentos.append((row + 1, col - 1))
            if col < 7 and self.tabuleiro[row + 1][col + 1].isupper():
                movimentos.append((row + 1, col + 1))
        
        if peça == "T" or peça == "t":  # Torre
            
            # Verifica movimentos para cima
            for r in range(row - 1, -1, -1):
                if self.tabuleiro[r][col] == " ":
                    movimentos.append((r, col))
                else:
                    if peça.isupper() != self.tabuleiro[r][col].isupper():
                        movimentos.append((r, col))
                    break
            # Verifica movimentos para baixo
            for r in range(row + 1, 8):
                if self.tabuleiro[r][col] == " ":
                    movimentos.append((r, col))
                else:
                    if peça.isupper() != self.tabuleiro[r][col].isupper():
                        movimentos.append((r, col))
                    break
            # Verifica movimentos para a esquerda
            for c in range(col - 1, -1, -1):
                if self.tabuleiro[row][c] == " ":
                    movimentos.append((row, c))
                else:
                    if peça.isupper() != self.tabuleiro[row][c].isupper():
                        movimentos.append((row, c))
                    break
            # Verifica movimentos para a direita
            for c in range(col + 1, 8):
                if self.tabuleiro[row][c] == " ":
                    movimentos.append((row, c))
                else:
                    if peça.isupper() != self.tabuleiro[row][c].isupper():
                        movimentos.append((row, c))
                    break
        
        if peça == "C" or peça == "c":  # Cavalo
            if row - 2 >= 0 and col - 1 >= 0 and (self.tabuleiro[row - 2][col - 1] == " " or peça.isupper() != self.tabuleiro[row - 2][col - 1].isupper()):
                movimentos.append((row - 2, col - 1))
            if row - 2 >= 0 and col + 1 < 8 and (self.tabuleiro[row - 2][col + 1] == " " or peça.isupper() != self.tabuleiro[row - 2][col + 1].isupper()):
                movimentos.append((row - 2, col + 1))
            if row - 1 >= 0 and col - 2 >= 0 and (self.tabuleiro[row - 1][col - 2] == " " or peça.isupper() != self.tabuleiro[row - 1][col - 2].isupper()):
                movimentos.append((row - 1, col - 2))
            if row - 1 >= 0 and col + 2 < 8 and (self.tabuleiro[row - 1][col + 2] == " " or peça.isupper() != self.tabuleiro[row - 1][col + 2].isupper()):
                movimentos.append((row - 1, col + 2))
            if row + 1 < 8 and col - 2 >= 0 and (self.tabuleiro[row + 1][col - 2] == " " or peça.isupper() != self.tabuleiro[row + 1][col - 2].isupper()):
                movimentos.append((row + 1, col - 2))
            if row + 1 < 8 and col + 2 < 8 and (self.tabuleiro[row + 1][col + 2] == " " or peça.isupper() != self.tabuleiro[row + 1][col + 2].isupper()):
                movimentos.append((row + 1, col + 2))
            if row + 2 < 8 and col - 1 >= 0 and (self.tabuleiro[row + 2][col - 1] == " " or peça.isupper() != self.tabuleiro[row + 2][col - 1].isupper()):
                movimentos.append((row + 2, col - 1))
            if row + 2 < 8 and col + 1 < 8 and (self.tabuleiro[row + 2][col + 1] == " " or peça.isupper() != self.tabuleiro[row + 2][col + 1].isupper()):
                movimentos.append((row + 2, col + 1))
        
        if peça == "B" or peça == "b":  # Bispo
            # Verifica movimentos na diagonal principal
            r, c = row - 1, col - 1
            while r >= 0 and c >= 0:
                if self.tabuleiro[r][c] == " ":
                    movimentos.append((r, c))
                else:
                    if peça.isupper() != self.tabuleiro[r][c].isupper():
                        movimentos.append((r, c))
                    break
                r -= 1
                c -= 1
            r, c = row + 1, col + 1
            while r < 8 and c < 8:
                if self.tabuleiro[r][c] == " ":
                    movimentos.append((r, c))
                else:
                    if peça.isupper() != self.tabuleiro[r][c].isupper():
                        movimentos.append((r, c))
                    break
                r += 1
                c += 1
            # Verifica movimentos na diagonal secundária
            r, c = row - 1, col + 1
            while r >= 0 and c < 8:
                if self.tabuleiro[r][c] == " ":
                    movimentos.append((r, c))
                else:
                    if peça.isupper() != self.tabuleiro[r][c].isupper():
                        movimentos.append((r, c))
                    break
                r -= 1
                c += 1
            r, c = row + 1, col - 1
            while r < 8 and c >= 0:
                if self.tabuleiro[r][c] == " ":
                    movimentos.append((r, c))
                else:
                    if peça.isupper() != self.tabuleiro[r][c].isupper():
                        movimentos.append((r, c))
                    break
                r += 1
                c -= 1
        
        if peça == "Q" or peça == "q":  # Rainha
            # Verifica movimentos na horizontal e vertical
            for r in range(row - 1, -1, -1):
                if self.tabuleiro[r][col] == " ":
                    movimentos.append((r, col))
                else:
                    if peça.isupper() != self.tabuleiro[r][col].isupper():
                        movimentos.append((r, col))
                    break
            for r in range(row + 1, 8):
                if self.tabuleiro[r][col] == " ":
                    movimentos.append((r, col))
                else:
                    if peça.isupper() != self.tabuleiro[r][col].isupper():
                        movimentos.append((r, col))
                    break
            for c in range(col - 1, -1, -1):
                if self.tabuleiro[row][c] == " ":
                    movimentos.append((row, c))
                else:
                    if peça.isupper() != self.tabuleiro[row][c].isupper():
                        movimentos.append((row, c))
                    break
            for c in range(col + 1, 8):
                if self.tabuleiro[row][c] == " ":
                    movimentos.append((row, c))
                else:
                    if peça.isupper() != self.tabuleiro[row][c].isupper():
                        movimentos.append((row, c))
                    break
            # Verifica movimentos na diagonal principal
            r, c = row - 1, col - 1
            while r >= 0 and c >= 0:
                if self.tabuleiro[r][c] == " ":
                    movimentos.append((r, c))
                else:
                    if peça.isupper() != self.tabuleiro[r][c].isupper():
                        movimentos.append((r, c))
                    break
                r -= 1
                c -= 1
            r, c = row + 1, col + 1
            while r < 8 and c < 8:
                if self.tabuleiro[r][c] == " ":
                    movimentos.append((r, c))
                else:
                    if peça.isupper() != self.tabuleiro[r][c].isupper():
                        movimentos.append((r, c))
                    break
                r += 1
                c += 1
            # Verifica movimentos na diagonal secundária
            r, c = row - 1, col + 1
            while r >= 0 and c < 8:
                if self.tabuleiro[r][c] == " ":
                    movimentos.append((r, c))
                else:
                    if peça.isupper() != self.tabuleiro[r][c].isupper():
                        movimentos.append((r, c))
                    break
                r -= 1
                c += 1
            r, c = row + 1, col - 1
            while r < 8 and c >= 0:
                if self.tabuleiro[r][c] == " ":
                    movimentos.append((r, c))
                else:
                    if peça.isupper() != self.tabuleiro[r][c].isupper():
                        movimentos.append((r, c))
                    break
                r += 1
                c -= 1
                
        if peça == "R" or peça == "r":  # Rei
            if row - 1 >= 0 and col - 1 >= 0 and (self.tabuleiro[row - 1][col - 1] == " " or peça.isupper() != self.tabuleiro[row - 1][col - 1].isupper()):
                movimentos.append((row - 1, col - 1))
            if row - 1 >= 0 and (self.tabuleiro[row - 1][col] == " " or peça.isupper() != self.tabuleiro[row - 1][col].isupper()):
                movimentos.append((row - 1, col))
            if row - 1 >= 0 and col + 1 < 8 and (self.tabuleiro[row - 1][col + 1] == " " or peça.isupper() != self.tabuleiro[row - 1][col + 1].isupper()):
                movimentos.append((row - 1, col + 1))
            if col - 1 >= 0 and (self.tabuleiro[row][col - 1] == " " or peça.isupper() != self.tabuleiro[row][col - 1].isupper()):
                movimentos.append((row, col - 1))
            if col + 1 < 8 and (self.tabuleiro[row][col + 1] == " " or peça.isupper() != self.tabuleiro[row][col + 1].isupper()):
                movimentos.append((row, col + 1))
            if row + 1 < 8 and col - 1 >= 0 and (self.tabuleiro[row + 1][col - 1] == " " or peça.isupper() != self.tabuleiro[row + 1][col - 1].isupper()):
                movimentos.append((row + 1, col - 1))
            if row + 1 < 8 and (self.tabuleiro[row + 1][col] == " " or peça.isupper() != self.tabuleiro[row + 1][col].isupper()):
                movimentos.append((row + 1, col))
            if row + 1 < 8 and col + 1 < 8 and (self.tabuleiro[row + 1][col + 1] == " " or peça.isupper() != self.tabuleiro[row + 1][col + 1].isupper()):
                movimentos.append((row + 1, col + 1))      
        
        return movimentos
        
    def pegar_peça(self):
        x, y = pygame.mouse.get_pos()
        row = (y // TAMANHO_QUADRADO)
        col = (x // TAMANHO_QUADRADO)
        self.mouse_pressed = True
        if self.tabuleiro[row][col] != " ":
            self.peça_selecionada = [self.tabuleiro[row][col], row, col,pygame.transform.scale(pygame.image.load(self.imagens[self.tabuleiro[row][col]]), (TAMANHO_QUADRADO*1.5, TAMANHO_QUADRADO*1.5)) ]
            self.movimentos = self.movimentos_possiveis((row, col))
            self.tabuleiro[row][col] = " "
        else: 
            self.mouse_pressed = False
            
    def soltar_peça(self):
        self.mouse_pressed = False
        if self.peça_selecionada != None:
            x, y = pygame.mouse.get_pos()
            row = (y // TAMANHO_QUADRADO)
            col = (x // TAMANHO_QUADRADO)
            if row >= 0 and row < 9 and col >= 0 and col < 9 and (row, col) in self.movimentos:
                self.tabuleiro[row][col] = self.peça_selecionada[0]
            else:
                self.tabuleiro[self.peça_selecionada[1]][self.peça_selecionada[2]] = self.peça_selecionada[0]
                
            self.peça_selecionada = None
            self.movimentos = []