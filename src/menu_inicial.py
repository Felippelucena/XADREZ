import pygame
import sys

class Menu_inicial:
    
    def __init__(self, tela, largura_tela, altura_tela):
        self.tela = tela
        self.fonte = pygame.font.Font(None, 36)
        self.texto_novo_jogo = self.fonte.render("Novo Jogo", True, (0, 0, 0))
        self.retangulo_novo_jogo = self.texto_novo_jogo.get_rect(center=(largura_tela/2, altura_tela/2))
   
    def iniciar(self):
        while True:
            self.tela.fill((255, 255, 255))
            self.tela.blit(self.texto_novo_jogo, self.retangulo_novo_jogo)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Botão esquerdo do mouse
                        if self.retangulo_novo_jogo.collidepoint(event.pos):
                            return