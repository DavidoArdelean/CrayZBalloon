import pygame
import classes

pygame.init()

screenW = 512
screenH = 512
screen = pygame.display.set_mode((screenW, screenH))

#game variables
game_paused = False
menu_state = "main"

sprite_index = 0
clock = pygame.time.Clock()  # Create a clock object to control the frame rate

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

#variabila font reprezentand fontul scrisului cu toate detaliile (scris si size)
font = pygame.font.SysFont(('arialblack'), 20)
#variabila TEXT_COL care contine culoare fontului care e alb
TEXT_COL = (255, 255, 255)


# button instances
start_button = classes.Button(screenW/2 - 125, 150, b_start, 0.5)

resume_button = classes.Button(screenW/2 - 125, 150, b_resume, 0.5)
hs_button = classes.Button(screenW/2 - 125, 230, b_highscore, 0.5)
quit_button = classes.Button(screenW/2 - 125, 310, b_quit, 0.5)
back_button = classes.Button(screenW/2 - 125, 390, b_back, 0.5)

def draw_text(text, font, text_col, x, y):  #functie care scrie un text pe screen si ia parametrii (text, fontul, culoare, pozitii x y)
    img = font.render(text, True, text_col)  #variabila imagine care contine un font randat cu text
    screen.blit(img, (x, y))

# def drawGameWindow():
# screen.blit(bg, (0, -8688))

'''            if start_button.draw(screen):
                print("start")
            if hs_button.draw(screen):
                print("high score")
            if quit_button.draw(screen):
                run = False
'''
run = True
while run:
    screen.fill((52, 50, 150))

    if game_paused == True:
        #check menu state
        if menu_state == "main":  #arata butoanele de pause screen
            if resume_button.draw(screen):
                game_paused = False
            if hs_button.draw(screen):
                menu_state = "highscore"
            if quit_button.draw(screen):
                run = False
        #verifica highscore menu
        if menu_state == "highscore":
            #arata highscore si back
            draw_text("Highscore:muiesteaua", font, TEXT_COL, 200, screenH / 2 - 10)
            if back_button.draw(screen):
                menu_state = "main"
    else:
        draw_text("Press SPACE to pause", font, TEXT_COL, 130, screenH / 2 - 10)



    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_SPACE:
                game_paused = True


        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()


pygame.quit()
