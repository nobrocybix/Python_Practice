import pygame 

class Loli():  
    def __init__(self, screen, ai_settings): 
        
        self.screen = screen
        
        self.image = pygame.image.load("12_2\pygame\images\image.png")
        self.rect = self.image.get_rect() 
        self.screen_rect = screen.get_rect()  
  
        self.rect.center = (self.screen_rect.centerx, self.screen_rect.centery)


    def blitme(self):         
        self.screen.blit(self.image, self.rect) 