import pygame
import classes
pygame.init()

#game images
pygame.display.set_caption("CrayZ Balloon")
walk = [pygame.image.load('walk0.png'), pygame.image.load('walk1.png'), pygame.image.load('walk2.png'), pygame.image.load('walk3.png'), pygame.image.load('walk4.png'), pygame.image.load('walk5.png'), pygame.image.load('walk6.png'), pygame.image.load('walk7.png')]
bg = pygame.image.load("bg.png")
sb = [pygame.image.load('SB0.png'), pygame.image.load('SB1.png')]
b_start = pygame.image.load('b_start.png')
b_highscore = pygame.image.load('b_highscore.png')
b_quit = pygame.image.load('b_quit.png')
b_resume = pygame.image.load('b_resume.png')
b_back = pygame.image.load('b_back.png')
b_main = pygame.image.load('b_main.png')

screenW = 512
screenH = 512
screen = pygame.display.set_mode((screenW, screenH))
surface = pygame.Surface((screenW, screenH), pygame.SRCALPHA)

#game variables
menu_state = "main"
once_started = False
bg_y = -8688
fps = 20
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
        self.vel = 7
        self.up = False
        self.down = False
        self.left = False
        self.right = False
        self.sprite_index = False


    def draw(self, onscreen):
        # Toggle sprite index
        self.sprite_index = not self.sprite_index

        # Get the current sprite based on sprite_index
        current_sprite = sb[self.sprite_index]

        # Blit the sprite to the screen
        onscreen.blit(current_sprite, (self.x, self.y))

player = Balloon(screenW // 2 - sb[0].get_width()/2, screenH - sb[0].get_height(), 128, 185)


def drawBackground():
    global bg_y
    screen.blit(bg, (0, bg_y))
    bg_y += 10
    if bg_y < bg.get_height() * -1:
        bg_y = bg.get_height()
    pygame.display.update()

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
        drawBackground()
        player.draw(screen)
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
