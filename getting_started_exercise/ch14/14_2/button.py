import pygame.font

class Button():

    def __init__(self, screen, msg):
        '''Initialize button attributes.'''
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        # Set the dimensions and properties of the button.
        self.width, self.height = (200, 50)
        self.text_color = (255, 0 , 0)
        self.button_color = (0, 255, 0)
        self.font = pygame.font.SysFont(None, 48)

        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self.prep_msg(msg)

    def prep_msg(self, msg):
        '''Trun msg into a rendered image, and center text on the button.'''
        self.msg_img = pygame.font.render(msg, True, self.text_color, self.button_color)
        self.msg_img_rect = self.msg_img_rect.get_rect()
        self.msg_img_rect.center = self.screen_rect.center
    
    def draw_button(self):
        '''Draw blank button, then draw messages.'''
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_img, self.msg_img_rect.center)


