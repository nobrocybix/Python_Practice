class Settings():

    def __init__(self):
        '''Initialize the game settings attributes'''
        self.width_height = (1200, 800)
        self.bg_color = (255, 255, 255)

        # ship settings and reset
        self.ship_speed_factor = 1

        # bullet settings
        self.bullet_speed_factor = 0.5
        self.bullet_limit = 1

        # game statistics settings
        self.miss = 3
        self.hit = 0

        # level up settings
        self.speedup_scale = 1.25
        self.level_up_hit = 1

        self.init_dynamic_settings()

    def init_dynamic_settings(self):
        '''Reset ememy speed and level'''
        # enemy settings
        self.enemy_speed_factor = 0.25
        self.level_up_init = self.level_up_hit

    def level_up(self):
        '''level up as hit the enemy'''
        self.enemy_speed_factor *= self.speedup_scale
        self.level_up_init += self.level_up_hit