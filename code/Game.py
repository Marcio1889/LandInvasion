from tkinter import Menu

import pygame

class Game:
    def __init__(self):
        self.window = None
        pygame.init()  # Iniciando o Pygame
        window = pygame.display.set_mode(size=(800, 600))  # Criando a janela do Pygame


    def run(self):
        while True:# Mantendo a Janela aberta
            menu = Menu(self.window)
            menu.run()
            pass
           # for event in pygame.event.get(): # Criando evento pra fechar a janela
           #     if event.type == pygame.QUIT:
           #         pygame.quit()
           #         quit() # Encerrando o pygame
