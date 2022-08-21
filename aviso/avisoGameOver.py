from loader.loadMenu import *

IMAGEM_GAME_OVER = pygame.image.load('imgs/msg_gameOver.png').convert_alpha()
AVISO = Botao(50, 350, IMAGEM_GAME_OVER, 0.8)

def gameOver():
    LOOP = True

    while LOOP:
        FPS.tick(60)
        LOGO_FLAPPY.clique(TELA)

        if AVISO.clique(TELA):
            LOOP = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                LOOP = False

        pygame.display.update()
    pygame.quit()    