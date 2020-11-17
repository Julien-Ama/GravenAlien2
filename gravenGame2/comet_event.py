import  pygame
from  comet import Comet

class CometFallEvent:

    # lors du chargement : creer un compteur
    def __init__(self, game):
        self.percent = 0
        self.percent_speed = 33
        self.game = game
        self.fall_mode = False

        # definir un groupe de sprite pour stoker les cometes
        self.all_comets = pygame.sprite.Group()

    def add_percent(self):
        self.percent += self.percent_speed / 100

    def is_full_loaded(self):
        return self.percent >= 100

    def reset_percent(self):
        self.percent = 0

    def meteor_fall(self):
        # boucle pour les valeur entre 1 et 10
        for i in range(1, 10):
            #premiere comete
            self.all_comets.add(Comet(self))

    def attempt_fall(self):
        if self.is_full_loaded and len(self.game.all_monsters) == 0:
            print("Pluie de cometes")
            self.meteor_fall()
            self.fall_mode = True # activer l'evenement

    def uptade_bar(self, surface):

        # ajouter du pourcentage a la barre
        self.add_percent()

        # barre noir (arriere plan)
        pygame.draw.rect(surface, (0, 0, 0), [
            0, # axe des x
            surface.get_height() - 20,# axe des y
            surface.get_width(), # longueur fenêtre
            10 # epaisseur de la barre
        ])
        # barre rouge (jauge d'evenement)
        pygame.draw.rect(surface, (187, 11, 11), [
            0,  # axe des x
            surface.get_height() - 20,  # axe des y
            (surface.get_width() / 100) * self.percent,  # longueur fenêtre
            10  # epaisseur de la barre
        ])
