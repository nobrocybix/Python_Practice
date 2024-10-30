import pygame 

class Loli():  
    def __init__(self, screen, ai_settings): 
        
        self.screen = screen
        
        self.image = pygame.image.load("12_3\pygame\images\image.png")
        self.rect = self.image.get_rect() 
        self.screen_rect = screen.get_rect()  
  
        self.rect.center = (self.screen_rect.centerx, self.screen_rect.centery)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        self.ai_settings = ai_settings
        self.float_centerx = float(self.rect.centerx)
        self.float_centery = float(self.rect.centery)


    def blitme(self):         
        self.screen.blit(self.image, self.rect) 

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.float_centerx += self.ai_settings.speedup
        elif self.moving_left and self.rect.left > 0:
            self.float_centerx -= self.ai_settings.speedup
        elif self.moving_up and self.rect.top > self.screen_rect.top:
            self.float_centery -= self.ai_settings.speedup
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.float_centery += self.ai_settings.speedup
        
        self.rect.centerx = self.float_centerx
        self.rect.centery = self.float_centery