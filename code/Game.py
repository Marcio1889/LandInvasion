import pygame

from code.Menu import Menu
from code.Phase import Phase
from code.const import WIND_WIDTH, WIND_HEIGHT


class Game:
    def __init__(self):
        pygame.init()  # Iniciando o Pygame
        self.window = pygame.display.set_mode(size=(WIND_WIDTH, WIND_HEIGHT))  # Criando a janela do Pygame


    def run(self):


        while True:# Mantendo a Janela aberta
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == 'NEW GAME':
                phase = Phase(self.window, 'FP1', menu_return)
                phase_return = phase.run()
            elif menu_return == 'SCORE':
                pass

            elif menu_return == 'QUIT GAME':
                pygame.quit()  # Fecha a Janela
                quit()  # Encerra o pygame

