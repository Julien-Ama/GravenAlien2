import pygame
import math
from game import Game

pygame.init()

# generer la fenetre de notre jeu
pygame.display.set_caption("Comet fall game")
screen = pygame.display.set_mode((1080, 720))

background = pygame.image.load("ressourceG/fondG.png")

# charger notre banniere
banner = pygame.image.load("ressourceG/banner.png")
banner = pygame.transform.scale(banner, (700, 700))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 6)

# import du chargement bouton lancer la partie
play_button = pygame.image.load('ressourceG/button.png')
play_button = pygame.transform.scale(play_button, (150 ,150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 2.37)
play_button_rect.y = math.ceil(screen.get_height() / 1.4)

game = Game()

running = True

# boucle tant que cette condition est vrai
while running:

    # appliquer la fenetre du jeu
    screen.blit(background, (0, 150))

    # verifier si le jeu commence ou non
    if game.is_playing:
        # declencher les instruction de la partie
        game.update(screen)
    # verifier si je jeu n'a pas commencé
    else:
    #     ajouter l'ecran menu
        screen.blit(banner, (banner_rect))
        screen.blit(play_button, play_button_rect)

    pygame.display.flip()

    # si le joueur ferme cette fenetre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("fermeture du jeu")
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
#             verification souris/bouton"jouer"
            if play_button_rect.collidepoint(event.pos):
#                 mettre le jeu en mode lancer
                game.start()
