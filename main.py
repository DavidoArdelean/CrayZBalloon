import pygame
import classes
import time
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

x = screenW // 2 - sb[0].get_width()/2
y = screenH - sb[0].get_height()
balloonW = 128
balloonH = 185
vel = 7
up = False
down = False
left = False
right = False
moveCount = 0
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


def drawGameWindow():
    global moveCount
    global menu_state
    # timpul trecut de cand a fost initiat pygame, in milisecunde, bagat in elapsed_time
    elapsed_time = pygame.time.get_ticks()
    # Calculate y-coordinate of the background based on elapsed time
    bg_speed = 4  # Adjust the scrolling speed as needed
    bg_y = int((elapsed_time * bg_speed) % (bg.get_height() + 8688)) - 8688
    screen.blit(bg, (0, bg_y))
    if bg_y >= 0:
        menu_state = "game over"

    current_sprite = sb[(pygame.time.get_ticks() // (1000 // fps)) % len(sb)]
    draw_text("Press SPACE to pause", font, TEXT_COL, 0, 0)
    if moveCount + 1 >= 20:
        moveCount = 0
    if up or down or left or right:
        current_sprite = sb[moveCount // 3 % len(sb)]
        screen.blit(current_sprite, (x, y))
        moveCount += 1
    else:
        screen.blit(current_sprite, (x, y))

    pygame.display.update()


run = True
while run:
    clock.tick(fps)
    #check menu state
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
        if menu_state != "game over":
            once_started = True
        drawGameWindow()

        keys = pygame.key.get_pressed()  # VERIFICA UP DOWN LEFT RIGHT, UP+LEFT+RIGHT ETC
        if keys[pygame.K_UP] and y > vel:
            if keys[pygame.K_LEFT] and y > vel and x > vel:
                y -= vel
                x -= vel/2
                up = True
                down = False
                left = True
                right = False
            elif keys[pygame.K_RIGHT] and y > vel and x < screenW - balloonW - vel:
                y -= vel
                x += vel/2
                up = True
                down = False
                left = False
                right = True
            else:
                y -= vel
                up = True
                down = False
        elif keys[pygame.K_DOWN] and y < screenH - balloonH - vel:
            if keys[pygame.K_LEFT] and y < screenH - balloonH - vel and x > vel:
                y += vel
                x -= vel/2
                up = False
                down = True
                left = True
                right = False
            elif keys[pygame.K_RIGHT] and y < screenH - balloonH - vel and x < screenW - balloonW - vel:
                y += vel
                x += vel/2
                up = False
                down = True
                left = False
                right = True
            else:
                y += vel
                up = False
                down = True
        if keys[pygame.K_LEFT] and x > vel:
            x -= vel
            left = True
            right = False
        elif keys[pygame.K_RIGHT] and x < screenW - balloonW - vel:
            x += vel
            left = False
            right = True

    if menu_state == "pause":  #arata butoanele de pause screen
        pygame.draw.rect(surface, (128, 128, 128, 20), [0, 0, screenW, screenH])
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
            menu_state = "main"

        pygame.display.update()

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
