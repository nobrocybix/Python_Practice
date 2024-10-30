import pygame

class Loli():
    def __init__(self, s, screen):
        '''Loli instance attributes'''
        self.image = pygame.image.load("images/image.png")

        self.rect_screen = screen.get_rect()
        self.rect_image = self.image.get_rect()

        self.rect_image.bottom = self.rect_screen.bottom
        self.rect_image.centerx = self.rect_screen.centerx

        # Movement flags
        self.speed_factor = s.loli_speed_factor
        self.moving_left = False
        self.moving_right = False

    def update(self):
        '''Update Loli in the screen'''
        # Update loli's position based on flags
        if self.moving_right and self.rect_image.right < self.rect_screen.right:
            self.rect_image.x += self.speed_factor
        elif self.moving_left and self.rect_image.left > 0:
            self.rect_image.x -= self.speed_factor