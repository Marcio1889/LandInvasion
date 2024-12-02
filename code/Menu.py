import pygame
from pygame import Surface, Rect
from pygame.examples.grid import WINDOW_WIDTH
from pygame.font import Font

from code.const import COLOR_ORANGE, MENU_OPTION, COLOR_WHITE, WIND_WIDTH, COLOR_YELLOW


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/Image.Menu.png')
        self.rect = self.surf.get_rect(left=0, top=0) # Colocando a imagem dentro de um retangulo


    def run(self):
            pygame.mixer_music.load('./asset/Music.Menu.mp3') # definindo a musica do menu
            pygame.mixer_music.play(-1) # deixando a musica tocar infinatamente

            while True:
                self.window.blit(source=self.surf, dest=self.rect) # Fundo do Menu
                self.menu_text(80, "Land", COLOR_YELLOW, ((WINDOW_WIDTH / 2), 70))
                self.menu_text(80, "Invasion",COLOR_YELLOW, ((WINDOW_WIDTH / 2), 120))

                for i in range(len(MENU_OPTION)): # configurando as opções do Menu
                    self.menu_text(30, MENU_OPTION[i], COLOR_ORANGE, ((WIND_WIDTH / 2), 230 + 60 * i))


                pygame.display.flip()

                for event in pygame.event.get():  # Criando evento pra fechar a janela
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()  # Encerrando o pygame

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple, shadow_color:
        tuple = (0, 0, 0), shadow_offset: tuple = (2,2)):
        text_font: Font = pygame.font.SysFont(name="Baskerville", size=text_size)
        shadow_surf: Surface = text_font.render(text, True, shadow_color).convert_alpha()
        shadow_rect: Rect = shadow_surf.get_rect(center=(text_center_pos[0] + shadow_offset[0], text_center_pos[1] + shadow_offset[1]))
        self.window.blit(source=shadow_surf, dest=shadow_rect)

        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)