import pygame, random, collision_mur, square, objet
from time import sleep

pygame.init()

class Ghost(pygame.sprite.Sprite):

    def __init__(self, image, x, y, var):
        super().__init__()
        self.attack = 1
        self.velocity = 2
        self.health = 1
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.entite = {
        'rect': self.rect,
        'old_rect': self.rect.copy(),
        'position': self.rect.topleft
        }
        self.lst_direction = [1, 2, 3, 4]
        self.lst_direction1 = [1, 2]
        self.lst_direction2 = [3, 4]
        self.var = var    # initialisation de la direction au départ
        self.i = 0
        self.jackpot = 0
        self.compt = 10

    def definir_collision(self):
        global i
        for element in square.lst_all:
            if self.rect.colliderect(element.entite['rect']):
                self.i += 1
                return True

    def move_right(self):
        if self.rect.x < 803:
            self.rect.x += self.velocity 
        else:
            self.var = random.choice(self.lst_direction)
    
    def move_left(self):
        if self.rect.x > 225:
            self.rect.x -= self.velocity 
        else:
            self.var = random.choice(self.lst_direction)

    def move_bottom(self):
        if self.rect.y < 670:
            self.rect.y += self.velocity 
        else:
            self.var = random.choice(self.lst_direction)

    def move_top(self):
        if self.rect.y > 14:
            self.rect.y -= self.velocity 
        else:
            self.var = random.choice(self.lst_direction)

    def change_direction(self):
        global i
        if self.i == 0:
        #si il n'y a pas de collision
            if self.var == 1:
                self.move_right()
            elif self.var == 2:
                self.move_left()
            elif self.var == 3:
                self.move_top()
            elif self.var == 4:
                self.move_bottom()
        elif self.i == 1:
        #si il y a une collision
            if self.var == 1:
                self.var = random.choice(self.lst_direction2)
                self.move_left()
            elif self.var == 2:
                self.var = random.choice(self.lst_direction2)
                self.move_right()
            elif self.var == 3:
                self.var = random.choice(self.lst_direction1)
                self.move_bottom()
            elif self.var == 4:
                self.var = random.choice(self.lst_direction1)
                self.move_top()
            if self.var == 1:
                self.move_right()
            elif self.var == 2:
                self.move_left()
            elif self.var == 3:
                self.move_top()
            elif self.var == 4:
                self.move_bottom()
            self.i = 0
                
def ghost_died(ghost, player, x, y, w, h, velocity):
    ghost.velocity = velocity
    ghost.image = pygame.image.load('assets/ghost_died.bmp').convert_alpha()
    ghost.image = pygame.transform.scale(ghost.image, (w, h))
    
def ghost_after_died(ghost, img, w, h, velocity):
        ghost.velocity = velocity
        ghost.image = pygame.image.load(img).convert_alpha()
        ghost.image = pygame.transform.scale(ghost.image, (w, h))

