import pygame
from pygame.sprite import Group

from settings import Settings
from loli import Loli
from game_stats import GameStates
import game_functions as gf

def run_game():
    # Initialize pygame, settings and screen
    pygame.init()
    s = Settings()
    screen = pygame.display.set_mode((s.screen_width, s.screen_height))
    pygame.display.set_caption("Catch Ball 2")

    # Create Loli and Game Statistics instance
    loli = Loli(s, screen)
    gs = GameStates(s)

    # Make a group and ball 
    balls = Group()
    gf.create_ball(s, screen, balls)

    while True:
        '''Start the main loop for the game.'''
        gf.check_event(loli)
        gf.display_update(s, screen, loli, gs, balls)

run_game()