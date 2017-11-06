import pygame,sys
import time
import random
from pygame import *
from pygame.locals import *
from pygame.sprite import *
from random import *
from pygame.font import *

#class to make the start and mode screen
class Start(Sprite):
    def __init__(self, img, x, y):
        Sprite.__init__(self)
        self.image = image.load(img)
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

pygame.init()
screen=pygame.display.set_mode((640,480),0,32)
pygame.display.set_caption("Pong Pong!")

start = Start("37227cb13801b11.png",320,240)
single = Start("single.png",320,120)
multi = Start("multi.png",320,360)
menu_sprites = Group(start)
mode_sprites = Group(single,multi)

#this is where the mode screen played
def mode():
    import pong
    import pong_multi
    screen.fill((0,0,0))
    mode_sprites.draw(screen)
    display.update()
    for command in event.get():
        if command.type == QUIT:
            pygame.quit()
        if command.type == MOUSEBUTTONDOWN:
            if single.rect.collidepoint(mouse.get_pos()):
                pygame.mixer.music.load("Final Fantasy VII - J-E-N-O-V-A [HQ].mp3")
                pygame.mixer.music.play(0)
                pong.game()
                pygame.mixer.music.stop()
            elif multi.rect.collidepoint(mouse.get_pos()):
                pygame.mixer.music.load("Final Fantasy VII - J-E-N-O-V-A [HQ].mp3")
                pygame.mixer.music.play(0)
                pong_multi.game()
                pygame.mixer.music.stop()

#game start from here
running = True
while running:
    screen.fill((0,0,0))
    menu_sprites.draw(screen)
    for command in event.get():
        if command.type == QUIT:
            running = False
            pygame.quit()
        elif command.type == MOUSEBUTTONDOWN:
            if start.rect.collidepoint(mouse.get_pos()):
                while running:
                    mode()

    display.update()



