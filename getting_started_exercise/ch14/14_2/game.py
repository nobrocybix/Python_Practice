import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from enemy import Enemy
from game_states import GameState
from button import Button
import functions as f

def run_game():
    '''The game Shooting Practice.'''

    # Initialize the game, settings adn screen object.
    pygame.init()
    g_settings = Settings()

    screen = pygame.display.set_mode(g_settings.width_height)
    pygame.display.set_caption("Shooting Practive")

    # Make a ship and enemy
    ship = Ship(g_settings, screen)
    enemy = Enemy(g_settings, screen)
    # Creat an instance to store game statiistics
    gs = GameState(g_settings)
    # Make a group of bullets and button
    bullets = Group()
    button = Button(screen, "Play")

    while True:
        '''The main loop for the game'''      
        f.check_event(g_settings, screen, ship, bullets, button, gs)

        # update object to the screen.
        screen.fill(g_settings.bg_color)

        if gs.running:
            ship.update()
            enemy.update()
            f.bullet_update(bullets, screen, enemy, gs)
        
        f.update_screen(ship, enemy, gs, button)
        pygame.display.flip()

run_game()