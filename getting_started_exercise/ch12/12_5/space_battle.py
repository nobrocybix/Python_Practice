import pygame

from ship import Ship
from settings import Settings
import game_functions as gf
from pygame.sprite import Group

def run_game():
    pygame.init()

    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    ship = Ship(game_settings, screen)
    
    bullets = Group()

    running = True  
    while running:

        gf.check_event(game_settings, screen, ship, bullets)
        ship.ship_update()
        gf.update_bullet(bullets, screen)
        gf.update_screen(game_settings, screen, ship, bullets)
                

run_game()