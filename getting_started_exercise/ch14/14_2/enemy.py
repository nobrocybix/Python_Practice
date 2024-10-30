import pygame

class Enemy():

    def __init__(self, g_settings, screen):
        '''Initialize the enemy attributes.'''
        
        # The enemy size and color
        self.width = 100
        self.height = 150
        self.rect_color = (0, 255, 0)

        # Get rect of the screen and settings
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.s = g_settings.enemy_speed_factor

        # The enemy object's size and start position.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.right = self.screen_rect.right
        self.rect.centery = self.screen_rect.centery

        # Store the emeny's exact position
        self.y = float(self.rect.y)

        # The enemy's direction flag
        self.direction_flag = 1

    def create_enemy(self):
        '''Draw the emeny to the screen.'''
        self.screen.fill(self.rect_color, self.rect)

    def update(self):
        '''The enemy's movement'''
        self.y += (self.s * self.direction_flag)

        if self.rect.bottom >= self.screen_rect.bottom:
            self.direction_flag = -1
        elif self.rect.top <= self.screen_rect.top:
            self.direction_flag = 1

        self.rect.y = self.y