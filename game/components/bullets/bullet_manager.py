from game.utils.constants import SHIELD_TYPE


class BulletManager:
    def __init__(self):
        self.bullets = []
        self.enemy_bullets = []

    def update(self, game):
        # eliminate the bullet and the Player
        for bullet in self.enemy_bullets:
            bullet.update(self.enemy_bullets, game.player.rotated_rect)
            if (bullet.rotated_rect.colliderect(game.player.rotated_rect)
                    and bullet.owner == "enemy"):
                self.enemy_bullets.remove(bullet)
                # if the player does not have a powerUp, die
                if game.player.power_up_type != SHIELD_TYPE:
                    game.player.lives -= 1  # takes life from the player
                if game.player.lives <= 0:
                    game.death_count.update()
                    game.playing = False
                    break

        # eliminate the bullet and the Enemy
        for bullet in self.bullets:
            bullet.update(self.bullets, game.user_cursor.rect.center)
            for enemy in game.enemy_manager.enemies:
                if (bullet.rotated_rect.colliderect(enemy.rotated_rect)
                        and bullet.owner == "player"):
                    self.bullets.remove(bullet)
                    game.enemy_manager.enemies.remove(enemy)
                    # updates the player score
                    game.score.update()
                    break

    def draw(self, screen):
        for bullet in self.enemy_bullets:
            bullet.draw(screen)
        for bullet in self.bullets:
            bullet.draw(screen)

    def add_bullet(self, bullet):
        if bullet.owner == "enemy" and len(self.enemy_bullets) < 10:
            self.enemy_bullets.append(bullet)
            bullet.rotate_bullet()  # rotate the enemy bullet to the player position
        if bullet.owner == "player" and len(self.bullets) < 5:
            self.bullets.append(bullet)
            bullet.rotate_bullet()

    def reset(self):
        self.bullets = []
        self.enemy_bullets = []
