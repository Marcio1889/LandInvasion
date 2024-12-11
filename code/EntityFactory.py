import random

from code.Background import Background
from code.Enemy import Enemy
from code.Player import Player
from code.const import WIND_WIDTH, WIND_HEIGHT


class EntityFactory:


    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'ImageFP':
                list_bg = []
                for i in range(11): # Numero de imagens da FP
                    list_bg.append(Background(f'ImageFP{i}',(0,0)))
                    list_bg.append(Background(f'ImageFP{i}', (WIND_WIDTH, 0)))
                return list_bg

            case 'Player':
                return Player('Player1',(10, WIND_HEIGHT / 2))

            case 'Enemy1':
                return Enemy('Enemy1',(WIND_WIDTH + 10, random.randint(60, WIND_HEIGHT - 60)))

            case 'Enemy2':
                return Enemy('Enemy2', (WIND_WIDTH + 10, random.randint(60, WIND_HEIGHT - 60)))


