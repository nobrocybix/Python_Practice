import pygame
import sys

from bullet import Bullet

def check_event(g_settings, screen, ship, bullets, button, gs):
    '''Respond to the keypresses'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_key_down_event(event, g_settings, screen, ship, bullets, gs)

        elif event.type == pygame.KEYUP:
            check_key_up_event(event, ship)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_mouse_down_event(button, mouse_x, mouse_y, gs, g_settings)

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
        start_game(gs, g_settings)      

def check_key_up_event(event, ship):
    '''Respond to the KEYUP'''
    if event.key == pygame.K_DOWN:
        ship.k_down_flag = False
    elif event.key == pygame.K_UP:
        ship.k_up_flag = False

def check_mouse_down_event(button, mouse_x, mouse_y, gs, g_settings):
    '''Respond to the mouse down'''
    if button.rect.collidepoint(mouse_x, mouse_y):
        start_game(gs, g_settings)

def start_game(gs, g_settings):
    '''Start new game as press the play button and key p '''
    gs.running = True
    gs.reset_miss()
    gs.reset_score()
    g_settings.init_dynamic_settings()
    pygame.mouse.set_visible(False)

def bullet_update(bullets, screen, enemy, gs, g_settings):
    '''Update the bullet to the screen'''
    screen_rect = screen.get_rect()

    # Draw bullets
    for bullet in bullets.sprites():
        bullet.create_bullet()
    
    level_up(enemy, bullets, gs, g_settings)
    remove_bullets(bullets, screen_rect, gs)
    bullets.update()

def level_up(enemy, bullets, gs, g_settings):
    '''Speed up enemy'''
    # bullet hit the target
    if pygame.sprite.spritecollide(enemy, bullets, True):
        gs.hit += 1

        print("Hit scores: %s" %gs.hit)
        if gs.hit == g_settings.level_up_init:
            g_settings.level_up()
        print("speed %s" %g_settings.enemy_speed_factor)

def update_screen(ship, enemy, gs, button):
    '''Update the object to the screen'''
    ship.create_ship()
    enemy.create_enemy()
    if gs.running == False:
        button.draw_button()
        pygame.mouse.set_visible(True)

def remove_bullets(bullets, screen_rect, gs):
    '''Remove the bullet out of screen'''
    for bullet in bullets.copy():
        if bullet.rect.left >= screen_rect.right:
            gs.miss -= 1
            print("bullets left: %s" %gs.miss)           
            if gs.miss == 0:
                print("Game Over")
                gs.running = False
                print("bullets left: %s" %gs.miss)
            bullets.remove(bullet)