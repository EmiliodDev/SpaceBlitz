from game.components.enemies.enemy import Enemy
from game.components.enemies.enemy_types.assault import Assault


class EnemyManager:
    def __init__(self):
        self.enemies = []

    def update(self, game):
        self.add_enemy()

        for enemy in self.enemies:
            enemy.update(self.enemies, game)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self):
        num_assault = sum(isinstance(enemy, Assault)for enemy in self.enemies)
        if num_assault < 2:
            enemy_assault = Assault()
            self.enemies.append(enemy_assault)

        num_enemies = sum(isinstance(enemy, Enemy) for enemy in self.enemies)
        if num_enemies >= 2 and num_assault < 2:
            enemy = Enemy()
            self.enemies.append(enemy)

    def reset(self):
        self.enemies = []
