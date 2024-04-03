import pygame

class Button:
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))  # dimensioneaza butoanele
        self.rect = self.image.get_rect()   # primeste un rectangle al butonului
        self.rect.topleft = (x, y)
        self.clicked = False  # toate butoanele incep neapasate

    def draw(self, surface):
        action = False  # variabila care se returneaza din functie pt fiecare functionalitate a butoanelor

        # get mouse position
        pos = pygame.mouse.get_pos()

        # check mouse over and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

        # draw button on the screen
        surface.blit(self.image, (self.rect.x, self.rect.y))
        return action


