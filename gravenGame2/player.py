import pygame
from projectile import Projectile


class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load("ressourceG/playerG.png")
        self.rect = self.image.get_rect()
        self.rect.x = 20
        self.rect.y = 425

    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount
        else:
    #         si le joueur n'a plus de pts de vie
            self.game.game_over()

    def update_health_bar(self, surface):
        # dessiner barre de vie
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x, self.rect.y - 10, self.max_health, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x, self.rect.y - 10, self.health, 5])

    def launch_projectile(self):
        self.all_projectiles.add(Projectile(self))

    def move_right(self):
        # si pas de collision avec le joueur/monstres
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity
