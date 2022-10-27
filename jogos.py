import time

import pygame
import sys
from cobrinha import Cobra
from comida import Comida

pygame.font.init()
minha_fonte = pygame.font.SysFont('Arial', 15)



pygame.init()
TAM_TELA = (300, 400)
tela = pygame.display.set_mode(TAM_TELA)
tempo = pygame.time.Clock()
cobra = Cobra()
comida = Comida()
posicao_comida = comida.posicao
pontuaçao = 0

# iniciando o loop do jogo

while True:
    tela.fill((7, 0, 10))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                cobra.mudar_direcao("direita")
            if event.key == pygame.K_LEFT:
                cobra.mudar_direcao("esquerda")
            if event.key == pygame.K_UP:
                cobra.mudar_direcao("cima")
            if event.key == pygame.K_DOWN:
                cobra.mudar_direcao("baixo")
    posicao_comida = comida.gera_nova_posicao()

    if cobra.mover(posicao_comida):
        comida.devorada = True
        pontuaçao += 1

    if cobra.verifica_colisao():
        voce_perdeu = minha_fonte.render('GAME OVER', True, (255, 255, 255))
        tela.blit(voce_perdeu, (80, 100))
        pygame.display.flip()

        time.sleep(2)
        pygame.quit()
        sys.exit()


    pontos = minha_fonte.render(f'Pontuaçao: {pontuaçao}', True, (255,255,255))
    tela.blit(pontos, (10, 10))


    for posi in cobra.corpo:
        pygame.draw.rect(tela,pygame.Color(255,204,0),
                         pygame.Rect(posi[0], posi[1], 10, 10))

        pygame.draw.rect(tela, pygame.Color(255, 0, 0),
                         pygame.Rect(posicao_comida[0], posicao_comida[1], 10, 10))

    pygame.display.update()
    tempo.tick(10)