import math
import pygame

# color constants
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
SKY_BLUE = (0, 94, 255)
GREY = (50, 54, 61)
ORANGE = (255, 106, 0)
LIGHT_GREY = (107, 107, 107)

# math constants
PI = math.pi

# game constants
SIZE = (800, 800)
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

    screen.fill(SKY_BLUE)

    # drawings

    # cloud function
    def cloud(cloud_x, cloud_y):
        pygame.draw.ellipse(screen, WHITE, [cloud_x, cloud_y, 40, 30])
        pygame.draw.ellipse(screen, WHITE, [cloud_x + 10, cloud_y - 5, 40, 30])
        pygame.draw.ellipse(screen, WHITE, [cloud_x - 10, cloud_y + 5, 40, 30])
        pygame.draw.ellipse(screen, WHITE, [cloud_x + 5, cloud_y + 5, 40, 30])
        pygame.draw.ellipse(screen, WHITE, [cloud_x - 15, cloud_y + 10, 40, 30])

    # ground and volcano
    pygame.draw.rect(screen, [18, 117, 18], [0, 650, 800, 150])
    pygame.draw.rect(screen, GREY, [350, 200, 100, 450])
    pygame.draw.polygon(screen, GREY, [(125, 650), (350, 200), (350, 650)])
    pygame.draw.polygon(screen, GREY, [(350, 650), (450, 200), (675, 650)])

    # lava flows and pools
    pygame.draw.line(screen, ORANGE, [440, 200], [615, 650], width=10)
    pygame.draw.line(screen, ORANGE, [350, 200], [125, 650], width=10)
    pygame.draw.line(screen, ORANGE, [440, 200], [400, 650], width=10)
    pygame.draw.line(screen, ORANGE, [410, 200], [200, 650], width=10)
    pygame.draw.circle(screen, ORANGE, [200, 700], 60)
    pygame.draw.circle(screen, ORANGE, [125, 700], 60)
    pygame.draw.circle(screen, ORANGE, [160, 700], 60)
    pygame.draw.circle(screen, ORANGE, [615, 700], 60)
    pygame.draw.circle(screen, ORANGE, [400, 700], 60)
    pygame.draw.circle(screen, ORANGE, [410, 700], 60)
    pygame.draw.circle(screen, ORANGE, [410, 710], 60)
    pygame.draw.circle(screen, ORANGE, [605, 710], 60)
    pygame.draw.circle(screen, ORANGE, [595, 700], 60)
    pygame.draw.circle(screen, ORANGE, [400, 200], 50)
    pygame.draw.rect(screen, SKY_BLUE, [350, 150, 100, 50])

    # lava smoke
    pygame.draw.circle(screen, LIGHT_GREY, [400, 175], 40)
    pygame.draw.circle(screen, LIGHT_GREY, [375, 175], 40)
    pygame.draw.circle(screen, LIGHT_GREY, [340, 135], 40)
    pygame.draw.circle(screen, LIGHT_GREY, [315, 100], 40)
    pygame.draw.circle(screen, LIGHT_GREY, [275, 75], 40)
    pygame.draw.circle(screen, LIGHT_GREY, [240, 40], 40)
    pygame.draw.circle(screen, LIGHT_GREY, [190, 10], 40)

    # clouds
    cloud(725, 50)
    cloud(625, 150)
    cloud(425, 25)
    cloud(575, 50)
    cloud(525, 175)
    cloud(150, 75)
    cloud(50, 50)
    cloud(100, 150)

    pygame.display.flip()

    clock.tick(FPS)

# quit
pygame.quit()
