

import pygame

from code.Menu import Menu
from code.Phase import Phase
from code.Score import Score
from code.const import WIND_WIDTH, WIND_HEIGHT


class Game:
    def __init__(self):
        pygame.init()  # Iniciando o Pygame
        self.window = pygame.display.set_mode(size=(WIND_WIDTH, WIND_HEIGHT))  # Criando a janela do Pygame


    def run(self):
        while True:# Mantendo a Janela aberta
            score = Score(self.window)
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == 'NEW GAME':
                player_score = [0]
                phase = Phase(self.window, 'FP1', menu_return, player_score)
                phase_return = phase.run(player_score)
                if phase_return:
                    score.save(menu_return, player_score)

            elif menu_return == 'SCORE':
                score.show()

            elif menu_return == 'QUIT GAME':
                pygame.quit()  # Fecha a Janela
                quit()  # Encerra o pygame


