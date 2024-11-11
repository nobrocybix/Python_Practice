import pygame
from pygame.sprite import Group

from setting import Settings
from ship import Ship
from game_stats import GameStates
from button import Button
from scoreboard import Scoreboard
import game_functions as gf

def run_game():
    # Initialize the pygame, settings, and screen objects.
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode(((
        ai_settings.screen_width, ai_settings.screen_height)))
    pygame.display.set_caption("Alien Invasion")

    # Make the Play button.
    play_button = Button(ai_settings, screen, "Play")

    # Creata instance to store game statistices and a scoreboard.
    stats = GameStates(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Make a ship, a group of aliens, and a group of bullets
    ship = Ship(ai_settings, screen)
    aliens = Group()
    bullets = Group() 

    # Create fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Start the main loops for the game.
    while True:
        gf.check_events(ai_settings, screen, sb, play_button, stats, ship, aliens, bullets)
        
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()