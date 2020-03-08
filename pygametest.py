import pygame
import random
width = 500
height  = 500
fps = 60

# Defining colors
White = (255, 255, 255)
Black = (0, 0, 0)
Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Test")
clock = pygame.time.Clock()

running = True

while running:
    # Fps
    clock.tick(fps)
    #inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #Update
    #Render
    screen.fill(Blue)

    pygame.display.flip()