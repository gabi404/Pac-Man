import pygame, square, ghost, random

class Collision(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

    def check_collision(self, joueur, carre):
        # vérifie si une entite rentre en collision avec avec un objet:
        return joueur.rect.colliderect(carre.entite['rect'])

    def collision_2(self, joueur, carre):
        if self.check_collision(joueur, carre):
            old_rect = joueur.entite['old_rect']
            new_rect = joueur.entite['rect']
            mur_rect = carre.entite['rect']
            x, y = joueur.entite['position']
            if joueur.t == 1 and old_rect.left >= mur_rect.bottom and new_rect.top < mur_rect.bottom:
                y = new_rect.top = mur_rect.bottom
            elif joueur.b == 2 and old_rect.left >= mur_rect.top and new_rect.bottom > mur_rect.top:
                new_rect.bottom = mur_rect.top
                y = new_rect.top
            if joueur.r == 3 and old_rect.left >= mur_rect.left and new_rect.right > mur_rect.left:
                new_rect.right = mur_rect.left
                x = new_rect.left
            elif joueur.l == 0 and old_rect.left >= mur_rect.right and new_rect.left < mur_rect.right:
                x = new_rect.left = mur_rect.right
            joueur.entite['position'] = (x, y)
        
    def collision_3(self, joueur, carre):
        if self.check_collision(joueur, carre):
            old_rect = joueur.entite['old_rect']
            new_rect = joueur.entite['rect']
            mur_rect = carre.entite['rect']
            x, y = joueur.entite['position']
            if joueur.t == 1 and old_rect.left <= mur_rect.bottom and new_rect.top < mur_rect.bottom:
                y = new_rect.top = mur_rect.bottom
            elif joueur.b == 2 and old_rect.left >= mur_rect.top and new_rect.bottom > mur_rect.top:
                new_rect.bottom = mur_rect.top
                y = new_rect.top
            if joueur.r == 3 and old_rect.left <= mur_rect.left and new_rect.right > mur_rect.left:
                new_rect.right = mur_rect.left
                x = new_rect.left
            elif joueur.l == 0 and old_rect.left <= mur_rect.right and new_rect.left < mur_rect.right:
                x = new_rect.left = mur_rect.right
            joueur.entite['position'] = (x, y)
    
    def collision_4(self, joueur, carre):
        if self.check_collision(joueur, carre):
            old_rect = joueur.entite['old_rect']
            new_rect = joueur.entite['rect']
            mur_rect = carre.entite['rect']
            x, y = joueur.entite['position']
            if joueur.t == 1 and old_rect.left <= mur_rect.bottom and new_rect.top < mur_rect.bottom:
                y = new_rect.top = mur_rect.bottom
            elif joueur.b == 2 and old_rect.left >= mur_rect.top and new_rect.bottom > mur_rect.top:
                new_rect.bottom = mur_rect.top
                y = new_rect.top
            if joueur.r == 3 and old_rect.left >= mur_rect.left and new_rect.right > mur_rect.left:
                new_rect.right = mur_rect.left
                x = new_rect.left
            elif joueur.l == 0 and old_rect.left >= mur_rect.right and new_rect.left < mur_rect.right:
                x = new_rect.left = mur_rect.right
            joueur.entite['position'] = (x, y)
    
    def collision_5(self, joueur, carre):
        if self.check_collision(joueur, carre):
            old_rect = joueur.entite['old_rect']
            new_rect = joueur.entite['rect']
            mur_rect = carre.entite['rect']
            x, y = joueur.entite['position']
            if joueur.t == 1 and old_rect.left >= mur_rect.bottom and new_rect.top < mur_rect.bottom:
                y = new_rect.top = mur_rect.bottom
            elif joueur.b == 2 and old_rect.left >= mur_rect.top and new_rect.bottom > mur_rect.top:
                new_rect.bottom = mur_rect.top
                y = new_rect.top
            if joueur.r == 3 and old_rect.left <= mur_rect.left and new_rect.right > mur_rect.left:
                new_rect.right = mur_rect.left
                x = new_rect.left
            elif joueur.l == 0 and old_rect.left <= mur_rect.right and new_rect.left < mur_rect.right:
                x = new_rect.left = mur_rect.right
            joueur.entite['position'] = (x, y)

    def collision_6(self, joueur, carre):
        if self.check_collision(joueur, carre):
            old_rect = joueur.entite['old_rect']
            new_rect = joueur.entite['rect']
            mur_rect = carre.entite['rect']
            x, y = joueur.entite['position']
            if joueur.t == 1 and old_rect.left <= mur_rect.bottom and new_rect.top < mur_rect.bottom:
                y = new_rect.top = mur_rect.bottom
            elif joueur.b == 2 and old_rect.left <= mur_rect.top and new_rect.bottom > mur_rect.top:
                new_rect.bottom = mur_rect.top
                y = new_rect.top
            if joueur.r == 3 and old_rect.left <= mur_rect.left and new_rect.right > mur_rect.left:
                new_rect.right = mur_rect.left
                x = new_rect.left
            elif joueur.l == 0 and old_rect.left <= mur_rect.right and new_rect.left < mur_rect.right:
                x = new_rect.left = mur_rect.right
            joueur.entite['position'] = (x, y)

    def collision_7(self, joueur, carre):
        if self.check_collision(joueur, carre):
            old_rect = joueur.entite['old_rect']
            new_rect = joueur.entite['rect']
            mur_rect = carre.entite['rect']
            x, y = joueur.entite['position']
            if joueur.t == 1 and old_rect.left <= mur_rect.bottom and new_rect.top < mur_rect.bottom:
                y = new_rect.top = mur_rect.bottom
            elif joueur.b == 2 and old_rect.left <= mur_rect.top and new_rect.bottom > mur_rect.top:
                new_rect.bottom = mur_rect.top
                y = new_rect.top
            if joueur.r == 3 and old_rect.left >= mur_rect.left and new_rect.right > mur_rect.left:
                new_rect.right = mur_rect.left
                x = new_rect.left
            elif joueur.l == 0 and old_rect.left >= mur_rect.right and new_rect.left < mur_rect.right:
                x = new_rect.left = mur_rect.right
            joueur.entite['position'] = (x, y)

    def collision_8(self, joueur, carre):
        if self.check_collision(joueur, carre):
            old_rect = joueur.entite['old_rect']
            new_rect = joueur.entite['rect']
            mur_rect = carre.entite['rect']
            x, y = joueur.entite['position']
            if joueur.t == 1 and old_rect.left >= mur_rect.bottom and new_rect.top < mur_rect.bottom:
                y = new_rect.top = mur_rect.bottom
            elif joueur.b == 2 and old_rect.left >= mur_rect.top and new_rect.bottom > mur_rect.top:
                new_rect.bottom = mur_rect.top
                y = new_rect.top
            if joueur.r == 3 and old_rect.left >= mur_rect.left and new_rect.right > mur_rect.left:
                new_rect.right = mur_rect.left
                x = new_rect.left
            elif joueur.l == 0 and old_rect.left <= mur_rect.right and new_rect.left < mur_rect.right:
                x = new_rect.left = mur_rect.right
            joueur.entite['position'] = (x, y)

    def collision_9(self, joueur, carre):
        if self.check_collision(joueur, carre):
            old_rect = joueur.entite['old_rect']
            new_rect = joueur.entite['rect']
            mur_rect = carre.entite['rect']
            x, y = joueur.entite['position']
            if joueur.t == 1 and old_rect.left <= mur_rect.bottom and new_rect.top < mur_rect.bottom:
                y = new_rect.top = mur_rect.bottom
            elif joueur.b == 2 and old_rect.left <= mur_rect.top and new_rect.bottom > mur_rect.top:
                new_rect.bottom = mur_rect.top
                y = new_rect.top
            if joueur.r == 3 and old_rect.left >= mur_rect.left and new_rect.right > mur_rect.left:
                new_rect.right = mur_rect.left
                x = new_rect.left
            elif joueur.l == 0 and old_rect.left <= mur_rect.right and new_rect.left < mur_rect.right:
                x = new_rect.left = mur_rect.right
            joueur.entite['position'] = (x, y)

    def collision_tp(self, joueur, carre):
        #téléporte le joueur:
        if self.check_collision(joueur, carre) and joueur.rect.x < 400:
            joueur.rect.x = 778
        elif self.check_collision(joueur, carre) and joueur.rect.x > 400:
            joueur.rect.x = 254
    
    def collision_coin(self, player, coin, score):
        if self.check_collision(player, coin):
            score += 10
            coin = pygame.image.load('assets\Candy_black.bmp')

def affiche_mur(square, screen):
    #afficher les murs:
    for element in square.lst_all:
        screen.blit(element.mur_surface, element.entite['rect'])    

def all_collision(player, square, contact):
    #tester si collision joueur/mur:
    for element in square.lst1:
        contact.collision_2(player, element)
    for element in square.lst2:
        contact.collision_3(player, element)
    for element in square.lst3:
        contact.collision_4(player, element)
    for element in square.lst4:
        contact.collision_5(player, element)
    for element in square.lst5:
        contact.collision_6(player, element)
    for element in square.lst6:
        contact.collision_7(player, element)
    for element in square.lst7:
        contact.collision_8(player, element)
    for element in square.lst8:
        contact.collision_9(player, element)
    contact.collision_tp(player, square.tp1)
    contact.collision_tp(player, square.tp2)




    