# import random
# import sys
#
# import pygame
# from pygame import Surface, Rect
# from pygame.font import Font
#
# from code.Enemy import Enemy
# from code.EntityFactory import EntityFactory
# from code.EntityMediator import EntityMediator
# from code.Player import Player
# from code.const import COLOR_WHITE, WIND_HEIGHT, EVENT_ENEMY, SPAWN_TIME, COLOR_BLUE, EVENT_TIMEOUT, TIMEOUT_LEVEL, \
#     TIMEOUT_STEP
#
#
# class Phase:
#
#     def __init__(self, window, name, game_mode):
#         self.timeout = TIMEOUT_LEVEL
#         self.window = window
#         self.name = name
#         self.game_mode = game_mode
#         self.entity_list =  []
#
#         self.entity_list.extend(EntityFactory.get_entity('ImageFP'))
#         self.entity_list.append(EntityFactory.get_entity('Player'))
#         pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME) # Geração do evento Inimigo
#         pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP) # Criando evento de encerramento de fase
#
#     def run(self):
#         pygame.mixer_music.load(f'./asset/Music_FP.mp3') # Definindo a Musica da PF
#         pygame.mixer_music.play(-1)
#         clock = pygame.time.Clock()
#         while True:
#             clock.tick(70) # Definindo a velocidade do jogo
#             for ent in self.entity_list:
#                 if ent is None:
#                     continue
#
#                 self.window.blit(source=ent.surf, dest=ent.rect)
#                 ent.move()
#                 if isinstance(ent, (Player, Enemy)):
#                     power = ent.power()
#                     if power is not None:
#                        self.entity_list.append(power)
#                 if ent.name == 'Player1':
#                     self.phase_text(18, f'Player1  /  Health: {ent.health} / Score: {ent.score}',
#                                     COLOR_BLUE, (10, 25))
#
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     pygame.quit()
#                     sys.exit()
#                 if event.type == EVENT_ENEMY:
#                     choice = random.choice(('Enemy1', 'Enemy2')) #Metodo choice sorteia o inimigo
#                     self.entity_list.append(EntityFactory.get_entity(choice))
#                 if event.type == EVENT_TIMEOUT:
#                     self.timeout -= TIMEOUT_STEP
#                     if self.timeout <= 0:
#                         return True
#
#             self.phase_text(18, f'{self.name}  /  Timeout: {self.timeout / 1000 :.1f}s', COLOR_WHITE, (10, 5))
#             self.phase_text(18, f'fps: {clock.get_fps() :.0f}', COLOR_WHITE, (10, WIND_HEIGHT - 35))
#             self.phase_text(18, f'entidades: {len(self.entity_list)}', COLOR_WHITE, (10, WIND_HEIGHT - 20))
#             pygame.display.flip()
#
#             # Verificando a colisão
#             EntityMediator.verify_collision(entity_list=self.entity_list)
#             EntityMediator.verify_health(entity_list=self.entity_list)
#         pass
#
#     def phase_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
#         text_font: Font = pygame.font.SysFont(name="Lucinda Sans Typewriter", size= text_size)
#         text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
#         text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
#         self.window.blit(source=text_surf, dest=text_rect)

import random
import pygame
import sys
from pygame import Surface, Rect
from pygame.font import Font

from code.Enemy import Enemy
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Player import Player
from code.const import COLOR_WHITE, WIND_HEIGHT, EVENT_ENEMY, SPAWN_TIME, COLOR_BLUE, EVENT_TIMEOUT, \
    TIMEOUT_LEVEL, TIMEOUT_STEP


class Phase:

    def __init__(self, window, name, game_mode):
        self.timeout = TIMEOUT_LEVEL
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list = []

        self.entity_list.extend(EntityFactory.get_entity('ImageFP'))
        self.entity_list.append(EntityFactory.get_entity('Player'))
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)  # Geração do evento Inimigo
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)  # Criando evento de encerramento de fase

    def run(self):
        pygame.mixer_music.load(f'./asset/Music_FP.mp3')  # Definindo a Música da fase
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(70)  # Definindo a velocidade do jogo
            for ent in self.entity_list:
                if ent is None:
                    continue

                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                if isinstance(ent, (Player, Enemy)):
                    power = ent.power()
                    if power is not None:
                        self.entity_list.append(power)
                if ent.name == 'Player1':
                    self.phase_text(18, f'Player1  /  Health: {ent.health} / Score: {ent.score}',
                                    COLOR_BLUE, (10, 25))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(['Enemy1', 'Enemy2'])  # Método choice sorteia o inimigo
                    self.entity_list.append(EntityFactory.get_entity(choice))
                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP
                    if self.timeout <= 0:
                        return True

            self.phase_text(18, f'{self.name}  /  Timeout: {self.timeout / 1000 :.1f}s', COLOR_WHITE, (10, 5))
            self.phase_text(18, f'fps: {clock.get_fps() :.0f}', COLOR_WHITE, (10, WIND_HEIGHT - 35))
            self.phase_text(18, f'entidades: {len(self.entity_list)}', COLOR_WHITE, (10, WIND_HEIGHT - 20))
            pygame.display.flip()

            # Verificando a colisão
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

            # Verifica se o Player1 morreu e encerra a fase
            player1 = next((ent for ent in self.entity_list if isinstance(ent, Player) and ent.name == 'Player1'), None)
            if player1 and player1.health <= 0:
                return False  # Encerra a fase se o jogador morrer
        pass

    def phase_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        """Exibe o texto na tela em uma posição específica."""
        text_font: Font = pygame.font.SysFont(name="Lucinda Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
