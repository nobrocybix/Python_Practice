import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

def check_keydown_events(event, ai_settings, screen, ship, bullets, stats, aliens):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_p:
        start_game(stats, aliens, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event, ship):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, play_button, stats, ship, aliens, bullets):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(screen, ai_settings, aliens, bullets, ship, play_button, mouse_x, mouse_y, stats)

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets, stats, aliens)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def start_game(stats, aliens, bullets):
        '''Start Game'''
        # Hide the mouse cursor.
        pygame.mouse.set_visible(False)

        # Reset the game statistics.
        stats.reset_stats()
        stats.game_active = True

        # Empty the list of aliens and bullets lists.
        aliens.empty()
        bullets.empty()   

def check_play_button(screen, ai_settings, aliens, bullets, ship, play_button, mouse_x, mouse_y, stats):
    '''Start a new game when the player clicks Play.'''
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)

    if button_clicked and not stats.game_active:

        ai_settings.initialize_dynamic_settings()
        start_game(stats, aliens, bullets)

        # Create a new fleet and center the ship
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

          

def update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button):
    """Update images on the screen and flip to the new screen."""
    screen.fill(ai_settings.bg_color)

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)

    # Draw the play button if the game is inactive
    if not stats.game_active:
        play_button.draw_button()

    pygame.display.flip()

def update_bullets(ai_settings, screen, ship, aliens, bullets):
    """Update the position of bullets and remove the ones that are off the screen."""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
            
    check_bullet_alien_collistions(ai_settings, screen, ship, aliens, bullets)

def check_bullet_alien_collistions(ai_settings, screen, ship, aliens, bullets):
    '''Response to bullet-alien collistions'''
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
        
    if len(aliens) == 0:
        # If the entire fleet is destroyed, start a new level.
        bullets.empty()
        ai_settings.increase_speed()

        create_fleet(ai_settings, screen, ship, aliens)

def fire_bullet(settings, screen, ship, bullets):
    """Fire a bullet if limit not reached yet."""
    if len(bullets) < settings.bullets_allowed:
        new_bullet = Bullet(settings, screen, ship)
        bullets.add(new_bullet)

def get_number_space_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - (2 * alien_width)
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(ai_settings, alien_height, ship_height):
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    num_rows = int(available_space_y / (2 * alien_height))
    return num_rows

def create_alien(ai_settings, screen, alien_number, aliens, row_numbers):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width   
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_numbers
    aliens.add(alien) 

def check_fleet_edges(ai_settings, aliens):
    '''Response appropriately if any aliens have reached an edge.'''
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    '''Drop the entire fleet, and change the fleet's direction.'''
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def create_fleet(ai_settings, screen, ship, aliens):
     """Create a full fleet of aliens """
     # Create an alien, find number of aliens in a roww
     alien = Alien(ai_settings, screen)    
     number_aliens_x = get_number_space_x(ai_settings, alien.rect.width)
     num_rows = get_number_rows(ai_settings, alien.rect.height, ship.rect.height)

     # Create the fleet of aliens
     for row_number in range(num_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, alien_number, aliens, row_number)

def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    '''Respond to ship being hit by aliens'''
    if stats.ships_left > 0:
        # Decrement ships left.
        stats.ships_left -= 1

        # Empty the list of aliens and bullets.
        aliens.empty()
        bullets.empty()

        # Create the new fleet, and center the ship
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # Pause
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    '''Check if any aliens have reached the bottom of the screen.'''
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Treat this same as if the ship got hit.
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break

def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    ''' Check if the fleet is at the edge,
        then update the postions of all aliens in the fleets.'''
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # Look for alliens-ships collisions.
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
    
    # Look for the aliens hitting the bottom of the screens.
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)