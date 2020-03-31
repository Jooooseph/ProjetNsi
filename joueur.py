import pygame
from projectile import Projectile
class Joueur(pygame.sprite.Sprite):

    def __init__(self):
        self.vie = 100
        self.viemax = 100
        self.attaque = 10
        self.vitesse = 2
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load('C:/Users/Mathys/Desktop/assets//Player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 30
        self.rect.y = 280
    
    
    def lancer_projectile(self):
        self.all_projectiles.add(Projectile(self))




    def move_right(self):
        self.rect.x += self.vitesse
    def move_left(self):
        self.rect.x -= self.vitesse

            

        