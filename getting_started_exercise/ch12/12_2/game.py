import sys
import pygame
from setting import Setting
from loli import Loli
import game_functions as gf

def run_game():

    pygame.init()
    ai_settings = Setting()

    screen = pygame.display.set_mode(((
        ai_settings.screen_width, ai_settings.screen_height)))  # 設定顯示視窗的大小為 1200x800 畫素
    pygame.display.set_caption("Loli")

    loli = Loli(screen, ai_settings)

    while True:
        loli.update()
        gf.update_screen(ai_settings, screen, loli)

run_game()