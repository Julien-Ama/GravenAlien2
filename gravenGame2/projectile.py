import pygame


class Projectile(pygame.sprite.Sprite):

    def __init__(self, player):
        super().__init__()
        self.velocity = 5
        self.player = player
        self.image = pygame.image.load("ressourceG/projectile.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 100
        self.rect.y = player.rect.y + 50
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        #     tourner le projectile
        self.angle += 12
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self):
        self.rect.x += self.velocity
        self.rotate()

        # verifier que le projectile entre en collision avec le monstre
        for monster in  self.player.game.check_collision(self, self.player.game.all_monsters):
            #     supprimer le projectile
            self.remove()
        #     infliger degats
            monster.damage(self.player.attack)

        # verifier si le projectile n'est plus présent a l'ecran
        if self.rect.x > 1080:
            # supprimer le preojectile (en dehors de l'ecran)
            self.remove()
            print("Projectiles supprimé !")
