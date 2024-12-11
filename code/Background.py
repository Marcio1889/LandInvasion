# from code.Entity import Entity
# from code.const import WIND_WIDTH, ENTITY_SPEED
#
#
# class Background(Entity):
#
#     def __init__(self, name: str, position: tuple):
#         super().__init__(name, position)
#
#     def move(self):
#         self.rect.centerx -= ENTITY_SPEED[self.name] # Definindo a velocidade das imagens de fundo
#         if self.rect.right <= 0:
#             self.rect.left = WIND_WIDTH
#         pass

from code.Entity import Entity
from code.const import WIND_WIDTH, ENTITY_SPEED


class Background(Entity):

    def __init__(self, name: str, position: tuple):

        # Inicializa uma instância do fundo.
        # :param name: Nome do fundo, usado para associar velocidade.
        # :param position: Posição inicial do fundo.

        super().__init__(name, position)

    def move(self):
        # Move o fundo horizontalmente com base na velocidade definida.
        # Se sair da tela pela esquerda, reposiciona à direita para criar o efeito de rolagem infinita.

        self.rect.centerx -= ENTITY_SPEED.get(self.name, 0)  # Garante um fallback de velocidade zero
        if self.rect.right <= 0:
            self.rect.left = WIND_WIDTH
