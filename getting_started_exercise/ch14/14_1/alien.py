import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A Class to response a single alien"""
    def __init__(self, ai_settings, screen):
        '''Initialize the alien, and set its starting positons'''
        super().__init__()
        self.ai_settings = ai_settings
        self.screen = screen

        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blitme(self):
        '''Draw the alien at is current loacation'''
        self.screen.blit(self.image, self.rect)
    
    def update(self):
        '''Move the alien left and right'''
        self.x += (self.ai_settings.alien_speed_factor * 
                   self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        '''Retun True if alien is at edge of screens.'''
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True