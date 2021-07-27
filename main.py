import pygame, collision_mur, objet, ghost, time, square, keyboard
from game import Game
from square import Square
from collision_mur import Collision

pygame.init()

# initialisation des fps
clock = pygame.time.Clock()
FPS = 60

# générer la fenetre du jeu:
pygame.display.set_caption('Pac-Man')
screen = pygame.display.set_mode((1080, 720))

# définir l'arrière plan:
background = pygame.image.load("assets/bg.jpg").convert_alpha()

# définir bannière d'acceuil:
banner = pygame.image.load("assets/banner.png").convert_alpha()
banner = pygame.transform.scale(banner, (510, 150))

# icone fenetre:
icone = pygame.image.load("assets\player.png").convert_alpha()
icone = pygame.transform.rotate(icone, 180)

# bouton play:
play_button = pygame.image.load('assets/button_play.png')
play_button = pygame.transform.scale(play_button, (330, 130))
play_button_rect = play_button.get_rect()
play_button_rect.x = 380
play_button_rect.y = 350

# bouton infos:
infos_button = pygame.image.load('assets/infos.png')
infos_button = pygame.transform.scale(infos_button, (200, 60))
infos_button_rect = infos_button.get_rect()
infos_button_rect.x = 440
infos_button_rect.y = 480

# bouton quitter:
quit_button = pygame.image.load('assets/quit.png').convert_alpha()
quit_button = pygame.transform.scale(quit_button, (52, 52))
quit_button_rect = quit_button.get_rect()
quit_button_rect.x = 1000
quit_button_rect.y = 650

# image fleche:
fleche = pygame.image.load('assets/fleche.png').convert_alpha()
fleche = pygame.transform.scale(fleche, (50, 50))
fleche_rect = fleche.get_rect()
fleche_rect.x = play_button_rect.x
fleche_rect.y = play_button_rect.y

# polices du jeu:
police = pygame.font.SysFont('courier', 30)
police2 = pygame.font.SysFont('courier', 50)
police3 = pygame.font.SysFont('courier', 20)

# image fantôme effrayé:
ghost_scary = pygame.image.load('assets/ghost_died.bmp').convert_alpha()
ghost_scary = pygame.transform.scale(ghost_scary, (40, 40))
text_ghost = police3.render(':200 pts', True, pygame.Color('white'))

# image coin et jackpot:
coin_img = pygame.image.load('assets/Candy.bmp')
coin_img = pygame.transform.scale(coin_img, (15, 15))
text_coin = police3.render(':10 pts', True, pygame.Color('white'))
jackpot_img = pygame.transform.scale(coin_img, (30, 30))
text_jackpot = police3.render(':50 pts', True, pygame.Color('white'))

game = Game()
contact = Collision()

running = True

current_time = 0  # temps courant
action_time = 0  # temps constant quand débute l'action de collision entre jackpot et pac-mans
jackpot = 0  # variable qui vaut 1 si jackpot manger par pac-man
down = False  # booléen qui vaut True si le sélécteur d'acceuil est sur le bouton du bas
down2 = False # booléen qui vaut True si le sélécteur d'acceuil est sur bonus
up = True  # booléen qui vaut True si le sélécteur d'acceuil est sur le bouton du haut
infos = False  # booléen qui vaut True si bouton infos activé
game_over = False  # booléen qui vaut True si jeu perdue
win = False # booléen qui vaut True si jeu gagné
var_animation = 0
var_animation2 = 0
img = game.player.image  # variable qui charge l'image du joueur
i = 0 # variable qui sert à jouer une seule fois le son de début de jeu
tuch_coin = False
move_r = False
move_l = False
move_t = False
move_b = False

