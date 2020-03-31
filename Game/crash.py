import pygame
from game import Game
pygame.init()



# generer la fenetre du jeu
pygame.display.set_caption("Crash Bandicoot")
screen = pygame.display.set_mode((1280, 720))

# genere le background
bg = pygame.image.load('fond essaie.png')

# chargement du jeu
game = Game()

running = True

# Boucle tant que true
while running:
    # on met le background
    screen.blit(bg, (0, 300))

    # on ajoute crash au bg
    screen.blit(game.crash.image, game.crash.rect)

    # verif touche et on l'ampeche de sortir de l'ecran
    if game.key_pressed.get(pygame.K_d) and game.crash.rect.x + game.crash.rect.width < screen.get_width():
        game.crash.move_right()
    elif game.key_pressed.get(pygame.K_a) and game.crash.rect.x > 0:
        game.crash.move_left()

    print(game.crash.rect.x)

    # update de l'ecran
    pygame.display.flip()

    # si l'on ferme
    for event in pygame.event.get():
        # verif
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Vous quittez Crash Bandicoot")
        # Detecte la touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.key_pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.key_pressed[event.key] = False
