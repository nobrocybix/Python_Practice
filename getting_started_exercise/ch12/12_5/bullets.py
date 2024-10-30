import pygame
from pygame.sprite import Sprite

class Bullets(Sprite):
    def __init__(self, game_settings, screen, ship):

        super(Bullets, self). __init__()

        self.screen = screen

        ## get bullet rectangle
        self.rect = pygame.Rect(0, 0, game_settings.bullet_width, game_settings.bullet_height)
        self.rect.centery = ship.rect_ship.centery
        self.rect.right = ship.rect_ship.right

        self.x = float(self.rect.x)

        self.color = game_settings.bullet_color
        self.speed_factor = game_settings.bullet_speed_factor
        
    
    def update(self):
        self.x += self.speed_factor
        self.rect.x = self.x

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)