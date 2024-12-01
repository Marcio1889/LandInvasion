from code.Menu import Menu

import pygame

from code.const import WIND_WIDTH, WIND_HEIGHT


class Game:
    def __init__(self):
        pygame.init()  # Iniciando o Pygame
        print("Inicializando o jogo...")
        self.window = pygame.display.set_mode(size=(WIND_WIDTH, WIND_HEIGHT))  # Criando a janela do Pygame
        print("Finalizando o jogo...")


    def run(self):
        pygame.mixer_music.load('./asset/Music.Menu.mp3') # definindo a musica do menu
        pygame.mixer_music.play(-1)# definindo o tempo da musica

        while True:# Mantendo a Janela aberta
            menu = Menu(self.window)
            menu.run()
            pass


