
from code.Enemy import Enemy
from code.EnemyPower import EnemyPower
from code.Entity import Entity
from code.Player import Player
from code.PlayerPower import PlayerPower
from code.const import WIND_WIDTH


class EntityMediator:

    @staticmethod
    def verify_collision_window(ent: Entity):
        # Verifica se a entidade ultrapassou os limites da janela
        if isinstance(ent, Enemy):
            if ent.rect.right <= 0:  # Se o inimigo saiu pela esquerda
                ent.health = 0
        if isinstance(ent, PlayerPower):
            if ent.rect.left >= WIND_WIDTH:  # Se o poder do jogador saiu pela direita
                ent.health = 0
        if isinstance(ent, EnemyPower):
            if ent.rect.right <= 0:  # Se o poder do inimigo saiu pela esquerda
                ent.health = 0

    @staticmethod
    def __verify_collision_entity(ent1: Entity, ent2: Entity):
        # Verifica as colisões entre as entidades
        vali_interaction = False

        # Definir interações válidas
        if isinstance(ent1, Enemy) and isinstance(ent2, PlayerPower):
            vali_interaction = True
        if isinstance(ent1, PlayerPower) and isinstance(ent2, EnemyPower):
            vali_interaction = True
        if isinstance(ent1, Player) and isinstance(ent2, EnemyPower):
            vali_interaction = True
        if isinstance(ent1, EnemyPower) and isinstance(ent2, Player):
            vali_interaction = True

        if vali_interaction:
            # Verifica a colisão (AABB: Axis-Aligned Bounding Box)
            if (ent1.rect.right >= ent2.rect.left and
                    ent1.rect.left <= ent2.rect.right and
                    ent1.rect.bottom >= ent2.rect.top and
                    ent1.rect.top <= ent2.rect.bottom):
                # Aplica dano mútuo entre as entidades
                ent1.health -= ent2.damage
                ent2.health -= ent1.damage

                # Registra quem causou o dano
                ent1.last_dmg = ent2.name
                ent2.last_dmg = ent1.name

    @staticmethod
    def __offer_score(enemy: Enemy, entity_list: list[Entity]):
        # Oferece pontos ao jogador que derrotou o inimigo
        if enemy.last_dmg == 'Player1Power':  # Verifica se foi o Player1Power que causou o dano
            for ent in entity_list:
                if ent.name == 'Player1':
                    ent.score += enemy.score

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        # Verifica as colisões entre todas as entidades na lista
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.verify_collision_window(entity1)  # Verifica se saiu da janela

            for j in range(i + 1, len(entity_list)):
                entity2 = entity_list[j]
                EntityMediator.__verify_collision_entity(entity1, entity2)  # Verifica a colisão entre as entidades

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        # Verifica a saúde das entidades e remove as que morreram
        for ent in entity_list:
            if isinstance(ent, Player):
                if ent.invincible_time > 0:
                    ent.invincible_time -= 1  # Diminui o tempo de invencibilidade

            if ent.health <= 0:
                if isinstance(ent, Enemy):
                    EntityMediator.__offer_score(ent, entity_list)  # Oferece pontos ao jogador
                entity_list.remove(ent)  # Remove a entidade se a saúde for zero
