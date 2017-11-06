import pygame,sys
from pygame import *
from pygame.locals import *
from pygame.sprite import *

class Retry(Sprite):
    def __init__(self, img, x, y):
        Sprite.__init__(self)
        self.image = image.load(img)
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

screen=pygame.display.set_mode((640,480),0,32)

retry = Retry("retry.png",320,120)
yes = Retry("yes.png",170,250)
no = Retry("no.png",470,250)
retry_sprites = Group(retry,yes,no)

def game_over():
    running = True
    while running:
        screen.fill((0,0,0))
        retry_sprites.draw(screen)
        for command in event.get():
            if command.type == QUIT:
                running = False
                pygame.quit()
            elif command.type == MOUSEBUTTONDOWN:
                if yes.rect.collidepoint(mouse.get_pos()):
                    while running:
                        import main
                        main.mode()
                elif no.rect.collidepoint(mouse.get_pos()):
                    running = False
                    pygame.quit()

        display.update()
