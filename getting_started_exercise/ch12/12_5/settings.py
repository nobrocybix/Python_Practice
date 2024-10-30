class Settings():
    
    def __init__(self):

        self.screen_width = 1600
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        
        self.moving_up_factor = 2
        self.moving_down_factor = 2

        self.bullet_width = 15  
        self.bullet_height = 5   
        self.bullet_color = (255, 0, 0)
        self.bullet_speed_factor = 1
        self.bullets_allowed  = 3