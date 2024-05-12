import pygame
from const import *

class Menu_partida:
    def __init__(self):
        # Inicialize quaisquer atributos necessários para o display lateral
        self.fonte = fonte = pygame.font.SysFont('Segoe UI Symbol', TAMANHO_QUADRADO//5, True, False)
        self.texto_voltar = self.fonte.render('Voltar Jogada', True, (70, 120, 95))
        self.botao_voltar = self.texto_voltar.get_rect(center=(TAMANHO+TAMANHO/8, TAMANHO/1.5+TAMANHO/12))
        self.texto_reiniciar = self.fonte.render('Reiniciar', True, (70, 120, 95))
        self.botao_reiniciar = self.texto_reiniciar.get_rect(center=(TAMANHO+TAMANHO/3, TAMANHO/1.5+TAMANHO/12))
        self.texto_ver_movimentos = self.fonte.render('Ver Movimentos', True, (70, 120, 95))
        self.botao_ver_movimentos = self.texto_ver_movimentos.get_rect(center=(TAMANHO+TAMANHO/8, TAMANHO/1.5+TAMANHO/6))
        self.texto_histotico = []
   
    def desenhar(self, tela):
        titulo = self.fonte.render(f'Histórico de Movimentos: ', True, (70, 120, 95))
        pygame.draw.rect(tela, (234, 235, 200), (TAMANHO+5, 0, TAMANHO/2, TAMANHO/1.5))
        tela.blit(titulo, (TAMANHO+TAMANHO/7.9, 30))
        if self.texto_histotico != []:
            col = 20
            lin = 0
            for i, movimento in enumerate(self.texto_histotico):
                if i%2 == 0:
                    texto = self.fonte.render(f'{i+1}. {movimento}', True, (70, 120, 95))
                    tela.blit(texto, (TAMANHO+col, 50 + lin * 20))
                else:
                    texto = self.fonte.render(f'{movimento}', True, (70, 120, 95))
                    tela.blit(texto, (TAMANHO+col+70, 50 + lin * 20))
                    lin+=1
                if i in [31,61]:
                    col+=140
                    lin=0
                    
        else:
            texto = self.fonte.render('Nenhum movimento ainda', True, (70, 120, 95))
            tela.blit(texto, (TAMANHO+TAMANHO/8.3, 60))
            
        # Desenhar botão de voltar jogada
        
        pygame.draw.rect(tela, (234, 235, 200), (TAMANHO+5, TAMANHO/1.5+5, TAMANHO/2,TAMANHO/3.2 ))
        tela.blit(self.texto_voltar, self.botao_voltar)
        tela.blit(self.texto_reiniciar, self.botao_reiniciar)
        tela.blit(self.texto_ver_movimentos, self.botao_ver_movimentos)
        
    def formatar_historico(self, dados_historico, historico):
        tabuleiro = historico[-1]
        dado = dados_historico[-1]
        if dado[0] == 'p' or dado[0] == 'P':
            texto = f'{CASAS[dado[3]]}{abs(dado[4]-8)}'
        else:
            texto = f'{SIMBOLOS[dado[0]]}{CASAS[dado[3]]}{abs(dado[4]-8)}'
            
        if tabuleiro[dado[4]][dado[3]] != " ":
            if dado[0] == 'p' or dado[0] == 'P':
                texto = f'{CASAS[dado[2]]}x{CASAS[dado[3]]}{abs(dado[4]-8)}'
            else:
                texto = f'{SIMBOLOS[dado[0]]}x{CASAS[dado[3]]}{abs(dado[4]-8)}'
            
        self.texto_histotico.append(texto)