
import pygame
from abc import ABC, abstractmethod
from code.const import ENTITY_HEALTH, ENTITY_DAMAGE, ENTITY_SCORE


class Entity(ABC):
    # Classe base para todas as entidades no jogo .

    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load(f'./asset/{name}.png').convert_alpha()
        self.rect = self.surf.get_rect(left=position[0], top=position[1])

        # Inicializa os atributos básicos da entidade com base no nome
        self.speed = 0
        self.health = ENTITY_HEALTH.get(self.name, 100)  # Valor padrão se não encontrar no dicionário
        self.damage = ENTITY_DAMAGE.get(self.name, 10)  # Valor padrão se não encontrar no dicionário
        self.score = ENTITY_SCORE.get(self.name, 0)  # Valor padrão se não encontrar no dicionário
        self.last_dmg = None

    @abstractmethod
    def move(self):
        pass