while running:

    # affiche icone fenetre:
    pygame.display.set_icon(icone)
    
    # vérifier si notre jeu a commencé:
    if game.is_playing:
        action_time, jackpot, game_over, win, var_animation, var_animation2, img, i, tuch_coin, move_r, move_l, move_t, move_b = game.update(screen, police, police2, jackpot, current_time, action_time, contact, background, win, game_over, var_animation, var_animation2, img, i, tuch_coin, move_r, move_l, move_t, move_b)
        if i == 1:
            i += 1
        elif i == 2:
            pygame.time.wait(3998) # stop le programme le temps que le son de début de jeu soit joué
            i += 1
            pygame.mixer.stop()
    elif not game.is_playing and infos == False:
        # ajout à mon écran d'acceuil:
        screen.fill('black')
        screen.blit(banner, (290 , 20))
        screen.blit(play_button, (play_button_rect.x, play_button_rect.y))
        screen.blit(quit_button, (quit_button_rect.x, quit_button_rect.y))
        screen.blit(infos_button, (infos_button_rect.x, infos_button_rect.y))
        screen.blit(fleche, (fleche_rect.x-10, fleche_rect.y+45))
        if game_over == True:
            # quand perdue
            text_fin_loose = police2.render("Game Over",True, pygame.Color('white'))
            screen.blit(text_fin_loose, (410, 230))
            score = police.render("Score: " + str(game.player.score),True, pygame.Color('white'))
            screen.blit(score, (460, 300))   
        elif win == True:
            # quand gagné
            text_fin_loose = police2.render("You Win",True, pygame.Color('white'))
            screen.blit(text_fin_loose, (440, 230))
            score = police.render("Score: " + str(game.player.score),True, pygame.Color('white'))
            screen.blit(score, (450, 300))   
    if infos == True:
        # affiche les infos du jeu:
        text = police.render('Commandes: ', True, pygame.Color('white'))
        droite = police3.render('droite:  fleche droite', True, pygame.Color('white'))
        gauche = police3.render('gauche:  fleche gauche', True, pygame.Color('white'))
        haut = police3.render('haut:  fleche haut', True, pygame.Color('white'))
        bas = police3.render('bas:  fleche bas', True, pygame.Color('white'))
        made_by = police3.render('Made by Gabriel', True, pygame.Color('white'))
        screen.fill('black')
        screen.blit(text, (50, 300))
        screen.blit(droite, (70, 350))
        screen.blit(gauche, (70, 390))
        screen.blit(haut, (70, 430))
        screen.blit(bas, (70, 470))
        screen.blit(banner, (290 , 20))
        screen.blit(made_by, (880, 685))
        screen.blit(ghost_scary, (700, 300))
        screen.blit(coin_img, (713, 360))
        screen.blit(jackpot_img, (705, 400))
        screen.blit(text_ghost, (750, 315))
        screen.blit(text_coin, (750, 360))
        screen.blit(text_jackpot, (750, 410))

    # mettre à jour la fenetre:
    pygame.display.update()
    pygame.display.set_icon(icone)
    # vérifie si l'évènement est fermeture de fenetre:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        # détecter si un joueur lache une touche du clavier:
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # savoir si souris vollision avec le bouton play
            if play_button_rect.collidepoint(event.pos):
                # mettre jeu en mode lancé
                game.is_playing = True
                pygame.mixer.Sound('assets/sound/menu_select.wav').play()
            elif quit_button_rect.collidepoint(event.pos):
                running = False
            elif infos_button_rect.collidepoint(event.pos):
                infos = True
                pygame.mixer.Sound('assets/sound/menu_select.wav').play()

        # descend et monte le curseur de séléction d'accueil
        if game.is_playing == False:
            if keyboard.is_pressed('down') and down == False:
                fleche_rect.y += 90
                pygame.mixer.Sound('assets/sound/bip.wav').play()  # joue son du curseur
                down = True
                up = False
            elif keyboard.is_pressed('up') and up == False:
                fleche_rect.y -= 90
                pygame.mixer.Sound('assets/sound/bip.wav').play()  # joue son du curseur
                up = True
                down = False

        if keyboard.is_pressed('enter') and up == True:
            # lance le jeu si entrer appuyé et boutton play séléctionné
            pygame.mixer.Sound('assets/sound/menu_select.wav').play()
            game.is_playing = True
            game_over = False
            win = False
        elif keyboard.is_pressed('enter') and down == True and down2 == False:
            # affiche les infos du jeu
            pygame.mixer.Sound('assets/sound/menu_select.wav').play()
            infos = True 
        if keyboard.is_pressed('esc'):
            infos = False

    current_time = pygame.time.get_ticks()  # temps courant

    # limitation des fps
    clock.tick(FPS)

pygame.quit()
quit()