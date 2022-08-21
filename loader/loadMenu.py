import os
import pygame

from classes.Botao import Botao

TELA_LARGURA = 500
TELA_ALTURA = 800

FPS = pygame.time.Clock()
TELA = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA))

IMAGEM_BACKGROUND = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bg.png')))
TELA.blit(IMAGEM_BACKGROUND, (0, 0))

IMAGEM_LOGO_FLAPPY = pygame.image.load('imgs/logo_flappy.png').convert_alpha()
LOGO_FLAPPY = Botao(50, 50, IMAGEM_LOGO_FLAPPY, 0.8)

IMAGEM_INICIAR = pygame.image.load('imgs/btn_iniciar.png').convert_alpha()
INICIAR = Botao(50, 500, IMAGEM_INICIAR, 0.8)