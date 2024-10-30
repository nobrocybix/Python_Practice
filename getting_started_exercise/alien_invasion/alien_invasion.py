import pygame
from pygame.sprite import Group

from setting import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from game_stats import GameStates
from button import Button

def run_game():
    # Initialize the pygame, settings, and screen objects.
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode(((
        ai_settings.screen_width, ai_settings.screen_height)))
    pygame.display.set_caption("Alien Invasion")

    # Make the Play button.
    play_button = Button(ai_settings, screen, "Play")

    # Creata instance to store game statistices
    stats = GameStates(ai_settings)
    # Make a ship, a group of aliens, and a group of bullets
    ship = Ship(ai_settings, screen)
    aliens = Group()
    bullets = Group()

    # Create fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Start the main loops for the game.
    while True:
        gf.check_events(ai_settings, screen, play_button, stats, ship, aliens, bullets)
        
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button)

run_game()