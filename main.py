import pygame

pygame.init() # Iniciando o Pygame
window = pygame.display.set_mode(size=(800, 600)) # Criando a janela do Pygame

while True: # Mantendo a Janela aberta
    for event in pygame.event.get(): # Criando evento pra fechar a janela
        if event.type == pygame.QUIT:
            pygame.quit()
            quit() # Encerrando o pygame

