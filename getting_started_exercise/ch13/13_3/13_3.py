import pygame
import rain_functions as rf

from settings import Settings
from pygame.sprite import Group

def rain_drop():
    # Initialize pygame, settings and screen object.
    pygame.init()
    s = Settings()
    screen = pygame.display.set_mode((s.screen_width, s.screen_height))
    pygame.display.set_caption("Rain Drop")

    # Make rain group
    rains = Group()

    rf.create_rain_row(s, screen, rains)

    running = True
    while running:

        rf.check_events()
        rf.screen_update(s, screen, rains)
        rf.update_rains(screen, rains)

rain_drop()