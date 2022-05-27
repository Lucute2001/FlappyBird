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
d_2tube = 150
back_ground_img = pygame.image.load("./images/background.png")
back_ground_img = pygame.transform.scale(back_ground_img, (400, 600))
bird_img = pygame.image.load("./images/bird.png")
bird_img = pygame.transform.scale(bird_img, (35, 35))
tube_img = pygame.image.load("./images/tube.png")
tube_op_img = pygame.image.load("./images/tube_op.png")
running = True
while (running):
    clock.tick(60)
    screen.fill(WHITE)
    # đưa back_ground_img vào screen
    screen.blit(back_ground_img, (0, 0))
    # ép ống và vẽ ống
    tube1_img = pygame.transform.scale(tube_img, (tube_width, tube1_height))
    tube1 = screen.blit(tube1_img, (tube1_x, 0))
    tube2_img = pygame.transform.scale(tube_img, (tube_width, tube2_height))
    tube2 = screen.blit(tube2_img, (tube2_x, 0))
    tube3_img = pygame.transform.scale(tube_img, (tube_width, tube3_height))
    tube3 = screen.blit(tube3_img, (tube3_x, 0))
    # ép ảnh ống và vẽ ống đối diện
    tube1_op_img = pygame.transform.scale(tube_op_img, (tube_width, 600-(tube1_height+d_2tube)))
    tube1_op = screen.blit(tube1_op_img, (tube1_x, tube1_height+d_2tube))   
    tube2_op_img = pygame.transform.scale(tube_op_img, (tube_width, 600-(tube2_height+d_2tube)))
    tube2_op = screen.blit(tube2_op_img, (tube2_x, tube2_height+d_2tube))   
    tube2_op_img = pygame.transform.scale(tube_op_img, (tube_width, 600-(tube2_height+d_2tube)))
    tube2_op = screen.blit(tube2_op_img, (tube2_x, tube2_height+d_2tube))   
    # đưa bird_img vào screen
    screen.blit(bird_img, (x_bird, y_bird))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
pygame.quit()
            