import pygame
from pygame.locals import *

pygame.init()
# This code sets up a "clock" object using the Pygame library and sets the desired frames per second (fps) to 60. The clock object is an essential tool for regulating the frame rate of the game loop. It ensures that the game runs at a consistent speed, regardless of the hardware it is running on.
clock = pygame.time.Clock()
fps = 60

screen_width = 864
screen_height = 936

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("F Brd")

#define game variables
ground_scroll = 0
scroll_speed = 4

#load images
bg = pygame.image.load('pygame/img/bg.png')
ground_img = pygame.image.load('pygame/img/ground.png')

run = True
while run:
    clock.tick(fps)
    # draw background
    screen.blit(bg, (0, 0))

    #draw and scroll the ground
    screen.blit(ground_img, (ground_scroll, 768))
    ground_scroll -= scroll_speed
    if abs(ground_scroll) > 35:
        ground_scroll = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()        
pygame.quit()
