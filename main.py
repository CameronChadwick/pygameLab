import math
import pygame
import random

# color constants
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
LIGHTBLUE = (0, 94, 255)
GREY = (50, 54, 61)
ORANGE = (255, 106, 0)
LIGHTGREY = (107, 107, 107)

# math constants
PI = math.pi

# game constants
SIZE = (800,800)
FPS = 60

##########################################################################

pygame.init()

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Pygame Picture")

clock = pygame.time.Clock()

running = True

while running:


    for event in pygame.event.get():

        # check for user input
        if event.type == pygame.QUIT:
            running = False


    # game logic

    screen.fill(LIGHTBLUE)

    # drawings

    pygame.draw.circle(screen, LIGHTGREY, [400, 200], 40)
    pygame.draw.circle(screen, LIGHTGREY, [375, 175], 40)
    pygame.draw.circle(screen, LIGHTGREY, [340, 135], 40)
    pygame.draw.rect(screen, GREY, [350, 200, 100, 450])
    pygame.draw.rect(screen, [18, 117, 18], [0, 650, 800, 150])
    pygame.draw.polygon(screen, GREY, [(125, 650), (350, 200), (350, 650)])
    pygame.draw.polygon(screen, GREY, [(350, 650), (450, 200), (675, 650)])
    pygame.draw.line(screen, ORANGE, [440, 200], [615, 650], width=10)
    pygame.draw.line(screen, ORANGE, [350, 200], [125, 650], width=10)
    pygame.draw.line(screen, ORANGE, [440, 200], [400, 650], width=10)
    pygame.draw.line(screen, ORANGE, [410, 200], [200, 650], width=10)



    pygame.display.flip()

    clock.tick(FPS)

# quit
pygame.quit()