import sys
import pygame

from rain import Rain

def get_num_rains(s, rain_width):
    '''Determine the number of rains that fit on the screen.'''
    available_space_x = s.screen_width - 2 * rain_width
    num_rains = int(available_space_x / rain_width)
    return num_rains

def create_rain(screen, rain_width, num_rain, rains):
    '''Create rain and place its in the row.'''
    rain = Rain(screen)
    rain.x = rain_width + rain_width * num_rain
    rain.rect.x = rain.x
    rains.add(rain)

def create_rain_row(s, screen, rains):
    '''Create a row of water drops.'''
    rain = Rain(screen)
    rain_width = rain.rect.width

    num_rains = get_num_rains(s, rain_width)

    # Add rain to a group 
    for num_rain in range(num_rains):
        create_rain(screen, rain_width, num_rain, rains)

def update_rains(s, screen, rains):
    '''Update the position of rains, and get rid of old rains'''
    rains.update()

    for rain in rains.copy():
        screen_rect = screen.get_rect()
        if rain.rect.top >= screen_rect.bottom:
            rains.remove(rain)
    
    if len(rains) <= 0:
        create_rain_row(s, screen, rains)
    print(rains)

def check_events():
    '''Respond to mouse and keypresses events'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def screen_update(s, screen, rains):
    '''Update the image on the screen, and flip in the new screen.'''
    screen.fill(s.bgcolor)
    rains.draw(screen)
  
    pygame.display.flip()