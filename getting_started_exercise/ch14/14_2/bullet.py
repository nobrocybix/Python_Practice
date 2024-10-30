import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self, g_settings, screen, ship):
        super().__init__()
        # Initialize the bullet attributes.
        self.width = 50
        self.height = 25
        self.rect_color = (0, 0, 255)

        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.ship = ship

        # Bullet start position
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.x = self.ship.rect.right
        self.rect.centery = self.ship.rect.centery

        # Store decimal of the bullet rect
        self.x = float(self.rect.x)
        self.factor = g_settings.bullet_speed_factor
    
    def create_bullet(self):
        # Draw the bullet to the screen.
        self.screen.fill(self.rect_color, self.rect)

    def update(self):
        # Update bullet in the screen
        self.x += self.factor
        self.rect.x = self.x