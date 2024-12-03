from abc import ABC

from code.Entity import Entity
from code.const import ENTITY_SPEED, WIND_WIDTH


class Enemy(Entity, ABC):
     def __init__(self, name: str, position: tuple):
         super().__init__(name, position)

     def move(self):
         self.rect.centerx -= ENTITY_SPEED[self.name]
         if self.rect.right <= 0:
             self.rect.left = WIND_WIDTH