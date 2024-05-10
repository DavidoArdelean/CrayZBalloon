'''
cauta alta forma pentru delay intre objects in loc de screenW *
deseneaza sprites
invata sprite groups pt o collision mai simpla ? ca sa nu scrii 100 de if-uri
fa in enemy class ca meteoritul sa mearga pe diagonala
'''

import pygame
import classes
import random
pygame.init()


def draw_text(text, font, text_col, x, y):  #functie care scrie un text pe screen si ia parametrii (text, fontul, culoare, pozitii x y)
    img = font.render(text, True, text_col)  #variabila imagine care contine un font randat cu text
    screen.blit(img, (x, y))


class Balloon:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 4
        self.up = False
        self.down = False
        self.left = False
        self.right = False
        self.sprite_index = False
        self.mask = pygame.mask.from_surface(sb[0])  # mask din sb index 0 (primul sprite)

    def draw(self, onscreen):
        self.sprite_index = not self.sprite_index  # la fiecare loop sprite index se schimba intre 0 si 1 (true-false)
        current_sprite = sb[self.sprite_index]  # Get the current sprite based on sprite_index
        onscreen.blit(current_sprite, (self.x, self.y))  # Blit the sprite to the screen

    def update_mask(self):
        self.mask = pygame.mask.from_surface(sb[self.sprite_index])  # update la balloon mask dupa index


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
    meteor_left = [pygame.image.load('Assets/meteor/ML0.png'), pygame.image.load('Assets/meteor/ML0.png'),
                   pygame.image.load('Assets/meteor/ML1.png'), pygame.image.load('Assets/meteor/ML1.png'),
                   pygame.image.load('Assets/meteor/ML2.png'), pygame.image.load('Assets/meteor/ML2.png'),
                   pygame.image.load('Assets/meteor/ML3.png'), pygame.image.load('Assets/meteor/ML3.png')]
    meteor_right = [pygame.image.load('Assets/meteor/MR0.png'), pygame.image.load('Assets/meteor/MR0.png'),
                    pygame.image.load('Assets/meteor/MR1.png'), pygame.image.load('Assets/meteor/MR1.png'),
                    pygame.image.load('Assets/meteor/MR2.png'), pygame.image.load('Assets/meteor/MR2.png'),
                    pygame.image.load('Assets/meteor/MR3.png'), pygame.image.load('Assets/meteor/MR3.png')]

    def __init__(self, enemy_type, side, x, y, width, height, end, vel, sprite_iteration):
        self.enemy_type = enemy_type
        self.side = side  # true-> _left, false-> _right
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = vel
        self.end = end
        self.path = [self.x, self.end]
        self.moveCount = 0
        self.sprite_iteration = sprite_iteration
        self.mask = pygame.mask.from_surface(self.enemy_type[0])  # mask la Enemy pe din bird_left index 0

    def draw(self, surface):
        self.move()
        if self.moveCount + 1 >= self.sprite_iteration:
            self.moveCount = 0
        if self.side:  #daca bird e in dreapta, DRAW in stanga
            if self.x >= -self.width - 10:
                surface.blit(self.enemy_type[self.moveCount // 2], (self.x, self.y))
                self.mask = pygame.mask.from_surface(
                    self.enemy_type[self.moveCount // 2])  # punem mask pe aceleasi coordonate cu bird_left
                self.moveCount += 1
        else:
            if self.x <= self.end:
                surface.blit(self.enemy_type[self.moveCount // 2], (self.x, self.y))
                self.mask = pygame.mask.from_surface(self.enemy_type[self.moveCount // 2])  # Update mask
                self.moveCount += 1

    def move(self):
        if self.side:  # daca enemy e in dreapta, MOVE in stanga
            if self.end - self.vel < self.path[0]:
                self.x -= self.vel

        else:  # daca enemy e in stanga, MOVE in dreapta
            if self.x <= self.path[1]:
                self.x += self.vel


def drawGame():
    global bg_y
    bg_y += 3
    if bg_y < bg.get_height() * -1:
        bg_y = bg.get_height()
    screen.blit(bg, (0, bg_y))

    player.draw(screen)
    bird_L1.draw(screen)
    airplane_R1.draw(screen)
    meteor_L1.draw(screen)

    pygame.display.update()


def check_collision(obj1, obj2):  # method ce verifica coliziunea intre 2 obiecte
    offset_x = obj2.x - obj1.x  # verifica decalaj intre xul obj2 si xul obj1
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) is not None


def reset_game(): #  resetam toate variabilele ca si locatie a obiectelor
    global bg_y
    global bird_L1
    global airplane_R1
    global counter_started
    global meteor_L1
    counter_started = False
    bg_y = -8688
    player.x = screenW // 2 - sb[0].get_width() / 2
    player.y = screenH - sb[0].get_height()
    bird_L1 = Enemy(Enemy.bird_right, False, -64 - 10, random.choice((100, 200, 300, 400)), 64, 64, screenW + 10, 3.2, 12)
    airplane_R1 = Enemy(Enemy.airplane_left, True, screenW * 2 + 10, random.choice((100, 200, 300, 400)), 220, 92, -230, 4, 12)
    meteor_L1 = Enemy(Enemy.meteor_right, False, -128, random.choice((0, 128, 256, 384)), 128, 128, screenW + 10, 6, 16)


#variables from game images
pygame.display.set_caption("CrayZ Balloon")
walk = [pygame.image.load('walk0.png'), pygame.image.load('walk1.png'), pygame.image.load('walk2.png'),
        pygame.image.load('walk3.png'), pygame.image.load('walk4.png'), pygame.image.load('walk5.png'),
        pygame.image.load('walk6.png'), pygame.image.load('walk7.png')]
bg = pygame.image.load("bg.png")
sb = [pygame.image.load('SB0.png'), pygame.image.load('SB1.png')]
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
surface = pygame.Surface((screenW, screenH), pygame.SRCALPHA)

#game variables
menu_state = "main"
bg_y = -8688
fps = 30
clock = pygame.time.Clock()  # Create a clock object to control the frame rate

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
player = Balloon(screenW // 2 - sb[0].get_width() / 2, screenH - sb[0].get_height(), 128, 185)
bird_L1 = Enemy(Enemy.bird_right, False, -64 - 10, random.choice((100, 200, 300, 400)), 64, 64, screenW + 10, 3.2, 12)
airplane_R1 = Enemy(Enemy.airplane_left, True, screenW * 2 + 10, random.choice((100, 200, 300, 400)), 220, 92, -230, 4, 12)
meteor_L1 = Enemy(Enemy.meteor_right, False, -128, random.choice((0, 128, 256, 384)), 128, 128, screenW + 10, 4, 16)

# MAIN LOOP
run = True
while run:
    clock.tick(fps)

    # check menu state
    if menu_state == "main":
        reset_game() # resetam variables cand suntem in main
        screen.fill((52, 50, 150))
        if start_button.draw(screen):
            menu_state = "play"
            counter = 0  # Reset counter when starting gameplay
            counter_started = True
        if hs_button.draw(screen):
            menu_state = "highscore"
        if quit_button.draw(screen):
            run = False

    if menu_state == "play":
        drawGame()

        if counter_started:  # Check if the counter has started
            counter += 1  # Increment the counter by 1 each frame
            score = counter // fps  # Calculate the score based on frames per second
        draw_text(str(score), font, TEXT_COL, 470, 10)
        score_file = open("scores.txt", "r+")
        if score > highest_score:  # daca score e mai mare decat highscore
            highest_score = score
            score_file.write(str(highest_score))  # score devine highscore

        if check_collision(player, bird_L1) or check_collision(player, airplane_R1) or check_collision(player, meteor_L1):
            menu_state = "game over"
        if bg_y >= 0:
            menu_state = "game over"

        # VERIFICA UP DOWN LEFT RIGHT, UP+LEFT+RIGHT ETC
        keys = pygame.key.get_pressed()
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

        if back_button.draw(screen):  # arata back button
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
