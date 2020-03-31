import pygame

# créer une classe pour le joueur
class Crash(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 3  # change cette valeur lorsqu'il gagne ou perd de la vie
        self.maxhealth = 3
        self.attack = 10
        self.velocity = 5
        self.image = pygame.image.load('Crash/Sprite Crash reste sur place/1.png')
        self.rect = self.image.get_rect()
        self.rect.x = 20
        self.rect.y = 450

    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity
