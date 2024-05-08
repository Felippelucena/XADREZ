import pygame
from partida import *

class Peca:
    def __init__(self, tela):

        self.imagens = IMAGENS
        self.tela = tela


    def desenhar_peças(self):
        for row in range(8):
            for col in range(8):
                peça = POSICAO_PECAS[row][col]
                if peça != " ":
                    # Carrega a imagem correspondente à peça
                    imagem = pygame.image.load(self.imagens[peça])
                    # Redimensiona a imagem para o tamanho do quadrado do tabuleiro
                    imagem = pygame.transform.scale(imagem, (TAMANHO_QUADRADO, TAMANHO_QUADRADO))
                    # Desenha a imagem na posição (row, col)
                    self.tela.blit(imagem, (col * TAMANHO_QUADRADO, row * TAMANHO_QUADRADO))



    def movimentos_possiveis(self, origem):
        row, col = origem
        peça = POSICAO_PECAS[row][col]

        movimentos = []

        if peça == "P":  # Peão branco
            # Verifica movimento para frente
            if POSICAO_PECAS[row - 1][col] == " ":
                movimentos.append((row - 1, col))
                # Verifica movimento duplo no primeiro movimento
                if row == 6 and POSICAO_PECAS[row - 2][col] == " ":
                    movimentos.append((row - 2, col))
            # Verifica captura na diagonal
            if col > 0 and POSICAO_PECAS[row - 1][col - 1].islower():
                movimentos.append((row - 1, col - 1))
            if col < 7 and POSICAO_PECAS[row - 1][col + 1].islower():
                movimentos.append((row - 1, col + 1))
        
        if peça == "p": # Peão preto
            # Verifica movimento para frente
            if POSICAO_PECAS[row + 1][col] == " ":
                movimentos.append((row + 1, col))
                # Verifica movimento duplo no primeiro movimento
                if row == 1 and POSICAO_PECAS[row + 2][col] == " ":
                    movimentos.append((row + 2, col))
            # Verifica captura na diagonal
            if col > 0 and POSICAO_PECAS[row + 1][col - 1].isupper():
                movimentos.append((row + 1, col - 1))
            if col < 7 and POSICAO_PECAS[row + 1][col + 1].isupper():
                movimentos.append((row + 1, col + 1))
        
        if peça == "T" or peça == "t":  # Torre
            
            # Verifica movimentos para cima
            for r in range(row - 1, -1, -1):
                if POSICAO_PECAS[r][col] == " ":
                    movimentos.append((r, col))
                else:
                    if peça.isupper() != POSICAO_PECAS[r][col].isupper():
                        movimentos.append((r, col))
                    break
            # Verifica movimentos para baixo
            for r in range(row + 1, 8):
                if POSICAO_PECAS[r][col] == " ":
                    movimentos.append((r, col))
                else:
                    if peça.isupper() != POSICAO_PECAS[r][col].isupper():
                        movimentos.append((r, col))
                    break
            # Verifica movimentos para a esquerda
            for c in range(col - 1, -1, -1):
                if POSICAO_PECAS[row][c] == " ":
                    movimentos.append((row, c))
                else:
                    if peça.isupper() != POSICAO_PECAS[row][c].isupper():
                        movimentos.append((row, c))
                    break
            # Verifica movimentos para a direita
            for c in range(col + 1, 8):
                if POSICAO_PECAS[row][c] == " ":
                    movimentos.append((row, c))
                else:
                    if peça.isupper() != POSICAO_PECAS[row][c].isupper():
                        movimentos.append((row, c))
                    break
        
        if peça == "C" or peça == "c":  # Cavalo
            if row - 2 >= 0 and col - 1 >= 0 and (POSICAO_PECAS[row - 2][col - 1] == " " or peça.isupper() != POSICAO_PECAS[row - 2][col - 1].isupper()):
                movimentos.append((row - 2, col - 1))
            if row - 2 >= 0 and col + 1 < 8 and (POSICAO_PECAS[row - 2][col + 1] == " " or peça.isupper() != POSICAO_PECAS[row - 2][col + 1].isupper()):
                movimentos.append((row - 2, col + 1))
            if row - 1 >= 0 and col - 2 >= 0 and (POSICAO_PECAS[row - 1][col - 2] == " " or peça.isupper() != POSICAO_PECAS[row - 1][col - 2].isupper()):
                movimentos.append((row - 1, col - 2))
            if row - 1 >= 0 and col + 2 < 8 and (POSICAO_PECAS[row - 1][col + 2] == " " or peça.isupper() != POSICAO_PECAS[row - 1][col + 2].isupper()):
                movimentos.append((row - 1, col + 2))
            if row + 1 < 8 and col - 2 >= 0 and (POSICAO_PECAS[row + 1][col - 2] == " " or peça.isupper() != POSICAO_PECAS[row + 1][col - 2].isupper()):
                movimentos.append((row + 1, col - 2))
            if row + 1 < 8 and col + 2 < 8 and (POSICAO_PECAS[row + 1][col + 2] == " " or peça.isupper() != POSICAO_PECAS[row + 1][col + 2].isupper()):
                movimentos.append((row + 1, col + 2))
            if row + 2 < 8 and col - 1 >= 0 and (POSICAO_PECAS[row + 2][col - 1] == " " or peça.isupper() != POSICAO_PECAS[row + 2][col - 1].isupper()):
                movimentos.append((row + 2, col - 1))
            if row + 2 < 8 and col + 1 < 8 and (POSICAO_PECAS[row + 2][col + 1] == " " or peça.isupper() != POSICAO_PECAS[row + 2][col + 1].isupper()):
                movimentos.append((row + 2, col + 1))
        
        if peça == "B" or peça == "b":  # Bispo
            # Verifica movimentos na diagonal principal
            r, c = row - 1, col - 1
            while r >= 0 and c >= 0:
                if POSICAO_PECAS[r][c] == " ":
                    movimentos.append((r, c))
                else:
                    if peça.isupper() != POSICAO_PECAS[r][c].isupper():
                        movimentos.append((r, c))
                    break
                r -= 1
                c -= 1
            r, c = row + 1, col + 1
            while r < 8 and c < 8:
                if POSICAO_PECAS[r][c] == " ":
                    movimentos.append((r, c))
                else:
                    if peça.isupper() != POSICAO_PECAS[r][c].isupper():
                        movimentos.append((r, c))
                    break
                r += 1
                c += 1
            # Verifica movimentos na diagonal secundária
            r, c = row - 1, col + 1
            while r >= 0 and c < 8:
                if POSICAO_PECAS[r][c] == " ":
                    movimentos.append((r, c))
                else:
                    if peça.isupper() != POSICAO_PECAS[r][c].isupper():
                        movimentos.append((r, c))
                    break
                r -= 1
                c += 1
            r, c = row + 1, col - 1
            while r < 8 and c >= 0:
                if POSICAO_PECAS[r][c] == " ":
                    movimentos.append((r, c))
                else:
                    if peça.isupper() != POSICAO_PECAS[r][c].isupper():
                        movimentos.append((r, c))
                    break
                r += 1
                c -= 1
        
        if peça == "Q" or peça == "q":  # Rainha
            # Verifica movimentos na horizontal e vertical
            for r in range(row - 1, -1, -1):
                if POSICAO_PECAS[r][col] == " ":
                    movimentos.append((r, col))
                else:
                    if peça.isupper() != POSICAO_PECAS[r][col].isupper():
                        movimentos.append((r, col))
                    break
            for r in range(row + 1, 8):
                if POSICAO_PECAS[r][col] == " ":
                    movimentos.append((r, col))
                else:
                    if peça.isupper() != POSICAO_PECAS[r][col].isupper():
                        movimentos.append((r, col))
                    break
            for c in range(col - 1, -1, -1):
                if POSICAO_PECAS[row][c] == " ":
                    movimentos.append((row, c))
                else:
                    if peça.isupper() != POSICAO_PECAS[row][c].isupper():
                        movimentos.append((row, c))
                    break
            for c in range(col + 1, 8):
                if POSICAO_PECAS[row][c] == " ":
                    movimentos.append((row, c))
                else:
                    if peça.isupper() != POSICAO_PECAS[row][c].isupper():
                        movimentos.append((row, c))
                    break
            # Verifica movimentos na diagonal principal
            r, c = row - 1, col - 1
            while r >= 0 and c >= 0:
                if POSICAO_PECAS[r][c] == " ":
                    movimentos.append((r, c))
                else:
                    if peça.isupper() != POSICAO_PECAS[r][c].isupper():
                        movimentos.append((r, c))
                    break
                r -= 1
                c -= 1
            r, c = row + 1, col + 1
            while r < 8 and c < 8:
                if POSICAO_PECAS[r][c] == " ":
                    movimentos.append((r, c))
                else:
                    if peça.isupper() != POSICAO_PECAS[r][c].isupper():
                        movimentos.append((r, c))
                    break
                r += 1
                c += 1
            # Verifica movimentos na diagonal secundária
            r, c = row - 1, col + 1
            while r >= 0 and c < 8:
                if POSICAO_PECAS[r][c] == " ":
                    movimentos.append((r, c))
                else:
                    if peça.isupper() != POSICAO_PECAS[r][c].isupper():
                        movimentos.append((r, c))
                    break
                r -= 1
                c += 1
            r, c = row + 1, col - 1
            while r < 8 and c >= 0:
                if POSICAO_PECAS[r][c] == " ":
                    movimentos.append((r, c))
                else:
                    if peça.isupper() != POSICAO_PECAS[r][c].isupper():
                        movimentos.append((r, c))
                    break
                r += 1
                c -= 1
                
        if peça == "R" or peça == "r":  # Rei
            if row - 1 >= 0 and col - 1 >= 0 and (POSICAO_PECAS[row - 1][col - 1] == " " or peça.isupper() != POSICAO_PECAS[row - 1][col - 1].isupper()):
                movimentos.append((row - 1, col - 1))
            if row - 1 >= 0 and (POSICAO_PECAS[row - 1][col] == " " or peça.isupper() != POSICAO_PECAS[row - 1][col].isupper()):
                movimentos.append((row - 1, col))
            if row - 1 >= 0 and col + 1 < 8 and (POSICAO_PECAS[row - 1][col + 1] == " " or peça.isupper() != POSICAO_PECAS[row - 1][col + 1].isupper()):
                movimentos.append((row - 1, col + 1))
            if col - 1 >= 0 and (POSICAO_PECAS[row][col - 1] == " " or peça.isupper() != POSICAO_PECAS[row][col - 1].isupper()):
                movimentos.append((row, col - 1))
            if col + 1 < 8 and (POSICAO_PECAS[row][col + 1] == " " or peça.isupper() != POSICAO_PECAS[row][col + 1].isupper()):
                movimentos.append((row, col + 1))
            if row + 1 < 8 and col - 1 >= 0 and (POSICAO_PECAS[row + 1][col - 1] == " " or peça.isupper() != POSICAO_PECAS[row + 1][col - 1].isupper()):
                movimentos.append((row + 1, col - 1))
            if row + 1 < 8 and (POSICAO_PECAS[row + 1][col] == " " or peça.isupper() != POSICAO_PECAS[row + 1][col].isupper()):
                movimentos.append((row + 1, col))
            if row + 1 < 8 and col + 1 < 8 and (POSICAO_PECAS[row + 1][col + 1] == " " or peça.isupper() != POSICAO_PECAS[row + 1][col + 1].isupper()):
                movimentos.append((row + 1, col + 1))      
        
        return movimentos
        
