from aviso.avisoRunIA import avisoRunIA
from aviso.avisoRun import avisoRun
from loader.loadMenu import *

LOOP = True

IMAGEM_RUN_IA = pygame.image.load('imgs/btn_ia.png').convert_alpha() 
RUN_IA = Botao(50, 250, IMAGEM_RUN_IA, 0.8)

IMAGEM_RUN = pygame.image.load('imgs/btn_jogar.png').convert_alpha()
RUN = Botao(50, 400, IMAGEM_RUN, 0.8)

IMAGEM_LOGO = pygame.image.load('imgs/logo.png').convert_alpha()
LOGO = Botao(50, 500, IMAGEM_LOGO, 0.8)

if __name__ == '__main__':
    while LOOP:
        FPS.tick(60)
        LOGO_FLAPPY.clique(TELA)
        LOGO.clique(TELA)

        if RUN_IA.clique(TELA): 
            avisoRunIA()
            LOOP = False
        
        if RUN.clique(TELA): 
            avisoRun()
            LOOP = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                LOOP = False

        pygame.display.update()
    pygame.quit()