
from code.Entity import Entity
from code.EnemyPower import EnemyPower
from code.const import ENTITY_SPEED, ENTITY_POWER_DELAY


class Enemy(Entity):
    # Classe que representa um inimigo no jogo, derivada da classe base Entity

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        # Configura o delay de poder do inimigo, que afeta a frequência de disparo
        self.power_delay = ENTITY_POWER_DELAY.get(self.name, 30)  # Valor padrão de 30 se não estiver no dicionário

    def move(self):
        # Move o inimigo para a esquerda com base na velocidade configurada.
        self.rect.centerx -= ENTITY_SPEED.get(self.name, 5)  # Valor padrão de 5 se não estiver no dicionário

    def power(self):
        # Controla o poder de disparo do inimigo, retornando um novo poder (tiro) se o delay de poder atingir 0.

        self.power_delay -= 1  # Diminui o delay de poder a cada ciclo
        if self.power_delay == 0:
            self.power_delay = ENTITY_POWER_DELAY.get(self.name, 30)  # Reseta o delay de poder
            # Retorna um novo poder (tiro) do inimigo
            return EnemyPower(name=f'{self.name}Power', position=(self.rect.centerx, self.rect.centery))
