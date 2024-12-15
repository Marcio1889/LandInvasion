
import pygame
from pygame import Surface, Rect
from pygame.font import Font
from code.const import COLOR_ORANGE, MENU_OPTION, COLOR_WHITE, COLOR_YELLOW, WIND_WIDTH


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/Image.Menu.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)  # Colocando a imagem dentro de um retângulo

    def run(self):
        menu_option = 0
        pygame.mixer_music.load('./asset/Music.Menu.mp3')  # Definindo a música do menu
        pygame.mixer_music.play(-1)  # Deixando a música tocar infinitamente

        while True:
            # Desenha as imagens
            self.window.blit(source=self.surf, dest=self.rect)  # Fundo do Menu
            self.menu_text(90, "Land", COLOR_YELLOW, (WIND_WIDTH / 2, 80))
            self.menu_text(90, "Invasion", COLOR_YELLOW, (WIND_WIDTH / 2, 130))

            for i in range(len(MENU_OPTION)):  # Configurando as fontes do Menu
                if i == menu_option:
                    self.menu_text(40, MENU_OPTION[i], COLOR_ORANGE, (WIND_WIDTH / 2, 240 + 60 * i))
                else:
                    self.menu_text(40, MENU_OPTION[i], COLOR_WHITE, (WIND_WIDTH / 2, 240 + 60 * i))

            for event in pygame.event.get():  # Criando evento pra fechar a janela
                if event.type == pygame.QUIT:
                    pygame.mixer_music.stop()
                    pygame.quit()
                    quit()  # Encerrando o pygame
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:  # Navega para baixo no menu
                        menu_option = (menu_option + 1) % len(MENU_OPTION)
                    if event.key == pygame.K_UP:  # Navega para cima no menu
                        menu_option = (menu_option - 1) % len(MENU_OPTION)
                    if event.key == pygame.K_RETURN:  # Seleciona uma opção
                        return MENU_OPTION[menu_option]

            pygame.display.flip()

    def menu_text(
        self,
        text_size: int,
        text: str,
        text_color: tuple,
        text_center_pos: tuple,
        shadow_color: tuple = (0, 0, 0),
        shadow_offset: tuple = (2, 2)
    ):
        # Desenhando o texto no menu com sombra
        text_font: Font = pygame.font.SysFont(name="Baskerville", size=text_size)
        # Renderiza a sombra
        shadow_surf: Surface = text_font.render(text, True, shadow_color).convert_alpha()
        shadow_rect: Rect = shadow_surf.get_rect(
            center=(text_center_pos[0] + shadow_offset[0], text_center_pos[1] + shadow_offset[1])
        )
        self.window.blit(source=shadow_surf, dest=shadow_rect)
        # Renderiza o texto
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

