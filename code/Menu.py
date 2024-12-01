import pygame


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/Image.Menu.png')
        self.rect = self.surf.get_rect(left=0, top=0) # Colocando a imagem dentro de um retangulo


    def run(self):
            self.window.blit(source=self.surf, dest=self.rect)
            pygame.display.flip()


            for event in pygame.event.get(): # Criando evento pra fechar a janela
               if event.type == pygame.QUIT:
                   pygame.quit()
                   quit() # Encerrando o pygame


