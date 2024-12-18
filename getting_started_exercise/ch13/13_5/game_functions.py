import pygame
import sys

from ball import Ball

def create_ball(s, screen, balls):
    '''Create a new ball'''
    ball = Ball(s, screen)
    balls.add(ball)

def catch_ball(s, screen, loli, balls):
    '''Respond to loli catch the ball.'''
    for ball in balls.sprites():
        if ball.rect.colliderect(loli.rect_image):
            ball.kill()
            create_ball(s, screen, balls)

def ball_out_of_screen(s, screen, balls):
    '''remove the ball out of screen'''
    for ball in balls.copy():
        if ball.rect.top >= ball.screen_rect.bottom:
            ball.kill()
            create_ball(s, screen, balls)

def balls_update(s, screen, loli, balls):
    '''Update the ball on the screen'''
    balls.update()

    ball_out_of_screen(s, screen, balls)

    catch_ball(s,screen, loli, balls)

def check_event_keydown(loli, check_event):
    '''Respond to Keypresses.'''
    if check_event.key == pygame.K_RIGHT:
        loli.moving_right = True
    elif check_event.key == pygame.K_LEFT:
        loli.moving_left = True

def check_event_keyup(loli, check_event):
    '''Respond to key releases.'''
    if check_event.key == pygame.K_RIGHT:
        loli.moving_right = False
    elif check_event.key == pygame.K_LEFT:
        loli.moving_left = False

def check_event(loli):
    '''Respond to keypresses.'''
    for check_event in pygame.event.get():
        if check_event.type == pygame.QUIT:
            sys.exit()

        elif check_event.type == pygame.KEYDOWN:
            check_event_keydown(loli, check_event)

        elif check_event.type == pygame.KEYUP:
            check_event_keyup(loli, check_event)

def display_update(s, screen, loli, balls):
        '''Update images on the screen, and flip to the new screen.'''
        screen.fill(s.bg_color)
        screen.blit(loli.image, loli.rect_image)
        loli.update()

        balls.draw(screen)
        balls_update(s, screen, loli, balls)

        pygame.display.flip()