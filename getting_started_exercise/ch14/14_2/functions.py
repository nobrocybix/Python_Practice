import pygame
import sys

from bullet import Bullet

def check_event(g_settings, screen, ship, bullets, gs):
    '''Respond to the keypresses'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_key_down_event(event, g_settings, screen, ship, bullets, gs)

        elif event.type == pygame.KEYUP:
            check_key_up_event(event, ship)

def check_key_down_event(event, g_settings, screen, ship, bullets, gs):
    '''Respond to the KEYDOWN'''
    if event.key == pygame.K_DOWN:
        ship.k_down_flag = True
    elif event.key == pygame.K_UP:
        ship.k_up_flag = True
    elif event.key == pygame.K_SPACE:
        bullet = Bullet(g_settings, screen, ship)
        # Maximum number of fires at the same time
        if (len(bullets)) < g_settings.bullet_limit:
            bullets.add(bullet) 
    elif event.key == pygame.K_p:
        gs.running = True      

def check_key_up_event(event, ship):
    '''Respond to the KEYUP'''
    if event.key == pygame.K_DOWN:
        ship.k_down_flag = False
    elif event.key == pygame.K_UP:
        ship.k_up_flag = False

def ship_update(ship):
    '''Update ship to the screen'''
    ship.update() 

def enemy_update(enemy):
    '''Update enemy to the screen'''       
    enemy.update()

def bullet_update(bullets, screen, enemy, gs):
    '''Update the bullet to the screen'''
    screen_rect = screen.get_rect()

    # Draw bullets
    for bullet in bullets.sprites():
        bullet.create_bullet()
    # bullet hit the target
    if pygame.sprite.spritecollide(enemy, bullets, True):
        gs.hit += 1
        print("Hit scores: %s" %gs.hit)

    remove_bullets(bullets, screen_rect, gs)
    bullets.update()

def update_screen(ship, enemy):
    '''Update the object to the screen'''
    ship.create_ship()
    enemy.create_enemy()

def remove_bullets(bullets, screen_rect, gs):
    '''Remove the bullet out of screen'''
    for bullet in bullets.copy():
        if bullet.rect.left >= screen_rect.right:
            gs.miss -= 1
            print("bullets left: %s" %gs.miss)
            if gs.miss == 0:
                print("Game Over")
                gs.running = False
                gs.reset_miss()
                gs.reset_score()
                print("bullets left: %s" %gs.miss)
            bullets.remove(bullet)