import pygame
import random


class Monster(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.image = pygame.image.load("ressourceG/alien2.png")
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 425
        self.velocity = random.randint(1, 5)

    def damage(self, amount):
        #     infliger les degats (subir les les degats)
        self.health -= amount

        #     verifier si son nouveau nombre de pts de vies inferieur ou = à 0
        if self.health <= 0:
            #         reapparaitre comme un nouveau monstre
            self.rect.x = 1000 + random.randint(0, 300)
            self.velocity = random.randint(1, 5)
            self.health = self.max_health

            # si la barre d'evenement est chargé a son maximum
            if self.game.comet_event.is_full_loaded():
                #retirer du jeu
                self.game.all_monsters.remove(self)

                # appel de la methode pour declencher la pluie de cometes
                self.game.comet_event.attempt_fall()

    def update_health_bar(self, surface):
        # definir une couleur pour les vies
        # bar_color = (111, 210, 46)
        # couleur arriere plan des vies
        # back_bar_color = (60, 63, 60)

        # definir position, largeur et epaisseur de la barre des vies (bar_position = [x, y, w, h])
        # bar_position = [self.rect.x, self.rect.y - 5, self.health, 5]
        # position arriere plan vies
        # back_bar_position = [self.rect.x, self.rect.y - 5, self.max_health, 5]

        # dessiner barre de vie
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x, self.rect.y - 5, self.max_health, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x, self.rect.y - 5, self.health, 5])

    def forward(self):
        # le déplacement se fait si il y a pas de collision joueur
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        # si le monstre est en collision avec le joueur
        else:
            # infliger degats au joueur
            self.game.player.damage(self.attack)
