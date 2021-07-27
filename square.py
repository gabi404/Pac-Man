import pygame
pygame.init()


class Square(pygame.sprite.Sprite):
    def __init__(self, x, y, largeur, hauteur):
        super().__init__()
        self.BLACK = (0, 0, 0)
        self.largeur = largeur
        self.hauteur = hauteur
        self.x = x
        self.y = y
        self.mur_surface = pygame.Surface((self.largeur, self.hauteur))
        self.mur_surface.set_colorkey(self.BLACK)
        pygame.draw.rect(self.mur_surface, self.BLACK, self.mur_surface.get_rect(), 9)
        self.mur = self.usine_entite(pygame.Rect(x, y, largeur, hauteur))

    def usine_entite(self, rectangle):
            self.entite = {
                'rect': rectangle,
                'vitesse': (0, 0),
                'position': rectangle.topleft

            }
            return self.entite

# initialisation des murs
b1 = Square(389, 359, 24, 94)
t1 = Square(527, 431, 25, 92)
t2 = Square(388, 570,25, 90)
t3 = Square(388, 220,25, 93)
t4 = Square(388, 151,25, 90)
t5 = Square(668, 220,24, 93)
t6 = Square(667, 151,25, 90)
bordure = Square(320, 361,23, 92)
bordure2 = Square(320, 221,23, 96)
l1 = Square(318, 499, 25, 92)
b2 = Square(668, 359, 22, 90)
t7 = Square(667, 570, 25, 90)
l2 = Square(736, 499, 25, 94)
t8 = Square(527, 571, 25, 91)
centre1 = Square(455, 288,25, 99)
centre2 = Square(600, 288,25, 99)
bordure3 = Square(737, 361, 25, 92)
bordure4 = Square(737, 221,25, 96)
t9 = Square(527, 153, 25, 91)
b3 = Square(527, 13, 25, 90)
c1 = Square(388, 58, 94, 45)
c2 = Square(597, 58, 94, 45)
c3 = Square(736, 58, 69, 45)
c4 = Square(273, 58, 70, 45)
h1 = Square(273, 637,208,25)
h2 = Square(598, 637,208,25)
h3 = Square(228, 569, 43,25)
h4 = Square(807, 569, 43,25)
h5 = Square(458, 569, 161,25)
h6 = Square(274, 499, 50,25)
h7 = Square(390, 499, 90,25)
h8 = Square(599, 499, 90,25)
h9 = Square(753, 499, 53,25)
h10 = Square(459, 428, 162,25)
bordure5 = Square(228, 431, 90,22)
bordure6 = Square(758, 431, 90,22)
bordure7 = Square(228, 361, 90,25)
bordure8 = Square(758, 361, 90,25)
bordure9 = Square(228, 293, 90, 24)
bordure10 = Square(758, 292, 90,25)
bordure11 = Square(228, 221, 90,25)
bordure12 = Square(758, 221, 90,25)
centre3 = Square(461, 362, 157, 25)
centre4 = Square(461, 288, 50, 25)
centre5 = Square(568, 288, 50, 25)
centre6 = Square(500, 288, 60, 25)
h11 = Square(458, 151, 163, 25)
h12 = Square(272, 151, 70, 25)
h13 = Square(737, 151, 69, 25)
h14 = Square(410, 220, 71,25)
h15 = Square(598, 220, 68,25)
tp1 = Square(228, 320,25, 90)
tp2 = Square(818, 320, 25, 90)

#liste qui contient tout les murs
lst_all = [b1, t3, t4, bordure, bordure2, bordure3, centre1, c1, c4, bordure5,
    bordure6, bordure7, centre3, bordure8, bordure9, bordure10,
    centre4, centre5, bordure11, bordure12, h12, h14, l2, t1, h8, h9, l1, h6, h7,
    t5, t6, b2, centre2, centre3, bordure4, centre6, t9, b3, c2, c3, h13, h15, 
    t7, t8, h2, h4, t2, h1, h3, h11, h10, h5]

#liste pour collision_2
lst1 = [b1, t3, t4, bordure, bordure2, centre1, c1, c4, bordure5,
    bordure6, bordure7, centre3, bordure8, bordure9, bordure10,
    centre4, centre5, centre6, bordure11, bordure12, h12, h14]

#liste pour collision_3
lst2 = [l2, t1, h8, h9]

#liste pour collision_4
lst3 = [l1, h6, h7]

#liste pour collision_5
lst4 = [t5, t6, b2, centre2, bordure3, bordure4, t9, b3, c2, c3, h13, h15]

#liste pour collision_6
lst5 = [t7, t8, h2, h4]

#liste pour collision_7
lst6 = [t2, h1, h3]

#liste pour collision_8
lst7 = [h11, h10]

#liste pour collision_9
lst8 = [h5]

