class Settings():  # 定義一個名為 Settings 的類
    """儲存《外星人入侵》的所有設定的類"""

    def __init__(self):  # 初始化函數，用於設置初始值
        """初始化遊戲的設定"""
        # 螢幕設定
        self.screen_width = 1200  # 螢幕的寬度設為 1200 畫素
        self.screen_height = 800  # 螢幕的高度設為 800 畫素
        self.bg_color = (230, 230, 230)  # 背景顏色設為淺灰色 (RGB 值)      

        # 子彈設定       
        self.bullet_width = 30
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # alien settings
        self.ship_limit = 3
        self.fleet_drop_speed = 10
        
        # How quickly the game speeds up.
        self.speedup_scale = 1.1
        # How quickly the alien point values increase.
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""

        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 1
        self.alien_speed_factor = 1

        # fleet_direction of 1 represents right, -1 represents left
        self.fleet_direction = 1

        # Scoring.
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)