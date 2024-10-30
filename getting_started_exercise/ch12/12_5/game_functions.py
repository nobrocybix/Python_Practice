import pygame
import sys
from bullets import Bullets

def check_event (game_settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit
            sys.exit()
        # ship up and down
        if event.type == pygame.KEYDOWN:
            event_keydown(event, game_settings, screen, ship, bullets)
        if event.type == pygame.KEYUP:
            event_keyup(event, ship)

def event_keydown(event, game_settings, screen, ship, bullets):  
        if event.key == pygame.K_UP:
            ship.moving_up = True                  
        elif event.key == pygame.K_DOWN:
            ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            if len(bullets) < game_settings.bullets_allowed:
                fire_bullet(game_settings, screen, ship, bullets)         

def event_keyup(event, ship):   
        if event.key == pygame.K_UP:
            ship.moving_up = False                  
        elif event.key == pygame.K_DOWN:
            ship.moving_down = False

def update_screen(game_settings, screen, ship, bullets):
        screen.fill(game_settings.bg_color)

        for bullet in bullets.sprites():
            bullet.draw_bullet()
        
        ship.blitme()
        pygame.display.flip()

def update_bullet(bullets, screen):
     bullets.update()
     rect = screen.get_rect()
     for bullet in bullets.copy():
          if bullet.rect.left >= rect.right:
               bullets.remove(bullet)

def fire_bullet(game_settings, screen, ship, bullets):
    new_bullet = Bullets(game_settings, screen, ship)
    bullets.add(new_bullet)
    print(bullets)