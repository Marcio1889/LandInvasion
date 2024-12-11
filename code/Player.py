
import pygame


from code.Entity import Entity
from code.PlayerPower import PlayerPower
from code.const import ENTITY_SPEED, WIND_WIDTH, WIND_HEIGHT, PLAYER_KEY_POWER, ENTITY_POWER_DELAY

class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.health = 100
        self.score = 0
        self.invincible_time = 0
        self.images = {
            "up": pygame.image.load('./asset/Player_up.png').convert_alpha(),
            "down": pygame.image.load('./asset/Player_down.png').convert_alpha(),
            "right": pygame.image.load('./asset/Player_right.png').convert_alpha(),
            "default": pygame.image.load('./asset/player1.png').convert_alpha(),
        }
        self.power_delay = ENTITY_POWER_DELAY[self.name]

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

    def power(self):
        """Verifica se a tecla de poder foi pressionada e gera um tiro"""
        self.power_delay -= 1
        if self.power_delay == 0:
            self.power_delay = ENTITY_POWER_DELAY[self.name]
            pressed_key = pygame.key.get_pressed()
            if pressed_key[PLAYER_KEY_POWER[self.name]]:
                return PlayerPower(name=f'{self.name}Power', position=(self.rect.centerx, self.rect.centery))
