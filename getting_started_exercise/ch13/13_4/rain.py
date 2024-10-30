import pygame
from pygame.sprite import Sprite

class Rain(Sprite):
    '''A Class to manage rain drop'''
    def __init__(self, screen):
        super(Rain, self).__init__()
        
        self.screen = screen
        # Create rain rect at (10, 0)
        self.image = pygame.image.load("images/rain_drop.png")
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width

        self.x = float(self.rect.x)

    def draw_rain(self):
        '''Draw the rain to the screen.'''
        self.screen.blit(self.image, self.rect)
        
    def update(self):
        '''Move rains to the bottom'''
        self.rect.y += 1