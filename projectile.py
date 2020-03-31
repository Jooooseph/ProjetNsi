import pygame

class Projectile(pygame.sprite.Sprite):

    def __init__(self, joueur):
        super().__init__()
        self.vitesse = 4
        self.joueur = joueur
        self.image = pygame.image.load('C:/Users/Mathys/Desktop/assets/projectile.png')
        self.image = pygame.transform.scale(self.image, (60,60))
        self.rect = self.image.get_rect()
        self.rect.x = joueur.rect.x + 110
        self.rect.y = joueur.rect.y + 30
    
    
    
    def remove(self):
        self.joueur.all_projectiles.remove(self)
    def move(self):
        self.rect.x += self.vitesse

        if self.rect.x > 1080:
            self.remove()
            
