import sys
import pygame


def update_screen(ai_settings, screen, loli):
    """更新螢幕上的影象，並切換到新螢幕"""
	# 每次循環時都重繪螢幕   
    screen.fill(ai_settings.bg_color)
    loli.blitme()
    # 讓最近繪製的螢幕可見
    pygame.display.flip()
    