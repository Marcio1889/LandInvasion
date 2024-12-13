
import random
from code.Background import Background
from code.Enemy import Enemy
from code.Player import Player
from code.const import WIND_WIDTH, WIND_HEIGHT


class EntityFactory:
    # Fábrica de Entidades - Responsável por criar e retornar diferentes tipos de entidades.

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        # Retorna a entidade solicitada com base no nome e posição fornecidos

        if entity_name == 'ImageFP':
            return EntityFactory._create_background_images()

        elif entity_name == 'Player':
            return Player('Player1', (10, WIND_HEIGHT / 2))

        elif entity_name == 'Enemy1' or entity_name == 'Enemy2':
            return EntityFactory._create_enemy(entity_name)

        else:
            raise ValueError(f"Entity '{entity_name}' not recognized.")

    @staticmethod
    def _create_background_images():
        # Cria a lista de imagens de fundo (Backgrounds).
        list_bg = []
        for i in range(11):  # Número de imagens da FP
            list_bg.append(Background(f'ImageFP{i}', (0, 0)))
            list_bg.append(Background(f'ImageFP{i}', (WIND_WIDTH, 0)))
        return list_bg

    @staticmethod
    def _create_enemy(enemy_name: str):
        # Cria e retorna um inimigo com base no nome.
        return Enemy(enemy_name, (WIND_WIDTH + 10, random.randint(60, WIND_HEIGHT - 60)))
