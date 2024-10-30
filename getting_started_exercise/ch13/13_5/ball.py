import pygame
from random import randint
from pygame.sprite import Sprite


class Ball(Sprite):
    '''A Class to manage ball falls'''
    def __init__(self, s, screen):
        super(Ball, self).__init__()
        '''Initialize the ball's position'''
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load("images/volleyball.png")
        self.rect = self.image.get_rect()

        # Set ball's random position and factor
        self.rect.x = randint(0, self.screen_rect.right)
        self.factor = s.ball_speed_factor

    def update(self):
        self.rect.y += self.factor       