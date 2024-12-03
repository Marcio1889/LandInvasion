from code.Entity import Entity
from code.const import WIND_WIDTH, ENTITY_SPEED


class Background(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name] # Definindo a velocidade das imagens de fundo
        if self.rect.right <= 0:
            self.rect.left = WIND_WIDTH
        pass