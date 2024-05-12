import pygame
from const import *

class Peca:
    def __init__(self, tela):

        self.imagens = IMAGENS
        self.tela = tela


    def desenhar_peças(self, posicao_pecas):
        for lin in range(8):
            for col in range(8):
                peça = posicao_pecas[lin][col]
                if peça != " ":
                    # Carrega a imagem correspondente à peça
                    imagem = pygame.image.load(self.imagens[peça])
                    # Redimensiona a imagem para o tamanho do quadrado do tabuleiro
                    imagem = pygame.transform.scale(imagem, (TAMANHO_QUADRADO, TAMANHO_QUADRADO))
                    # Desenha a imagem na posição (lin, col)
                    self.tela.blit(imagem, (col * TAMANHO_QUADRADO, lin * TAMANHO_QUADRADO))



    def movimentos_possiveis(self, origem, posicao_pecas, ultimo_movimento):
        lin, col = origem
        peça = posicao_pecas[lin][col]

        movimentos = []

        if peça == "P":  # Peão branco
            # Verifica movimento para frente
            if posicao_pecas[lin - 1][col] == " ":
                movimentos.append((lin - 1, col))
                # Verifica movimento duplo no primeiro movimento
                if lin == 6 and posicao_pecas[lin - 2][col] == " ":
                    movimentos.append((lin - 2, col))
            # Verifica captura na diagonal
            if col > 0 and posicao_pecas[lin - 1][col - 1].islower():
                movimentos.append((lin - 1, col - 1))
            if col < 7 and posicao_pecas[lin - 1][col + 1].islower():
                movimentos.append((lin - 1, col + 1))
            if ultimo_movimento != []:
                if ultimo_movimento[1][0] == lin and abs(ultimo_movimento[0][0] - ultimo_movimento[1][0]) == 2:
                    if col > 0 and ultimo_movimento[1][1] == col - 1:
                        movimentos.append((lin - 1, col - 1))
                    if col < 7 and ultimo_movimento[1][1] == col + 1:
                        movimentos.append((lin - 1, col + 1))
        
        if peça == "p": # Peão preto
            # Verifica movimento para frente
            if posicao_pecas[lin + 1][col] == " ":
                movimentos.append((lin + 1, col))
                # Verifica movimento duplo no primeiro movimento
                if lin == 1 and posicao_pecas[lin + 2][col] == " ":
                    movimentos.append((lin + 2, col))
            # Verifica captura na diagonal
            if col > 0 and posicao_pecas[lin + 1][col - 1].isupper():
                movimentos.append((lin + 1, col - 1))
            if col < 7 and posicao_pecas[lin + 1][col + 1].isupper():
                movimentos.append((lin + 1, col + 1))
            if ultimo_movimento != []:
                if ultimo_movimento[1][0] == lin and abs(ultimo_movimento[0][0] - ultimo_movimento[1][0]) == 2:
                    if col > 0 and ultimo_movimento[1][1] == col - 1:
                        movimentos.append((lin + 1, col - 1))
                    if col < 7 and ultimo_movimento[1][1] == col + 1:
                        movimentos.append((lin + 1, col + 1))
        
        if peça == "T" or peça == "t":  # Torre
            
            # Verifica movimentos para cima
            for r in range(lin - 1, -1, -1):
                if posicao_pecas[r][col] == " ":
                    movimentos.append((r, col))
                else:
                    if peça.isupper() != posicao_pecas[r][col].isupper():
                        movimentos.append((r, col))
                    break
            # Verifica movimentos para baixo
            for r in range(lin + 1, 8):
                if posicao_pecas[r][col] == " ":
                    movimentos.append((r, col))
                else:
                    if peça.isupper() != posicao_pecas[r][col].isupper():
                        movimentos.append((r, col))
                    break
            # Verifica movimentos para a esquerda
            for c in range(col - 1, -1, -1):
                if posicao_pecas[lin][c] == " ":
                    movimentos.append((lin, c))
                else:
                    if peça.isupper() != posicao_pecas[lin][c].isupper():
                        movimentos.append((lin, c))
                    break
            # Verifica movimentos para a direita
            for c in range(col + 1, 8):
                if posicao_pecas[lin][c] == " ":
                    movimentos.append((lin, c))
                else:
                    if peça.isupper() != posicao_pecas[lin][c].isupper():
                        movimentos.append((lin, c))
                    break
        
        if peça == "C" or peça == "c":  # Cavalo
            if lin - 2 >= 0 and col - 1 >= 0 and (posicao_pecas[lin - 2][col - 1] == " " or peça.isupper() != posicao_pecas[lin - 2][col - 1].isupper()):
                movimentos.append((lin - 2, col - 1))
            if lin - 2 >= 0 and col + 1 < 8 and (posicao_pecas[lin - 2][col + 1] == " " or peça.isupper() != posicao_pecas[lin - 2][col + 1].isupper()):
                movimentos.append((lin - 2, col + 1))
            if lin - 1 >= 0 and col - 2 >= 0 and (posicao_pecas[lin - 1][col - 2] == " " or peça.isupper() != posicao_pecas[lin - 1][col - 2].isupper()):
                movimentos.append((lin - 1, col - 2))
            if lin - 1 >= 0 and col + 2 < 8 and (posicao_pecas[lin - 1][col + 2] == " " or peça.isupper() != posicao_pecas[lin - 1][col + 2].isupper()):
                movimentos.append((lin - 1, col + 2))
            if lin + 1 < 8 and col - 2 >= 0 and (posicao_pecas[lin + 1][col - 2] == " " or peça.isupper() != posicao_pecas[lin + 1][col - 2].isupper()):
                movimentos.append((lin + 1, col - 2))
            if lin + 1 < 8 and col + 2 < 8 and (posicao_pecas[lin + 1][col + 2] == " " or peça.isupper() != posicao_pecas[lin + 1][col + 2].isupper()):
                movimentos.append((lin + 1, col + 2))
            if lin + 2 < 8 and col - 1 >= 0 and (posicao_pecas[lin + 2][col - 1] == " " or peça.isupper() != posicao_pecas[lin + 2][col - 1].isupper()):
                movimentos.append((lin + 2, col - 1))
            if lin + 2 < 8 and col + 1 < 8 and (posicao_pecas[lin + 2][col + 1] == " " or peça.isupper() != posicao_pecas[lin + 2][col + 1].isupper()):
                movimentos.append((lin + 2, col + 1))
        
        if peça == "B" or peça == "b":  # Bispo
            # Verifica movimentos na diagonal principal
            r, c = lin - 1, col - 1
            while r >= 0 and c >= 0:
                if posicao_pecas[r][c] == " ":
                    movimentos.append((r, c))
                else:
                    if peça.isupper() != posicao_pecas[r][c].isupper():
                        movimentos.append((r, c))
                    break
                r -= 1
                c -= 1
            r, c = lin + 1, col + 1
            while r < 8 and c < 8:
                if posicao_pecas[r][c] == " ":
                    movimentos.append((r, c))
                else:
                    if peça.isupper() != posicao_pecas[r][c].isupper():
                        movimentos.append((r, c))
                    break
                r += 1
                c += 1
            # Verifica movimentos na diagonal secundária
            r, c = lin - 1, col + 1
            while r >= 0 and c < 8:
                if posicao_pecas[r][c] == " ":
                    movimentos.append((r, c))
                else:
                    if peça.isupper() != posicao_pecas[r][c].isupper():
                        movimentos.append((r, c))
                    break
                r -= 1
                c += 1
            r, c = lin + 1, col - 1
            while r < 8 and c >= 0:
                if posicao_pecas[r][c] == " ":
                    movimentos.append((r, c))
                else:
                    if peça.isupper() != posicao_pecas[r][c].isupper():
                        movimentos.append((r, c))
                    break
                r += 1
                c -= 1
        
        if peça == "D" or peça == "d":  # Dama
            # Verifica movimentos na horizontal e vertical
            for r in range(lin - 1, -1, -1):
                if posicao_pecas[r][col] == " ":
                    movimentos.append((r, col))
                else:
                    if peça.isupper() != posicao_pecas[r][col].isupper():
                        movimentos.append((r, col))
                    break
            for r in range(lin + 1, 8):
                if posicao_pecas[r][col] == " ":
                    movimentos.append((r, col))
                else:
                    if peça.isupper() != posicao_pecas[r][col].isupper():
                        movimentos.append((r, col))
                    break
            for c in range(col - 1, -1, -1):
                if posicao_pecas[lin][c] == " ":
                    movimentos.append((lin, c))
                else:
                    if peça.isupper() != posicao_pecas[lin][c].isupper():
                        movimentos.append((lin, c))
                    break
            for c in range(col + 1, 8):
                if posicao_pecas[lin][c] == " ":
                    movimentos.append((lin, c))
                else:
                    if peça.isupper() != posicao_pecas[lin][c].isupper():
                        movimentos.append((lin, c))
                    break
            # Verifica movimentos na diagonal principal
            r, c = lin - 1, col - 1
            while r >= 0 and c >= 0:
                if posicao_pecas[r][c] == " ":
                    movimentos.append((r, c))
                else:
                    if peça.isupper() != posicao_pecas[r][c].isupper():
                        movimentos.append((r, c))
                    break
                r -= 1
                c -= 1
            r, c = lin + 1, col + 1
            while r < 8 and c < 8:
                if posicao_pecas[r][c] == " ":
                    movimentos.append((r, c))
                else:
                    if peça.isupper() != posicao_pecas[r][c].isupper():
                        movimentos.append((r, c))
                    break
                r += 1
                c += 1
            # Verifica movimentos na diagonal secundária
            r, c = lin - 1, col + 1
            while r >= 0 and c < 8:
                if posicao_pecas[r][c] == " ":
                    movimentos.append((r, c))
                else:
                    if peça.isupper() != posicao_pecas[r][c].isupper():
                        movimentos.append((r, c))
                    break
                r -= 1
                c += 1
            r, c = lin + 1, col - 1
            while r < 8 and c >= 0:
                if posicao_pecas[r][c] == " ":
                    movimentos.append((r, c))
                else:
                    if peça.isupper() != posicao_pecas[r][c].isupper():
                        movimentos.append((r, c))
                    break
                r += 1
                c -= 1
                
        if peça == "R" or peça == "r":  # Rei
            if lin - 1 >= 0 and col - 1 >= 0 and (posicao_pecas[lin - 1][col - 1] == " " or peça.isupper() != posicao_pecas[lin - 1][col - 1].isupper()):
                movimentos.append((lin - 1, col - 1))
            if lin - 1 >= 0 and (posicao_pecas[lin - 1][col] == " " or peça.isupper() != posicao_pecas[lin - 1][col].isupper()):
                movimentos.append((lin - 1, col))
            if lin - 1 >= 0 and col + 1 < 8 and (posicao_pecas[lin - 1][col + 1] == " " or peça.isupper() != posicao_pecas[lin - 1][col + 1].isupper()):
                movimentos.append((lin - 1, col + 1))
            if col - 1 >= 0 and (posicao_pecas[lin][col - 1] == " " or peça.isupper() != posicao_pecas[lin][col - 1].isupper()):
                movimentos.append((lin, col - 1))
            if col + 1 < 8 and (posicao_pecas[lin][col + 1] == " " or peça.isupper() != posicao_pecas[lin][col + 1].isupper()):
                movimentos.append((lin, col + 1))
            if lin + 1 < 8 and col - 1 >= 0 and (posicao_pecas[lin + 1][col - 1] == " " or peça.isupper() != posicao_pecas[lin + 1][col - 1].isupper()):
                movimentos.append((lin + 1, col - 1))
            if lin + 1 < 8 and (posicao_pecas[lin + 1][col] == " " or peça.isupper() != posicao_pecas[lin + 1][col].isupper()):
                movimentos.append((lin + 1, col))
            if lin + 1 < 8 and col + 1 < 8 and (posicao_pecas[lin + 1][col + 1] == " " or peça.isupper() != posicao_pecas[lin + 1][col + 1].isupper()):
                movimentos.append((lin + 1, col + 1))      
        
        return movimentos
    
    def el_passant(self, lin, col, posicao_pecas, ultimo_movimento, origem_peca_selecionada):
        if origem_peca_selecionada == "P":
            if lin == 2 and col == ultimo_movimento[1][1] and ultimo_movimento[1][0] == 3:
                posicao_pecas[3][ultimo_movimento[1][1]] = " "
        elif origem_peca_selecionada == "p":
            if lin == 5 and col == ultimo_movimento[1][1] and ultimo_movimento[1][0] == 4:
                posicao_pecas[4][ultimo_movimento[1][1]] = " "

    def promocao_peao(self, lin, col, posicao_pecas,origem_peca_selecionada):
        if origem_peca_selecionada == "P" and lin == 0:
            posicao_pecas[lin][col] = "D"
        elif origem_peca_selecionada == "p" and lin == 7:
            posicao_pecas[lin][col] = "d"