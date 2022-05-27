from turtle import back
from random import randint
import pygame
pygame.init()
screen = pygame.display.set_mode((400, 600))
pygame.display.set_caption("Flappy Bird by @LCH")
clock = pygame.time.Clock()
WHITE = (255, 255, 255)
x_bird = 50
y_bird = 350
tube1_x = 0
tube2_x = 200
tube3_x = 400
tube1_height = randint(100, 400)
tube2_height = randint(100, 400)
tube3_height = randint(100, 400)
tube_width = 50
back_ground_img = pygame.image.load("./images/background.png")
back_ground_img = pygame.transform.scale(back_ground_img, (400, 600))
bird_img = pygame.image.load("./images/bird.png")
bird_img = pygame.transform.scale(bird_img, (35, 35))
tube_img = pygame.image.load("./images/tube.png")
running = True
while (running):
    clock.tick(60)
    screen.fill(WHITE)
    # đưa back_ground_img vào screen
    screen.blit(back_ground_img, (0, 0))
    # ép ống và vẽ ống
    tube1_img = pygame.transform.scale(tube_img, (tube_width, tube1_height))
    tube1 = screen.blit(tube1_img, (tube1_x, 0))
    # đưa bird_img vào screen
    screen.blit(bird_img, (x_bird, y_bird))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
pygame.quit()
            