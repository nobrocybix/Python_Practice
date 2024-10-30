import pygame

class Ship():
    '''A Class to draw the ship and moving.'''
    
    def __init__(self, g_settings, screen):
        # Initialize the ship attributes.
        self.width = 50
        self.height = 60
        self.rect_color = (255, 0, 0)

        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.x = 0
        self.rect.centery = self.screen_rect.centery
        
        # The ship's speed factor
        self.factor = g_settings.ship_speed_factor

        # Store a decimal value for the ship
        self.y = float(self.rect.y)

        # Set the ship movement flags.
        self.k_down_flag = False
        self.k_up_flag = False

    def create_ship(self):
        # Draw the ship to the screen.
        self.screen.fill(self.rect_color, self.rect)

    def update(self):
        # Update the ship position.
        if self.k_down_flag and self.rect.bottom <= self.screen_rect.bottom:
            self.y += self.factor
        elif self.k_up_flag and self.rect.top >= 0:
            self.y -= self.factor
        
        self.rect.y = self.y
