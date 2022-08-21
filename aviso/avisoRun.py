from execucao.run import mainRun
from loader.loadMenu import *

IMAGEM_ENTER = pygame.image.load('imgs/msg_espaco.png').convert_alpha()
AVISO = Botao(50, 200, IMAGEM_ENTER, 0.8)

def avisoRun():
    LOOP = True
    TELA.blit(IMAGEM_BACKGROUND, (0, 0))

    while LOOP:
        FPS.tick(60)
        AVISO.clique(TELA)
        LOGO_FLAPPY.clique(TELA)

        if INICIAR.clique(TELA): 
            mainRun()
            LOOP = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                LOOP = False

        pygame.display.update()
    pygame.quit()    