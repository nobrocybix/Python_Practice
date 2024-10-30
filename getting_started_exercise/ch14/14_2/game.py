import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from enemy import Enemy
from game_states import GameState
import functions as f

def run_game():
    '''The game Shooting Practice.'''

    # Initialize the game, settings adn screen object.
    pygame.init()
    g_settings = Settings()

    screen = pygame.display.set_mode(g_settings.width_height)
    pygame.display.set_caption("Shooting Practive")

    # Create Ship and Enemy instance
    ship = Ship(g_settings, screen)
    enemy = Enemy(g_settings, screen)
    gs = GameState(g_settings)
    bullets = Group()

    while True:
        '''The main loop for the game'''      
        f.check_event(g_settings, screen, ship, bullets, gs)

        # update object to the screen.
        screen.fill(g_settings.bg_color)

        if gs.running:
            f.ship_update(ship)
            f.enemy_update(enemy)
            f.bullet_update(bullets, screen, enemy, gs)
        
        f.update_screen(ship, enemy)
        pygame.display.flip()

run_game()