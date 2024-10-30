import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """一個對飛船發射的子彈進行管理的類"""

    def __init__(self, ai_settings, screen, ship):
        """在飛船所處的位置創建一個子彈對象"""
        super(Bullet, self).__init__()  # 調用父類的初始化方法
        self.screen = screen  # 將螢幕對象賦值給實例屬性

        # 在(0,0)處創建一個表示子彈的矩形，再設置正確的位置
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)  # 建立子彈的矩形
        self.rect.centerx = ship.rect.centerx  # 將子彈的中心 X 坐標設置為飛船的中心 X 坐標
        self.rect.top = ship.rect.top  # 將子彈的上邊界設置為飛船的上邊界

        # 存儲用小數表示的子彈位置
        self.y = float(self.rect.y)  # 使用浮點數來表示子彈的 Y 位置，以便於精確計算
        self.color = ai_settings.bullet_color  # 設置子彈顏色
        self.speed_factor = ai_settings.bullet_speed_factor  # 設置子彈的速度因子

    def update(self):
        """向上移動子彈"""
        # 更新表示子彈位置的小數值
        self.y -= self.speed_factor  # 根據速度因子減少子彈的 Y 位置
        # 更新表示子彈的 rect 的位置
        self.rect.y = self.y  # 將矩形的 Y 坐標設置為更新後的 Y 位置

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)