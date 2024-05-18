"""
invata sprite groups pt o collision mai simpla ? nu-i nevoie, faci cu o lista de enemies prin care iterezi
fa full screen sa arate ok
fa muzica, sunete la fiecare enemy si fiecare miscare
aranjeaza enemies fara randomize
"""

import pygame
import classes
import random
pygame.init()

alien_sprites = [pygame.image.load('Assets/alien/Final00.png'), pygame.image.load('Assets/alien/Final01.png'),
                 pygame.image.load('Assets/alien/Final02.png'), pygame.image.load('Assets/alien/Final03.png'),
                 pygame.image.load('Assets/alien/Final04.png'), pygame.image.load('Assets/alien/Final05.png'),
                 pygame.image.load('Assets/alien/Final06.png'), pygame.image.load('Assets/alien/Final07.png'),
                 pygame.image.load('Assets/alien/Final08.png'), pygame.image.load('Assets/alien/Final09.png'),
                 pygame.image.load('Assets/alien/Final10.png'), pygame.image.load('Assets/alien/Final11.png'),
                 pygame.image.load('Assets/alien/Final12.png'), pygame.image.load('Assets/alien/Final13.png'),
                 pygame.image.load('Assets/alien/Final14.png'), pygame.image.load('Assets/alien/Final15.png'),
                 pygame.image.load('Assets/alien/Final16.png'), pygame.image.load('Assets/alien/Final17.png'),
                 pygame.image.load('Assets/alien/Final18.png'), pygame.image.load('Assets/alien/Final19.png'),
                 pygame.image.load('Assets/alien/Final20.png'), pygame.image.load('Assets/alien/Final21.png'),
                 pygame.image.load('Assets/alien/Final22.png'), pygame.image.load('Assets/alien/Final23.png'),
                 pygame.image.load('Assets/alien/Final24.png'), pygame.image.load('Assets/alien/Final25.png'),
                 pygame.image.load('Assets/alien/Final26.png'), pygame.image.load('Assets/alien/Final27.png'),
                 pygame.image.load('Assets/alien/Final28.png'), pygame.image.load('Assets/alien/Final29.png'),
                 pygame.image.load('Assets/alien/Final30.png'), pygame.image.load('Assets/alien/Final31.png'),
                 pygame.image.load('Assets/alien/Final32.png'), pygame.image.load('Assets/alien/Final33.png'),
                 pygame.image.load('Assets/alien/Final34.png'), pygame.image.load('Assets/alien/Final35.png'),
                 pygame.image.load('Assets/alien/Final36.png'), pygame.image.load('Assets/alien/Final37.png'),
                 pygame.image.load('Assets/alien/Final38.png'), pygame.image.load('Assets/alien/Final39.png'),
                 pygame.image.load('Assets/alien/Final40.png'), pygame.image.load('Assets/alien/Final41.png'),
                 pygame.image.load('Assets/alien/Final42.png'), pygame.image.load('Assets/alien/Final43.png'),
                 pygame.image.load('Assets/alien/Final44.png'), pygame.image.load('Assets/alien/Final45.png'),
                 pygame.image.load('Assets/alien/Final46.png'), pygame.image.load('Assets/alien/Final47.png'),
                 pygame.image.load('Assets/alien/Final48.png'), pygame.image.load('Assets/alien/Final49.png'),
                 pygame.image.load('Assets/alien/Final50.png'), pygame.image.load('Assets/alien/Final51.png'),
                 pygame.image.load('Assets/alien/Final52.png'), pygame.image.load('Assets/alien/Final53.png'),
                 pygame.image.load('Assets/alien/Final54.png'), pygame.image.load('Assets/alien/Final55.png'),
                 pygame.image.load('Assets/alien/Final56.png'), pygame.image.load('Assets/alien/Final57.png'),
                 pygame.image.load('Assets/alien/Final58.png'), pygame.image.load('Assets/alien/Final59.png'),
                 pygame.image.load('Assets/alien/Final60.png'), pygame.image.load('Assets/alien/Final61.png'),
                 pygame.image.load('Assets/alien/Final62.png'), pygame.image.load('Assets/alien/Final63.png'),
                 pygame.image.load('Assets/alien/Final64.png'), pygame.image.load('Assets/alien/Final65.png'),
                 pygame.image.load('Assets/alien/Final66.png'), pygame.image.load('Assets/alien/Final67.png'),
                 pygame.image.load('Assets/alien/Final68.png'), pygame.image.load('Assets/alien/Final69.png'),
                 pygame.image.load('Assets/alien/Final70.png'), pygame.image.load('Assets/alien/Final71.png'),
                 pygame.image.load('Assets/alien/Final72.png'), pygame.image.load('Assets/alien/Final73.png'),
                 pygame.image.load('Assets/alien/Final74.png'), pygame.image.load('Assets/alien/Final75.png'),
                 pygame.image.load('Assets/alien/Final76.png'), pygame.image.load('Assets/alien/Final77.png'),
                 pygame.image.load('Assets/alien/Final78.png'), pygame.image.load('Assets/alien/Final79.png'),
                 pygame.image.load('Assets/alien/Final80.png'), pygame.image.load('Assets/alien/Final81.png'),
                 pygame.image.load('Assets/alien/Final82.png'), pygame.image.load('Assets/alien/Final83.png'),
                 pygame.image.load('Assets/alien/Final84.png'), pygame.image.load('Assets/alien/Final85.png'),
                 pygame.image.load('Assets/alien/Final86.png'), pygame.image.load('Assets/alien/Final87.png'),
                 pygame.image.load('Assets/alien/Final88.png'), pygame.image.load('Assets/alien/Final89.png')]


