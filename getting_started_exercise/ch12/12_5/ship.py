import pygame

class Ship():

    def __init__(self, game_settings, screen):
        self.game_settings = game_settings
        
        self.screen = screen
        self.rect = self.screen.get_rect()
        
        self.ship_image = pygame.image.load("12_5/images/ship.png")

        # ship start position 
        self.rect_ship = self.ship_image.get_rect()
        self.rect_ship.left =  0
        self.rect_ship.centery = self.rect.centery
    
        pygame.display.set_caption("Pygame")

        self.moving_up = False
        self.moving_down = False

    def blitme(self):      
        self.screen.blit(self.ship_image, self.rect_ship)

    def ship_update(self):
        if self.moving_up and self.rect_ship.top > 0:
            self.rect_ship.y -= self.game_settings.moving_up_factor
        elif self.moving_down and self.rect_ship.bottom < self.rect.bottom:
            self.rect_ship.y += self.game_settings.moving_down_factor