from execucao.runIA import rodar
from loader.loadMenu import *

IMAGEM_ENTER = pygame.image.load('imgs/msg_enter.png').convert_alpha()
AVISO = Botao(50, 200, IMAGEM_ENTER, 0.8)

def avisoRunIA():
    LOOP = True
    TELA.blit(IMAGEM_BACKGROUND, (0, 0))

    while LOOP:
        FPS.tick(60)
        AVISO.clique(TELA)
        LOGO_FLAPPY.clique(TELA)

        if INICIAR.clique(TELA): 
            caminho = os.path.dirname(__file__)
            caminho_config = os.path.join(caminho, '../config/config.txt')
            rodar(caminho_config)
            LOOP = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                LOOP = False

        pygame.display.update()
    pygame.quit()    