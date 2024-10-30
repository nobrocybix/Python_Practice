class Settings():

    def __init__(self):
        '''Initialize the game settings attributes'''
        self.width_height = (1200, 800)
        self.bg_color = (255, 255, 255)

        # ship settings
        self.ship_speed_factor = 0.5

        # enemy settings
        self.enemy_speed_factor = 0.25

        # bullet settings
        self.bullet_speed_factor = 0.5
        self.bullet_limit = 1

        # game statistics settings
        self.miss = 3
        self.hit = 0