import pygame
import sys

import functions as f
from pygame.sprite import Group

def star_in_sky():
    pygame.init()

    screen = pygame.display.set_mode((1600, 800))

    image = pygame.image.load("images/universe.png")
    image_rect = image.get_rect()
    pygame.display.set_caption("Star in the sky")

    stars = Group()
    f.create_star_row(screen, stars)

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        f.update(screen, image, image_rect, stars)


star_in_sky()