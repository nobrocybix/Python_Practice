import pygame
from pygame.sprite import Group

from settings import Settings
from loli import Loli
import game_functions as gf

def run_game():
    # Initialize pygame, settings and screen
    pygame.init()
    s = Settings()
    screen = pygame.display.set_mode((s.screen_width, s.screen_height))
    pygame.display.set_caption("Catch Ball")

    # Create Loli instance
    loli = Loli(s, screen)


    # Make a group and ball 
    balls = Group()
    gf.create_ball(s, screen, balls)

    while True:
        '''Start the main loop for the game.'''
        gf.check_event(loli)
        gf.display_update(s, screen, loli, balls)
        
run_game()