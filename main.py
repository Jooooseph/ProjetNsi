import pygame
from jeu import Jeu
pygame.init()



    





pygame.display.set_caption("Pokemon")
ecran = pygame.display.set_mode((1080, 700))

background = pygame.image.load('C:/Users/Mathys/Desktop/assets/bg.png')

jeu = Jeu()

execution = True
while execution:

    ecran.blit(background, (0, -500))
    ecran.blit(jeu.joueur.image, jeu.joueur.rect)

    for projectile in jeu.joueur.all_projectiles:
        projectile.move()
    

    jeu.joueur.all_projectiles.draw(ecran)

    if jeu.pressed.get(pygame.K_RIGHT) and jeu.joueur.rect.x + jeu.joueur.rect.width < ecran.get_width():
        jeu.joueur.move_right()
    elif jeu.pressed.get(pygame.K_LEFT) and jeu.joueur.rect.x > 0:
        jeu.joueur.move_left()

    
    

    pygame.display.flip()

    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            execution = False
            pygame.quit()
            print("Fermeture du jeu")
        elif evenement.type == pygame.KEYDOWN:
            jeu.pressed[evenement.key] = True

            if evenement.key == pygame.K_SPACE:
                jeu.joueur.lancer_projectile() 
        elif evenement.type == pygame.KEYUP:
            jeu.pressed[evenement.key] = False









