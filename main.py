import pygame
import classes
import random
pygame.init()

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

screenW = 512
screenH = 512
screen = pygame.display.set_mode((screenW, screenH))
surface = pygame.Surface((screenW, screenH), pygame.SRCALPHA)

#game variables
menu_state = "main"
once_started = False
bg_y = -8688
fps = 30
clock = pygame.time.Clock()  # Create a clock object to control the frame rate


#variabila font reprezentand fontul scrisului cu toate detaliile (scris si size)
font = pygame.font.SysFont('arialblack', 15)
font_gameover = pygame.font.SysFont('arialblack', 25)
#variabila TEXT_COL care contine culoare fontului care e alb
TEXT_COL = (255, 255, 255)

# button instances
start_button = classes.Button(screenW/2 - 125, 150, b_start, 0.5)
resume_button = classes.Button(screenW/2 - 125, 150, b_resume, 0.5)
hs_button = classes.Button(screenW/2 - 125, 230, b_highscore, 0.5)
quit_button = classes.Button(screenW/2 - 125, 310, b_quit, 0.5)
back_button = classes.Button(screenW/2 - 125, 390, b_back, 0.5)
main_button = classes.Button(screenW/2 - 125, 390, b_main, 0.5)


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
        self.sprite_index = not self.sprite_index   # la fiecare loop sprite index se schimba intre 0 si 1 (true-false)
        current_sprite = sb[self.sprite_index]  # Get the current sprite based on sprite_index
        onscreen.blit(current_sprite, (self.x, self.y))   # Blit the sprite to the screen

    def update_mask(self):
        self.mask = pygame.mask.from_surface(sb[self.sprite_index])   # update la balloon mask dupa index


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

    def __init__(self, side, x, y, width, height, end): # INTRODU EMENY TYPE IN PARAMETRII SI SCHIMBA ACOLO UNDE APARE
        #self.enemy_type = enemy_type
        self.side = side  # true-> _left, false-> _right
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 3.2
        self.end = end
        self.path = [self.x, self.end]
        self.moveCount = 0
        self.mask = pygame.mask.from_surface(self.bird_left[0])   # mask la Enemy pe din bird_left index 0

    def draw(self, surface):
        self.move()
        if self.moveCount + 1 >= 12:
            self.moveCount = 0
        if self.side:  #daca bird e in dreapta, DRAW in stanga
            surface.blit(self.bird_left[self.moveCount // 2], (self.x, self.y))
            self.mask = pygame.mask.from_surface(self.bird_left[self.moveCount // 2])  # punem mask pe aceleasi coordonate cu bird_left
            self.moveCount += 2
        else:
            surface.blit(self.bird_right[self.moveCount // 2], (self.x, self.y))
            self.mask = pygame.mask.from_surface(self.bird_right[self.moveCount // 2])  # Update mask
            self.moveCount += 2

    def move(self):
        if self.side:  # daca enemy e in dreapta, MOVE in stanga
            if self.end - self.vel < self.path[0]:
                    self.x -= self.vel

        else:           # daca enemy e in stanga, MOVE in dreapta
            if self.x <= self.path[1]:
                    self.x += self.vel


def drawGame():
    start_time = pygame.time.get_ticks()
    global bg_y
    screen.blit(bg, (0, bg_y))
    player.draw(screen)
    bird_L1.draw(screen)
    bird_L2.draw(screen)

    bg_y += 3
    if bg_y < bg.get_height() * -1:
        bg_y = bg.get_height()
    pygame.display.update()

def check_collision(obj1, obj2):   # method ce verifica coliziunea intre 2 obiecte
    offset_x = obj2.x - obj1.x   # verifica decalaj intre xul obj2 si xul obj1
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) is not None

# INSTANCES of classes
player = Balloon(screenW // 2 - sb[0].get_width()/2, screenH - sb[0].get_height(), 128, 185)
bird_L1 = Enemy(False, -64, random.choice((100, 200, 300, 400)), 64, 64, screenW)
# fa sa porneasca dupa cateva secunde !!!!!!
bird_L2 = Enemy(True, screenW, random.choice((100, 200, 300, 400)), 64, 64, -64)

# MAIN LOOP
run = True
while run:
    clock.tick(fps)
    # check menu state
    if menu_state == "main":

        screen.fill((52, 50, 150))
        if start_button.draw(screen):
            menu_state = "play"
            once_started = True
        if hs_button.draw(screen):
            menu_state = "highscore"
        if quit_button.draw(screen):
            run = False

    if menu_state == "play":
        drawGame()
        if check_collision(player, bird_L1) or check_collision(player, bird_L2):
            print("Collision occurred!")
        if bg_y >= 0:
            menu_state = "game over"


        # VERIFICA UP DOWN LEFT RIGHT, UP+LEFT+RIGHT ETC
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and player.y > player.vel:
            if keys[pygame.K_LEFT] and player.y > player.vel and player.x > player.vel:
                player.y -= player.vel
                player.x -= player.vel/2
                player.up = True
                player.down = False
                player.left = True
                player.right = False
            elif keys[pygame.K_RIGHT] and player.y > player.vel and player.x < screenW - player.width - player.vel:
                player.y -= player.vel
                player.x += player.vel/2
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
                player.x -= player.vel/2
                player.up = False
                player.down = True
                player.left = True
                player.right = False
            elif keys[pygame.K_RIGHT] and player.y < screenH - player.height - player.vel and player.x < screenW - player.width - player.vel:
                player.y += player.vel
                player.x += player.vel/2
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
        #arata back button
        draw_text("Highscore:", font, TEXT_COL, 200, screenH / 2 - 10)
        if back_button.draw(screen):
            menu_state = "main"

    if menu_state == "game over":
        screen.fill((52, 50, 150))
        draw_text("Your score was :", font_gameover, TEXT_COL, 100, screenH / 2 - 100)
        if quit_button.draw(screen):
            run = False
        if main_button.draw(screen):
            #daca e game over, se reseteaza tot cand se intra pe main menu
            player.x = screenW // 2 - sb[0].get_width() / 2
            player.y = screenH - sb[0].get_height()
            player.up = False
            player.down = False
            player.left = False
            player.right = False
            bg_y = -8688
            menu_state = "main"


    # EVENT CHECK
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
