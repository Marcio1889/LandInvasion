from code.Entity import Entity
from code.const import ENTITY_SPEED


class PlayerPower(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        self.rect.centerx += ENTITY_SPEED[self.name] # definindo a posição dos tiros