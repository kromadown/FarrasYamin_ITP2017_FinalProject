#!/usr/bin/env python
#
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#		It's my first actual game-making attempt. I know code could be much better
#		with classes or defs but I tried to make it short and understandable with very
#		little knowledge of python and pygame(I'm one of them). Enjoy.

import pygame,sys
import time
import random
from pygame import *
from pygame.locals import *
from pygame.sprite import *
from random import *
from pygame.font import *

screen=pygame.display.set_mode((640,480),0,32)
pygame.display.set_caption("Pong Pong!")

#Creating 2 bars, a ball and background.
back = pygame.Surface((640,480))
background = back.convert()
background.fill((0,0,0))
bar = pygame.Surface((10,50))
bar1 = bar.convert()
bar1.fill((0,0,255))
bar2 = bar.convert()
bar2.fill((255,0,0))
circ_sur = pygame.Surface((15,15))
circ = pygame.draw.circle(circ_sur,(0,255,0),(7,7),7)
circle = circ_sur.convert()
circle.set_colorkey((0,0,0))

def game():
    import retry
    # some definitions
    bar1_x, bar2_x = 10. , 620.
    bar1_y, bar2_y = 215. , 215.
    circle_x, circle_y = 307.5, 232.5
    bar1_move, bar2_move = 0. , 0.
    speed_x, speed_y, speed_circ = 275., 275., 275.
    bar1_score, bar2_score = 0,0
    #clock and font objects
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("arcadeclassic",40)
    result_1, result_2 = "Player 1 WIN","Player 2 WIN"

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    bar2_move = -ai_speed
                if event.key == K_DOWN:
                    bar2_move = ai_speed
                if event.key == K_w:
                    bar1_move = -ai_speed
                if event.key == K_s:
                    bar1_move = ai_speed
            elif event.type == KEYUP:
                if event.key == K_UP:
                    bar2_move = 0.
                if event.key == K_DOWN:
                    bar2_move = 0.
                if event.key == K_w:
                    bar1_move = 0.
                if event.key == K_s:
                    bar1_move = 0.

        score1 = font.render(str(bar1_score), True,(255,255,255))
        score2 = font.render(str(bar2_score), True,(255,255,255))

        screen.blit(background,(0,0))
        frame = pygame.draw.rect(screen,(255,255,255),Rect((5,5),(630,470)),2)
        middle_line = pygame.draw.aaline(screen,(255,255,255),(330,5),(330,475))
        screen.blit(bar1,(bar1_x,bar1_y))
        screen.blit(bar2,(bar2_x,bar2_y))
        screen.blit(circle,(circle_x,circle_y))
        screen.blit(score1,(260.,210.))
        screen.blit(score2,(380.,210.))

        bar1_y += bar1_move
        bar2_y += bar2_move

    # movement of circle
        time_passed = clock.tick(30)
        time_sec = time_passed / 1000.0

        circle_x += speed_x * time_sec
        circle_y += speed_y * time_sec
        ai_speed = speed_circ * time_sec

    #limit for the bars
        if bar1_y >= 420.: bar1_y = 420.
        elif bar1_y <= 10. : bar1_y = 10.
        if bar2_y >= 420.: bar2_y = 420.
        elif bar2_y <= 10.: bar2_y = 10.

    #since i don't know anything about collision, ball hitting bars goes like this.
        if circle_x <= bar1_x + 10.:
            if circle_y >= bar1_y - 7.5 and circle_y <= bar1_y + 42.5:
                circle_x = 20.
                speed_x = -speed_x
        if circle_x >= bar2_x - 15.:
            if circle_y >= bar2_y - 7.5 and circle_y <= bar2_y + 42.5:
                circle_x = 605.
                speed_x = -speed_x
        if circle_x < 5.:
            bar2_score += 1
            circle_x, circle_y = 320., 232.5
            bar1_y,bar_2_y = 215., 215.
        elif circle_x > 620.:
            bar1_score += 1
            circle_x, circle_y = 307.5, 232.5
            bar1_y, bar2_y = 215., 215.
        if circle_y <= 10.:
            speed_y = -speed_y
            circle_y = 10.
        elif circle_y >= 457.5:
            speed_y = -speed_y
            circle_y = 457.5

        win_1 = font.render(str(result_1), True, (255,255,255)) #player 1 win
        win_2 = font.render(str(result_2), True, (255,255,255)) #player 2 win

        if bar1_score >= 10:
            screen.blit(win_1,(220,240))
            pygame.display.update()
            pygame.time.delay(3000)
            retry.game_over()
            bar1_score = -1
            bar2_score = 0
            pygame.display.update()
        if bar2_score >= 10:
            screen.blit(win_2,(220,240))
            pygame.display.update()
            pygame.time.delay(3000)
            retry.game_over()
            bar1_score = 0
            bar2_score = -1
            pygame.display.update()


        pygame.display.update()