class human_walk:
    walk = [pygame.image.load('Assets/human/H0.png'), pygame.image.load('Assets/human/H1.png'),
            pygame.image.load('Assets/human/H2.png'), pygame.image.load('Assets/human/H3.png'),
            pygame.image.load('Assets/human/H4.png'), pygame.image.load('Assets/human/H5.png'),
            pygame.image.load('Assets/human/H6.png'), pygame.image.load('Assets/human/H7.png')]
    balloon = [pygame.image.load('Assets/Balloon/B0.png'), pygame.image.load('Assets/Balloon/B1.png')]

    def __init__(self, x, y, x_end, vel):
        self.x = x
        self.y = y
        self.x_end = x_end
        self.vel = vel
        self.move_count = 0  # pentru a itera in walk sprite list
        self.balloon_iter = False  # pentru a itera in balloon sprite list

    def draw(self, surface):
        self.move()
        if self.move_count + 1 >= 12:
            self.move_count = 0

        if self.x <= self.x_end:
            surface.blit(bg, (0, bg_y))  # intai printam bg
            surface.blit(self.walk[self.move_count // 2], (self.x, self.y))  # apoi printam walk
            self.balloon_iter = not self.balloon_iter  # la fiecare loop sprite index se schimba intre 0 si 1 (true-false)
            current_sprite = self.balloon[self.balloon_iter]  # Get the current sprite based on sprite_index
            surface.blit(current_sprite, (player.x, player.y))  # Blit the sprite to the screen
            self.move_count += 1

    def move(self):
        if self.x <= self.x_end:
            self.x += self.vel


def draw_text(text, font, text_col, x, y):  #functie care scrie un text pe screen si ia parametrii (text, fontul, culoare, pozitii x y)
    img = font.render(text, True, text_col)  #variabila imagine care contine un font randat cu text
    screen.blit(img, (x, y))


class Balloon:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.up = False
        self.down = False
        self.left = False
        self.right = False
        self.sprite_index = False
        self.mask = pygame.mask.from_surface(bf[0])  # mask din sb index 0 (primul sprite)

    def draw(self, onscreen):
        self.sprite_index = not self.sprite_index  # la fiecare loop sprite index se schimba intre 0 si 1 (true-false)
        current_sprite = bf[self.sprite_index]  # Get the current sprite based on sprite_index
        onscreen.blit(current_sprite, (self.x, self.y))  # Blit the sprite to the screen

    def update_mask(self):
        self.mask = pygame.mask.from_surface(bf[self.sprite_index])  # update la balloon mask dupa index


class Enemy:
    bird_left = [pygame.image.load('Assets/Birds/FBL1.png'), pygame.image.load('Assets/Birds/FBL2.png'),
                 pygame.image.load('Assets/Birds/FBL3.png'), pygame.image.load('Assets/Birds/FBL4.png'),
                 pygame.image.load('Assets/Birds/FBL5.png'), pygame.image.load('Assets/Birds/FBL6.png')]
    bird_right = [pygame.image.load('Assets/Birds/FBR1.png'), pygame.image.load('Assets/Birds/FBR2.png'),
                  pygame.image.load('Assets/Birds/FBR3.png'), pygame.image.load('Assets/Birds/FBR4.png'),
                  pygame.image.load('Assets/Birds/FBR5.png'), pygame.image.load('Assets/Birds/FBR6.png')]
    airplane_left = [pygame.image.load('Assets/airplane/AL0.png'), pygame.image.load('Assets/airplane/AL1.png'),
                     pygame.image.load('Assets/airplane/AL2.png'), pygame.image.load('Assets/airplane/AL3.png'),
                     pygame.image.load('Assets/airplane/AL4.png'), pygame.image.load('Assets/airplane/AL5.png'),
                     pygame.image.load('Assets/airplane/AL6.png'), pygame.image.load('Assets/airplane/AL7.png')]
    airplane_right = [pygame.image.load('Assets/airplane/AR0.png'), pygame.image.load('Assets/airplane/AR1.png'),
                      pygame.image.load('Assets/airplane/AR2.png'), pygame.image.load('Assets/airplane/AR3.png'),
                      pygame.image.load('Assets/airplane/AR4.png'), pygame.image.load('Assets/airplane/AR5.png'),
                      pygame.image.load('Assets/airplane/AR6.png'), pygame.image.load('Assets/airplane/AR7.png')]
    meteor_left = [pygame.image.load('Assets/meteor/ML0.png'), pygame.image.load('Assets/meteor/ML1.png'),
                   pygame.image.load('Assets/meteor/ML2.png'), pygame.image.load('Assets/meteor/ML3.png'),
                   pygame.image.load('Assets/meteor/ML4.png'), pygame.image.load('Assets/meteor/ML5.png'),
                   pygame.image.load('Assets/meteor/ML6.png'), pygame.image.load('Assets/meteor/ML7.png')]
    meteor_right = [pygame.image.load('Assets/meteor/MR0.png'), pygame.image.load('Assets/meteor/MR1.png'),
                    pygame.image.load('Assets/meteor/MR2.png'), pygame.image.load('Assets/meteor/MR3.png'),
                    pygame.image.load('Assets/meteor/MR4.png'), pygame.image.load('Assets/meteor/MR5.png'),
                    pygame.image.load('Assets/meteor/MR6.png'), pygame.image.load('Assets/meteor/MR7.png')]
    cloud_left = [pygame.image.load('Assets/cloud/CL00.png'), pygame.image.load('Assets/cloud/CL01.png'),
                  pygame.image.load('Assets/cloud/CL02.png'), pygame.image.load('Assets/cloud/CL03.png'),
                  pygame.image.load('Assets/cloud/CL04.png'), pygame.image.load('Assets/cloud/CL05.png'),
                  pygame.image.load('Assets/cloud/CL06.png'), pygame.image.load('Assets/cloud/CL07.png'),
                  pygame.image.load('Assets/cloud/CL08.png'), pygame.image.load('Assets/cloud/CL09.png')]
    cloud_right = [pygame.image.load('Assets/cloud/CR00.png'), pygame.image.load('Assets/cloud/CR01.png'),
                   pygame.image.load('Assets/cloud/CR02.png'), pygame.image.load('Assets/cloud/CR03.png'),
                   pygame.image.load('Assets/cloud/CR04.png'), pygame.image.load('Assets/cloud/CR05.png'),
                   pygame.image.load('Assets/cloud/CR06.png'), pygame.image.load('Assets/cloud/CR07.png'),
                   pygame.image.load('Assets/cloud/CR08.png'), pygame.image.load('Assets/cloud/CR09.png')]
    witch_left = [pygame.image.load('Assets/witch/WL0.png'), pygame.image.load('Assets/witch/WL1.png'),
                  pygame.image.load('Assets/witch/WL2.png'), pygame.image.load('Assets/witch/WL3.png'),
                  pygame.image.load('Assets/witch/WL4.png'), pygame.image.load('Assets/witch/WL5.png'),
                  pygame.image.load('Assets/witch/WL6.png'), pygame.image.load('Assets/witch/WL7.png')]
    witch_right = [pygame.image.load('Assets/witch/WR0.png'), pygame.image.load('Assets/witch/WR1.png'),
                   pygame.image.load('Assets/witch/WR2.png'), pygame.image.load('Assets/witch/WR3.png'),
                   pygame.image.load('Assets/witch/WR4.png'), pygame.image.load('Assets/witch/WR5.png'),
                   pygame.image.load('Assets/witch/WR6.png'), pygame.image.load('Assets/witch/WR7.png')]

    def __init__(self, enemy_type, side, x, y, width, height, x_end, y_end, vel, sprite_iteration, spawn_place, meteor_enemy):
        self.enemy_type = enemy_type
        self.side = side  # true-> _left, false-> _right
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = vel
        self.x_end = x_end
        self.y_end = y_end
        self.x_path = [self.x, self.x_end]
        self.y_path = [self.y, self.y_end]
        self.moveCount = 0
        self.sprite_iteration = sprite_iteration
        self.meteor_enemy = meteor_enemy
        self.spawn_place = spawn_place
        self.mask = pygame.mask.from_surface(self.enemy_type[0])  # mask la Enemy pe din bird_left index 0
        self.bird_sound_trigger = False

    def draw(self, surface):
        if bg_y > self.spawn_place:
            self.move()
            self.sounds()
            if self.moveCount + 1 >= self.sprite_iteration:
                self.moveCount = 0
            if self.side:  #daca enemy e in dreapta, DRAW in stanga
                if self.x >= -self.width - 10:
                    surface.blit(self.enemy_type[self.moveCount // 2], (self.x, self.y))
                    self.mask = pygame.mask.from_surface(self.enemy_type[self.moveCount // 2])  # punem mask pe aceleasi coordonate cu enemy_left
                    self.moveCount += 1
            else:
                if self.x <= self.x_end:
                    surface.blit(self.enemy_type[self.moveCount // 2], (self.x, self.y))
                    self.mask = pygame.mask.from_surface(self.enemy_type[self.moveCount // 2])  # Update mask
                    self.moveCount += 1

    def move(self):
        if self.meteor_enemy:  # daca enemy este meteorit, trebuie sa mearga pe diagonala
            if self.side:  # daca enemy e in dreapta, MOVE in stanga
                if self.x_end - self.vel < self.x_path[0]:
                    self.x -= self.vel
                if self.y <= self.y_path[1]:  # identic cu cea de jos pt ca balonul merge tot pe axa Y in jos
                    self.y += self.vel

            else:  # daca enemy e in stanga, MOVE in dreapta
                if self.x <= self.x_path[1]:
                    self.x += self.vel
                if self.y <= self.y_path[1]:  # identic cu cea de sus
                    self.y += self.vel
        else:
            if self.side:  # daca enemy e in dreapta, MOVE in stanga
                if self.x_end - self.vel < self.x_path[0]:
                    self.x -= self.vel

            else:  # daca enemy e in stanga, MOVE in dreapta
                if self.x <= self.x_path[1]:
                    self.x += self.vel

    def sounds(self):
        if self.side and self.x == 500:
            if self.enemy_type == Enemy.bird_left:
                bird_sound.play()
            elif self.enemy_type == Enemy.airplane_left:
                airplane_sound.play()
            elif self.enemy_type == Enemy.cloud_left:
                cloud_sound.play()
            elif self.enemy_type == Enemy.witch_left:
                meteor_sound.play()

        elif self.meteor_enemy and self.y == 10:
            meteor_sound.play()


def drawGame():
    if human.x < 225:
        human.draw(screen)
    else:
        global bg_y
        bg_y += 3
        if bg_y < bg.get_height() * -1:
            bg_y = bg.get_height()
        screen.blit(bg, (0, bg_y))
        if bg_y <= 0:
            player.draw(screen)

        bird_L1.draw(screen)
        bird_R1.draw(screen)

        airplane_L1.draw(screen)
        airplane_R1.draw(screen)

        meteor_L1.draw(screen)
        meteor_R1.draw(screen)

        cloud_L1.draw(screen)
        cloud_R1.draw(screen)

        witch_L1.draw(screen)
        witch_R1.draw(screen)

        pygame.display.update()


def check_collision(obj1, obj2):  # method ce verifica coliziunea intre 2 obiecte
    offset_x = obj2.x - obj1.x  # verifica decalaj intre xul obj2 si xul obj1
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) is not None


def reset_game():  #  resetam toate variabilele ca si locatie a obiectelor
    global bg_y
    global counter_started
    global human
    global alien_count

    global bird_L1
    global bird_R1

    global airplane_L1
    global airplane_R1

    global meteor_L1
    global meteor_R1

    global cloud_L1
    global cloud_R1

    global witch_L1
    global witch_R1

    counter_started = False
    bg_y = -8688
    player.x = screenW // 2 - bf[0].get_width() / 2
    player.y = screenH - bf[0].get_height()
    human.x = 10
    alien_count = 0

    bird_L1 = Enemy(Enemy.bird_right, False, -64, random.choice((100, 200, 300, 400)), 64, 64, screenW, screenH, 4, 12,
                    -8700, False)
    bird_R1 = Enemy(Enemy.bird_left, True, screenW, random.choice((100, 200, 300, 400)), 64, 64, -74, screenH, 4, 12,
                    -8600, False)

    airplane_L1 = Enemy(Enemy.airplane_right, False, -220, random.choice((100, 200, 300, 400)), 220, 92, screenW,
                        screenH, 4, 12, -8500, False)
    airplane_R1 = Enemy(Enemy.airplane_left, True, screenW, random.choice((100, 200, 300, 400)), 220, 92, -220, screenH,
                        4, 12, -8400, False)

    meteor_L1 = Enemy(Enemy.meteor_right, False, -128, random.choice((-350, -256, 0, 180)), 128, 128, screenW, screenH,
                      6, 16, -8200, True)
    meteor_R1 = Enemy(Enemy.meteor_left, True, screenW, random.choice((-350, -256, 0, 180)), 128, 128, -128, screenH, 6,
                      16, -8000, True)

    cloud_L1 = Enemy(Enemy.cloud_right, False, -100, random.choice((100, 200, 300, 400)), 100, 100, screenW, screenH, 5,
                     20, -7900, False)
    cloud_R1 = Enemy(Enemy.cloud_left, True, screenW, random.choice((100, 200, 300, 400)), 100, 100, -100, screenH, 5,
                     20, -7800, False)

    witch_L1 = Enemy(Enemy.witch_right, False, -128, random.choice((100, 200, 300, 400)), 100, 100, screenW, screenH, 5,
                     12, -7700, False)
    witch_R1 = Enemy(Enemy.witch_left, True, screenW, random.choice((100, 200, 300, 400)), 100, 100, -100, screenH, 5,
                     12, -7600, False)


# SOUNDS and MUSIC VARIABLES
bird_sound = pygame.mixer.Sound('sounds/birds1.wav')
airplane_sound = pygame.mixer.Sound('sounds/plane1.wav')
cloud_sound = pygame.mixer.Sound('sounds/cloud1.wav')
meteor_sound = pygame.mixer.Sound('sounds/meteor1.wav')
witch_sound = pygame.mixer.Sound('sounds/witch2.wav')
walk_sound = pygame.mixer.Sound('sounds/steps1.wav')

game_music1 = pygame.mixer.Sound('sounds/menusong1.mp3')
game_music2 = pygame.mixer.Sound('sounds/menusong2.mp3')
game_music3 = pygame.mixer.Sound('sounds/song1.mp3')
game_music4 = pygame.mixer.Sound('sounds/song2.mp3')
game_music = [game_music1, game_music2, game_music3, game_music4]

#fa game_music o singura melodie legata din 4 si day play doar la asta la infinit
game_music.play(-1)

#variables from game images
pygame.display.set_caption("Cray-Z Balloon")
bg = pygame.image.load("bg.png")
bf = [pygame.image.load('Assets/BalloonFlying/BF0.png'), pygame.image.load('Assets/BalloonFlying/BF1.png')]
b_start = pygame.image.load('Assets/menu/b_start.png')
b_highscore = pygame.image.load('Assets/menu/b_highscore.png')
b_quit = pygame.image.load('Assets/menu/b_quit.png')
b_resume = pygame.image.load('Assets/menu/b_resume.png')
b_back = pygame.image.load('Assets/menu/b_back.png')
b_main = pygame.image.load('Assets/menu/b_main.png')

#window variables
screenW = 512
screenH = 512
screen = pygame.display.set_mode((screenW, screenH))
surface = pygame.Surface((screenW, screenH), pygame.SRCALPHA)  # face un rectangle semi transparent

#game variables
menu_state = "main"
bg_y = -8688
fps = 30
clock = pygame.time.Clock()  # Create a clock object to control the frame rate
alien_count = 0

#score variables
counter = 0
score = 0
counter_started = False
score_file = open("scores.txt", "r")  # deschidem fisierul scores.txt pentru read+write
score_file.seek(0)  # duce pointer la index 0 in fisier ca sa poata citi textul
highest_score = int(score_file.read())
score_file.close()

#variabila font reprezentand fontul scrisului cu toate detaliile (scris si size)
font = pygame.font.SysFont('arialblack', 20)
font_gameover = pygame.font.SysFont('arialblack', 25)
#variabila TEXT_COL care contine culoare fontului care e alb
TEXT_COL = (255, 255, 255)

# button instances
start_button = classes.Button(screenW / 2 - 125, 150, b_start, 0.5)
resume_button = classes.Button(screenW / 2 - 125, 150, b_resume, 0.5)
hs_button = classes.Button(screenW / 2 - 125, 230, b_highscore, 0.5)
quit_button = classes.Button(screenW / 2 - 125, 310, b_quit, 0.5)
back_button = classes.Button(screenW / 2 - 125, 390, b_back, 0.5)
main_button = classes.Button(screenW / 2 - 125, 390, b_main, 0.5)

# INSTANCES of classes
player = Balloon(screenW // 2 - bf[0].get_width() / 2, screenH - bf[0].get_height(), 128, 185)
human = human_walk(10, 448, 225, 3.5)

# pune aici, pune in reset, pune in draw method + global variable, pune collision
# enemy_type, side, x, y, width, height, x_end, y_end, vel, sprite_iteration, spawn_place, meteor_enemy
bird_L1 = Enemy(Enemy.bird_right, False, -64, random.choice((100, 200, 300, 400)), 64, 64, screenW, screenH, 4, 12, -8700, False)
bird_R1 = Enemy(Enemy.bird_left, True, screenW, random.choice((100, 200, 300, 400)), 64, 64, -74, screenH, 4, 12, -8600, False)

airplane_L1 = Enemy(Enemy.airplane_right, False, -220, random.choice((100, 200, 300, 400)), 220, 92, screenW, screenH, 4, 12, -8500, False)
airplane_R1 = Enemy(Enemy.airplane_left, True, screenW, random.choice((100, 200, 300, 400)), 220, 92, -220, screenH, 4, 12, -8400, False)

meteor_L1 = Enemy(Enemy.meteor_right, False, -128, random.choice((-350, -256, 0, 180)), 128, 128, screenW, screenH, 6, 16, -8200, True)
meteor_R1 = Enemy(Enemy.meteor_left, True, screenW, random.choice((-350, -256, 0, 180)), 128, 128, -128, screenH, 6, 16, -8000, True)

cloud_L1 = Enemy(Enemy.cloud_right, False, -100, random.choice((100, 200, 300, 400)), 100, 100, screenW, screenH, 5, 20, -7900, False)
cloud_R1 = Enemy(Enemy.cloud_left, True, screenW, random.choice((100, 200, 300, 400)), 100, 100, -100, screenH, 5, 20, -7800, False)

witch_L1 = Enemy(Enemy.witch_right, False, -128, random.choice((100, 200, 300, 400)), 100, 100, screenW, screenH, 5, 12, -7700, False)
witch_R1 = Enemy(Enemy.witch_left, True, screenW, random.choice((100, 200, 300, 400)), 100, 100, -100, screenH, 5, 12, -7600, False)

# MAIN LOOP
run = True
while run:
    clock.tick(fps)

    # check menu state
    if menu_state == "main":
        reset_game()  # resetam variables cand suntem in main
        screen.fill((52, 50, 150))
        if start_button.draw(screen):
            walk_sound.play()
            menu_state = "play"
            counter = 0  # Reset counter when starting gameplay
            counter_started = True
        if hs_button.draw(screen):
            menu_state = "highscore"
        if quit_button.draw(screen):
            run = False

    if menu_state == "play":
        drawGame()

        # SCORE CODE
        if counter_started:  # Check if the counter has started
            counter += 1  # Increment the counter by 1 each frame
            score = counter // fps  # Calculate the score based on frames per second
        draw_text(str(score), font, TEXT_COL, 470, 10)
        score_file = open("scores.txt", "r+")
        if score > highest_score:  # daca score e mai mare decat highscore
            highest_score = score
            score_file.write(str(highest_score))  # score devine highscore

        # COLLISION CODE
        if (check_collision(player, bird_L1)
            or check_collision(player, bird_R1)

            or check_collision(player, airplane_L1)
            or check_collision(player, airplane_R1)

            or check_collision(player, meteor_L1)
            or check_collision(player, meteor_R1)

            or check_collision(player, cloud_L1)
            or check_collision(player, cloud_R1)

            or check_collision(player, witch_L1)
            or check_collision(player, witch_R1)):
            menu_state = "game over"

        if bg_y >= 0:
            if alien_count <= 89: # afisam animatia de final
                screen.blit(alien_sprites[alien_count], (0, 0))
                alien_count += 1
            else:
                menu_state = "game over"

        # VERIFICA UP DOWN LEFT RIGHT, UP+LEFT+RIGHT ETC
        keys = pygame.key.get_pressed()
        if human.x >= 225:  # miscam balonul doar daca human ajunge la el
            if keys[pygame.K_UP] and player.y > player.vel:
                if keys[pygame.K_LEFT] and player.y > player.vel and player.x > player.vel:
                    player.y -= player.vel
                    player.x -= player.vel / 2
                    player.up = True
                    player.down = False
                    player.left = True
                    player.right = False
                elif keys[pygame.K_RIGHT] and player.y > player.vel and player.x < screenW - player.width - player.vel:
                    player.y -= player.vel
                    player.x += player.vel / 2
                    player.up = True
                    player.down = False
                    player.left = False
                    player.right = True
                else:
                    player.y -= player.vel
                    player.up = True
                    player.down = False
            elif keys[pygame.K_DOWN] and player.y < screenH - player.height - player.vel:
                if keys[pygame.K_LEFT] and player.y < screenH - player.height - player.vel and player.x > player.vel:
                    player.y += player.vel
                    player.x -= player.vel / 2
                    player.up = False
                    player.down = True
                    player.left = True
                    player.right = False
                elif keys[pygame.K_RIGHT] and player.y < screenH - player.height - player.vel and player.x < screenW - player.width - player.vel:
                    player.y += player.vel
                    player.x += player.vel / 2
                    player.up = False
                    player.down = True
                    player.left = False
                    player.right = True
                else:
                    player.y += player.vel
                    player.up = False
                    player.down = True
            if keys[pygame.K_LEFT] and player.x > player.vel:
                player.x -= player.vel
                player.left = True
                player.right = False
            elif keys[pygame.K_RIGHT] and player.x < screenW - player.width - player.vel:
                player.x += player.vel
                player.left = False
                player.right = True

    if menu_state == "pause":  #arata butoanele de pause screen
        pygame.draw.rect(surface, (128, 128, 128, 5), [0, 0, screenW, screenH])
        screen.blit(surface, (0, 0))

        if resume_button.draw(screen):
            menu_state = "play"
        if quit_button.draw(screen):
            run = False

    if menu_state == "highscore":
        screen.fill((52, 50, 150))

        with open("scores.txt", "r") as score_file:
            draw_text("Highscore: " + str(score_file.read()), font, TEXT_COL, 180, screenH / 2 - 10)

        if back_button.draw(screen):  # + arata back button
            menu_state = "main"

    if menu_state == "game over":
        screen.fill((52, 50, 150))

        draw_text("Your score : " + str(score), font_gameover, TEXT_COL, 100, screenH / 2 - 100)
        draw_text("Highest score : " + str(highest_score), font_gameover, TEXT_COL, 100, screenH / 2 - 50)

        if quit_button.draw(screen):
            run = False
        if main_button.draw(screen):
            menu_state = "main"

    # Event checker
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_SPACE:
                if menu_state == "play":
                    menu_state = "pause"
                elif menu_state == "pause":
                    menu_state = "play"
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.display.quit()
pygame.quit()
