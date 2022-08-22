import pygame
import os
import sys

from classes.Passaro import Passaro
from classes.Cano import Cano
from classes.Chao import Chao

TELA_LARGURA = 500
TELA_ALTURA = 800

IMAGEM_CANO = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'pipe.png')))
IMAGEM_CHAO = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'base.png')))
IMAGEM_BACKGROUND = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bg.png')))
IMAGENS_PASSARO = [
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird1.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird2.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird3.png'))),
]

if 'win' in sys.platform:
    extensao = '.wav'
else:
    extensao = '.ogg'

SONS = {
    'pulo': 'songs/pulo'+extensao,
    'morte': 'songs/morte'+extensao,
    'batida': 'songs/batida'+extensao,
}

pygame.font.init()
FONTE_PONTOS = pygame.font.SysFont('arial', 35)

def retornaSom(som):
    pygame.init()
    pygame.mixer.music.load(som)
    return pygame.mixer.music