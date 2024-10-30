import pygame
from pygame.sprite import Sprite

class Star(Sprite):

    def __init__(self, screen):

        super(Star, self).__init__()

        self.screen = screen
        self.image = pygame.image.load("images/star.png")
        self.rect = self.image.get_rect()

        # star starting position
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
    
    def create_star(self):

        self.screen.blit(self.image, self.rect)