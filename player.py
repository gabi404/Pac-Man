import pygame, collision_mur, square

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets\player.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (35, 35))
        self.image2 = pygame.image.load('assets\player2.png').convert_alpha()
        self.image2 = pygame.transform.scale(self.image2, (35, 35))
        self.rect = self.image.get_rect()
        self.score = 0
        self.vie = 3
        self.velocity = 3
        self.rect.x = 518
        self.rect.y = 388
        #variable pour gérer rotation joueur:
        self.r = 0
        self.l = 0
        self.t = 0
        self.b = 0

        self.entite = {
        'rect': self.rect,
        'old_rect': self.rect.copy(),
        'position': self.rect.topleft
        }

    def move_right(self):
        #fct pour bouger à droite:
        if self.r == 0:
            self.r = 3
            self.l = 3
            self.t = 3
            self.b = 3
        elif self.r == 1:
            self.r = 3
            self.l = 3
            self.b = 3
            self.t = 3
        elif self.r == 2:
            self.r = 3
            self.l = 3
            self.b = 3
            self.t = 3
        elif self.r == 3:
            self.l = 3
            self.b = 3
            self.t = 3
        return self.r, self.l, self.t, self.b

    def move_left(self):
            #fct pour bouger à gauche:
        if self.l == 0:
            self.r = 0
            self.b = 0
            self.t = 0
        elif self.l == 1:
            self.l = 0
            self.r = 0
            self.b = 0
            self.t = 0
        elif self.l == 2:
            self.l = 0
            self.r = 0
            self.b = 0
            self.t = 0
        elif self.l == 3:
            self.l = 0
            self.r = 0
            self.b = 0
            self.t = 0
        return self.r, self.l, self.t, self.b

    def move_top(self):
        #fct pour bouger en haut:
        if self.t == 0:
            self.t = 1
            self.r = 1
            self.l = 1
            self.b = 1
        elif self.t == 1:
            self.r = 1
            self.l = 1
            self.b = 1
        elif self.t == 2:
            self.t = 1
            self.r = 1
            self.l = 1
            self.b = 1
        elif self.t == 3:
            self.t = 1
            self.r = 1
            self.l = 1
            self.b = 1
        return self.r, self.l, self.t, self.b

    def move_bottom(self):
        #fct pour bouger en bas:
        if self.b == 0:
            self.b = 2
            self.r = 2
            self.l = 2
            self.t = 2
        elif self.b == 1:
            self.b = 2
            self.r = 2
            self.l = 2
            self.t = 2
        elif self.b == 2:
            self.r = 2
            self.l = 2
            self.t = 2
        elif self.b == 3:
            self.b = 2
            self.r = 2
            self.l = 2
            self.t = 2
        return self.r, self.l, self.t, self.b

    def affiche_vie(self, screen):
        # affiche la vie du joueur
        ecart = 30
        for i in range(0, self.vie):
            image = pygame.image.load("assets\health.png").convert_alpha()
            image = pygame.transform.scale(image, (35, 35))
            screen.blit(image, (870+ecart, 670))
            ecart += 50

    def move_right_constant(self, move_r):
        if move_r == True:
            self.rect.x += self.velocity

    def move_left_constant(self, move_l):
        if move_l == True:
            self.rect.x -= self.velocity

    def move_top_constant(self, move_t):
        if move_t == True:
            self.rect.y -= self.velocity

    def move_bottom_constant(self, move_b):
        if move_b == True:
            self.rect.y += self.velocity

    def animation(self, var_animation, var_animation2, img):
        if var_animation <= 5 and var_animation2 == 0:
            img = self.image
            img = pygame.transform.scale(img, (40, 40))
            var_animation += 1
        elif var_animation <= 10 and var_animation2 == 0:
            img = self.image2
            img = pygame.transform.scale(img, (40, 40))
            var_animation += 1
            var_animation2 = 1
        if var_animation <= 10 and var_animation >= 5 and var_animation2 == 1:
            img = self.image2
            img = pygame.transform.scale(img, (40, 40))
            var_animation -= 1
        elif var_animation <= 5 and var_animation >= 0 and var_animation2 == 1:
            img = self.image
            img = pygame.transform.scale(img, (40, 40))
            var_animation -= 1
        if var_animation == 0 and var_animation2 == 1:
            var_animation2 = 0

        return var_animation, var_animation2, img
        