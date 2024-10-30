import pygame
import sys
from time import sleep

from ball import Ball

def create_ball(s, screen, balls):
    '''Create a new ball'''
    ball = Ball(s, screen)
    balls.add(ball)

def catch_ball(s, screen, loli, gs, balls):
    '''Respond to loli catch the ball.'''
    for ball in balls.sprites():
        if ball.rect.colliderect(loli.rect_image):
            gs.ball_total_catch += 1                     
            ball.kill()
            create_ball(s, screen, balls)    

def ball_out_of_screen(s, screen, gs, balls):
    '''remove the ball out of screen'''
    screen_rect = screen.get_rect()

    for ball in balls.copy():
        if ball.rect.top >= screen_rect.bottom:
            if gs.ball_left > 1:          
                gs.ball_left -= 1            
            else:
                print("Game Over")
                sleep(2)
                gs.reset_game()

            ball.kill()        
            create_ball(s, screen, balls)
                            
def balls_update(s, screen, loli, gs, balls):
    '''Update the ball on the screen'''
    balls.draw(screen)
    balls.update()
    ball_out_of_screen(s, screen, gs, balls)
    catch_ball(s, screen, loli, gs, balls)

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

def display_update(s, screen, loli, gs, balls):
        '''Update images on the screen, and flip to the new screen.'''
        screen.fill(s.bg_color)
        screen.blit(loli.image, loli.rect_image)
        loli.update()

        balls_update(s, screen, loli, gs, balls)

        pygame.display.flip()