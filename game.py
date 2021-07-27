import pygame, objet, square, collision_mur, ghost, time, player
from player import Player
from square import Square
from ghost import Ghost


# creer une classe qui représente le jeu:
class Game:
    def __init__(self):
        # générer joueur et fantômes quand partie est lancée:
        self.is_playing = False
        self.player = Player()
        # ghost(pos_x, pos_y, var_direction, vitesse, taille_image, taille_image)
        self.ghost_red = Ghost('assets\ghost_red.png', 550, 248, 3)
        self.ghost_blue = Ghost('assets\ghost_blue.png', 610, 248, 1)
        self.ghost_pink = Ghost('assets\ghost_pink.png', 420, 248, 2)
        self.ghost_brown = Ghost('assets\ghost_brown.png', 480, 248, 3)

        self.pressed = {
            "touche_fleche_droite": True,
            "touche_fleche_gauche": False,
            "touche_fleche_haut": True,
            "touche_fleche_bas": False
        }

    def update(self, screen, police, police2, jackpot, current_time, action_time, contact, background, win, game_over, var_animation, var_animation2, img, i, tuch_coin, move_r, move_l, move_t, move_b):

        # applique l'arrière plan:
        screen.blit(background, (0, 0))    

        # affiche vie joueur:
        self.player.affiche_vie(screen)
    
        # afficher score:
        score = police.render("Score: " + str(self.player.score),True, pygame.Color('white'))
        screen.blit(score, (10, 10))

        if self.player.vie <= 0:
            # affiche fin perdue
            time.sleep(1)
            self.is_playing = False
            game_over = True 
            win = False

        elif objet.map == objet.map2:
            # affiche fin gagné
            time.sleep(1)
            self.is_playing = False
            win = True

        #affiche mur:
        collision_mur.affiche_mur(square, screen)

        #gère collision mur/joueur:
        collision_mur.all_collision(self.player, square, contact)

        # affiche map avec coins
        if objet.affiche_coin(objet.map, screen, self.player, tuch_coin) == 2:
            # vérifie si JACKPOT mangé par joueur
            action_time = pygame.time.get_ticks()
            jackpot = 1
            # transforme fantome
            ghost.ghost_died(self.ghost_red, self.player, 520, 248, 30, 30, 3)
            ghost.ghost_died(self.ghost_blue, self.player, 520, 248, 30, 30, 3)
            ghost.ghost_died(self.ghost_pink, self.player, 520, 248, 30, 30, 3)
            ghost.ghost_died(self.ghost_brown, self.player, 520, 248, 30, 30, 3)
           
        # appliquer l'image des fantômes:
        if self.player.vie > 0:
            if win == False:
                screen.blit(self.ghost_red.image, self.ghost_red.rect)
                screen.blit(self.ghost_blue.image, self.ghost_blue.rect)
                screen.blit(self.ghost_pink.image, self.ghost_pink.rect)
                screen.blit(self.ghost_brown.image, self.ghost_brown.rect)
            screen.blit(img, self.player.rect) # affiche image du joueur

        # joue le son de début de jeu
        if i == 0:
            start_sound = pygame.mixer.Sound('assets/sound/start_game.wav').play()
            start_sound.set_volume(0.5)
            i += 1
            
        # gère collision fantome/mur:
        self.ghost_red.definir_collision() # fantome rouge
        self.ghost_red.change_direction()

        self.ghost_blue.definir_collision() # fantome bleue
        self.ghost_blue.change_direction()

        self.ghost_pink.definir_collision() # fantome rose
        self.ghost_pink.change_direction()

        self.ghost_brown.definir_collision() # fantome marron
        self.ghost_brown.change_direction()    
               
        # si joueur touché par fantome:
        if jackpot == 0:
            if self.player.rect.colliderect(self.ghost_red.rect) or self.player.rect.colliderect(self.ghost_blue.rect) or self.player.rect.colliderect(self.ghost_pink.rect) or self.player.rect.colliderect(self.ghost_brown.rect):
                self.player.vie -= 1
                # initialisation des positions joueur/fantomes:
                self.player.rect.x = 511
                self.player.rect.y = 388

                self.ghost_red.rect.x = 511
                self.ghost_red.rect.y = 245

                self.ghost_blue.rect.x = 590
                self.ghost_blue.rect.y = 245

                self.ghost_pink.rect.x = 420
                self.ghost_pink.rect.y = 245

                self.ghost_brown.rect.x = 480
                self.ghost_brown.rect.y = 245

                sound_die = pygame.mixer.Sound('assets/sound/pac_die.ogg').play()  # son joué quand pac-man meurt
                sound_die.set_volume(0.5)
                pygame.time.wait(1480) # stop le programme le temps du son
                pygame.mixer.stop() # stop le mixe du son
        
        if jackpot == 1:
            if self.player.rect.colliderect(self.ghost_red.rect):
                self.player.score += 200
                # respawn des fantomes
                self.ghost_red.rect.x = 511
                self.ghost_red.rect.y = 248
                sound_eat_ghost = pygame.mixer.Sound('assets/sound/pac_eatghost.wav').play()  # joue son fantôme mangé
                sound_eat_ghost.set_volume(0.5)

            if self.player.rect.colliderect(self.ghost_brown.rect):
                self.player.score += 200
                # respawn des fantomes
                self.ghost_brown.rect.x = 511
                self.ghost_brown.rect.y = 248
                sound_eat_ghost = pygame.mixer.Sound('assets/sound/pac_eatghost.wav').play()  # joue son fantôme mangé
                sound_eat_ghost.set_volume(0.5)

            if self.player.rect.colliderect(self.ghost_blue.rect):
                self.player.score += 200
                # respawn des fantomes
                self.ghost_blue.rect.x = 511
                self.ghost_blue.rect.y = 248
                sound_eat_ghost = pygame.mixer.Sound('assets/sound/pac_eatghost.wav').play()  # joue son fantôme mangé
                sound_eat_ghost.set_volume(0.5)

            if self.player.rect.colliderect(self.ghost_pink.rect):
                self.player.score += 200
                # respawn des fantomes
                self.ghost_pink.rect.x = 511
                self.ghost_pink.rect.y = 248
                sound_eat_ghost = pygame.mixer.Sound('assets/sound/pac_eatghost.wav').play()  # joue son fantôme mangé
                sound_eat_ghost.set_volume(0.5)          
        
        # verifier si le joueur veut aller à gauche, à droite, en haut ou en bas:
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x < 812:
            move_r = True
            move_l = False
            move_t = False
            move_b = False
            self.player.r, self.player.l, self.player.t, self.player.b = self.player.move_right()

        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 230:
            move_r = False
            move_l = True
            move_t = False
            move_b = False
            self.player.r, self.player.l, self.player.t, self.player.b = self.player.move_left()
            
        elif self.pressed.get(pygame.K_UP) and self.player.rect.y > 16 :
            move_r = False
            move_l = False
            move_t = True
            move_b = False
            self.player.r, self.player.l, self.player.t, self.player.b = self.player.move_top()

        elif self.pressed.get(pygame.K_DOWN) and self.player.rect.y < 667 :
            move_r = False
            move_l = False
            move_t = False
            move_b = True
            self.player.r, self.player.l, self.player.t, self.player.b = self.player.move_bottom() 

        if self.player.rect.x < 812:  # gère déplacement joueur droite
            self.player.move_right_constant(move_r)
            if move_r == True:
                var_animation, var_animation2, img = self.player.animation(var_animation, var_animation2, img)
                if self.player.r == 0 or self.player.r == 3:
                    img = pygame.transform.rotate(img, 180)
                elif self.player.r == 1:
                    img = pygame.transform.rotate(img, 270)
                elif self.player.r == 2:
                    img = pygame.transform.rotate(img, 90)
                img = pygame.transform.scale(img, (34, 34))

        if self.player.rect.x > 230:  # gère déplacement joueur gauche
            self.player.move_left_constant(move_l)
            if move_l == True:
                var_animation, var_animation2, img = self.player.animation(var_animation, var_animation2, img)
                if self.player.l == 1:
                    img = pygame.transform.rotate(img, 90)
                elif self.player.l == 2:
                    img = pygame.transform.rotate(img, 270)
                elif self.player.l == 3:
                    img = pygame.transform.rotate(img, 180)
                img = pygame.transform.scale(img, (34, 34))

        if self.player.rect.y > 16:  # gère déplacement joueur haut
            self.player.move_top_constant(move_t)
            if move_t == True:
                var_animation, var_animation2, img = self.player.animation(var_animation, var_animation2, img)
                if self.player.t == 0 or self.player.t == 1:
                    img = pygame.transform.rotate(img, 270)
                elif self.player.t == 2:
                    img = pygame.transform.rotate(img, 180)
                elif self.player.t == 3:
                    img = pygame.transform.rotate(img, 90)
                img = pygame.transform.scale(img, (34, 34))

        if self.player.rect.y < 667:  # gère déplacement joueur bas
            self.player.move_bottom_constant(move_b)
            if move_b == True:
                var_animation, var_animation2, img = self.player.animation(var_animation, var_animation2, img)
                if self.player.b == 0 or self.player.b == 2:
                    img = pygame.transform.rotate(img, 90)
                elif self.player.b == 1:
                    img = pygame.transform.rotate(img, 180)
                elif self.player.b == 3:
                    img = pygame.transform.rotate(img, 270)
                img = pygame.transform.scale(img, (34, 34))

        if current_time - action_time > 6000 and action_time != 0:
            # fin du JACKPOT
            ghost.ghost_after_died(self.ghost_red, 'assets\ghost_red.png', 30, 30, 2)
            ghost.ghost_after_died(self.ghost_blue, 'assets\ghost_blue.png', 30, 30, 2)
            ghost.ghost_after_died(self.ghost_pink, 'assets\ghost_pink.png', 30, 30, 2)
            ghost.ghost_after_died(self.ghost_brown, 'assets\ghost_brown.png', 30, 30, 2)

            jackpot = 0
            action_time = 0

        return action_time, jackpot, game_over, win, var_animation, var_animation2, img, i, tuch_coin, move_r, move_l, move_t, move_b