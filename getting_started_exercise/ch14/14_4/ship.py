import pygame 
from pygame.sprite import Sprite

class Ship(Sprite):  
    def __init__(self, ai_settings, screen): 
        """初始化飞船并设置其初始位置"""
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings        

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load(r"D:\temp\Python\Python_Practice\getting_started_exercise\alien_invasion\images\ship.bmp")  # 加載飛船的圖片
        self.rect = self.image.get_rect()  # 獲取圖片的外接矩形，這個矩形用來控制飛船的位置和大小
        self.screen_rect = screen.get_rect()  # 獲取屏幕的外接矩形，這樣可以用來對齊飛船

        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx  # 將飛船的中心點設置為屏幕的中心
        self.rect.bottom = self.screen_rect.bottom  # 將飛船的底部設置為屏幕的底部

        self.center = float(self.rect.centerx)

        self.moving_right = False  # 初始化移動標誌，表示飛船初始不向右移動
        self.moving_left = False

    def update(self):  
        """根據移動標誌調整飛船的位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:  
            self.center += self.ai_settings.ship_speed_factor  
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        
        self.rect.centerx = self.center

    def blitme(self):  
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)  # 將飛船的圖片繪製到屏幕上

    def center_ship(self):
        '''Center the ship on the screen.'''
        self.center = self.screen_rect.centerx
