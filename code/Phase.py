import random
import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.EntityFactory import EntityFactory
from code.const import COLOR_WHITE, WIND_HEIGHT, EVENT_ENEMY, SPAWN_TIME


class Phase:

    def __init__(self, window, name, game_mode):
        self.timeout = 20000  # 20 segundos
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list =  []

        self.entity_list.extend(EntityFactory.get_entity('ImageFP'))
        self.entity_list.append(EntityFactory.get_entity('Player'))
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME) #Geração do evento Inimigo

    def run(self):
        pygame.mixer_music.load(f'./asset/Music_FP.mp3') # Definindo a Musica da PF
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(30) # Definindo a velocidade do jogo
            for ent in self.entity_list:
                if ent is None:
                    continue

                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2')) #Metodo choice sorteia o inimigo
                    self.entity_list.append(EntityFactory.get_entity(choice))


            self.phase_text(18, f'{self.name} - Timeout: {self.timeout / 1000 :.1f}s', COLOR_WHITE, (10, 5))
            self.phase_text(18, f'fps:{clock.get_fps() :.0f}', COLOR_WHITE, (10, WIND_HEIGHT - 35))
            self.phase_text(18, f'entidades: {len(self.entity_list)}', COLOR_WHITE, (10, WIND_HEIGHT - 20))
            pygame.display.flip()
        pass

    def phase_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucinda Sans Typewriter", size= text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)

