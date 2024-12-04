from abc import ABC

from code.EnemyPower import EnemyPower
from code.Entity import Entity
from code.const import ENTITY_SPEED, WIND_WIDTH, ENTITY_POWER_DELAY


class Enemy(Entity, ABC):
     def __init__(self, name: str, position: tuple):
         super().__init__(name, position)
         self.power_delay = ENTITY_POWER_DELAY[self.name]

     def move(self):
         self.rect.centerx -= ENTITY_SPEED[self.name]

     def power(self):
         self.power_delay -= 1 # configurando a volocidade de tiro do inimigo
         if self.power_delay == 0:
             self.power_delay = ENTITY_POWER_DELAY[self.name]
             return EnemyPower(name=f'{self.name}Power', position=(self.rect.centerx, self.rect.centery))

