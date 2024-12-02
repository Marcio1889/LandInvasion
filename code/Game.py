from code.Menu import Menu

import pygame

from code.const import WIND_WIDTH, WIND_HEIGHT


class Game:
    def __init__(self):
        pygame.init()  # Iniciando o Pygame
        self.window = pygame.display.set_mode(size=(WIND_WIDTH, WIND_HEIGHT))  # Criando a janela do Pygame


    def run(self):


        while True:# Mantendo a Janela aberta
            menu = Menu(self.window)
            menu.run()
            pass


