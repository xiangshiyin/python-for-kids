# Reference: https://www.pygame.org/docs/tut/PygameIntro.html#taste

import os
import sys
import time
import pygame


os.chdir(os.path.dirname(os.path.abspath(__file__)))

pygame.init()

# size = width, height = 320, 240
size = width, height = 640, 480
speed = [1, 1]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

# ball = pygame.image.load("./intro_ball.gif")
ball = pygame.image.load("./cat.jpeg")
ballrect = ball.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()

    time.sleep(0.01)
