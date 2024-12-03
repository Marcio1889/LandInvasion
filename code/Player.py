from email.policy import default

import pygame

from code.Entity import Entity
from code.const import ENTITY_SPEED, WIND_WIDTH, WIND_HEIGHT


# class Player(Entity):
#
#     def __init__(self, name: str, position: tuple):
#         super().__init__(name, position)
#         pass
#
#     def move(self):
#         pressed_key = pygame.key.get_pressed() #Defininindo a movimentação da nave no player 1
#         if pressed_key[pygame.K_UP] and self.rect.top > 0:
#             self.rect.centery -= ENTITY_SPEED[self.name]
#         if pressed_key[pygame.K_DOWN] and self.rect.bottom < WIND_HEIGHT:
#             self.rect.centery += ENTITY_SPEED[self.name]
#         if pressed_key[pygame.K_LEFT] and self.rect.left > 0:
#             self.rect.centerx -= ENTITY_SPEED[self.name]
#         if pressed_key[pygame.K_RIGHT] and self.rect.right < WIND_WIDTH:
#             self.rect.centerx += ENTITY_SPEED[self.name]
#

class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.images = {
            "up": pygame.image.load('./asset/Player_up.png').convert_alpha(),
            "down": pygame.image.load('./asset/Player_down.png').convert_alpha(),
            "right": pygame.image.load('./asset/Player_right.png').convert_alpha(),
            "default": pygame.image.load('./asset/player1.png').convert_alpha(),
        }

    def move(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_UP] and self.rect.top > 0:
            self.rect.centery -= ENTITY_SPEED[self.name]
            self.surf = self.images["up"]  # Troca para imagem de "cima"
        elif pressed_key[pygame.K_DOWN] and self.rect.bottom < WIND_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.name]
            self.surf = self.images["down"]  # Troca para imagem de "baixo"
        elif pressed_key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
        elif pressed_key[pygame.K_RIGHT] and self.rect.right < WIND_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]
            self.surf = self.images["right"]
        else:
            self.surf = self.images["default"]






