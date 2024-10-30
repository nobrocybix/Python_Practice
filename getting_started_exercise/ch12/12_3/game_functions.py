import sys
import pygame

def check_events(loli):
    """響應按鍵和滑鼠事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        check_key_down(event, loli)           
        check_key_up(event, loli)


def update_screen(ai_settings, screen, loli):
    """更新螢幕上的影象，並切換到新螢幕"""
	# 每次循環時都重繪螢幕   
    screen.fill(ai_settings.bg_color)
    loli.blitme()
    # 讓最近繪製的螢幕可見
    pygame.display.flip()

def check_key_down(event, loli):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            loli.moving_right = True
        elif event.key == pygame.K_LEFT:
            loli.moving_left = True
        elif event.key == pygame.K_UP:
            loli.moving_up = True
        elif event.key == pygame.K_DOWN:
            loli.moving_down = True 

def check_key_up(event, loli):
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            loli.moving_right = False
        elif event.key == pygame.K_LEFT:
            loli.moving_left = False
        elif event.key == pygame.K_UP:
            loli.moving_up = False
        elif event.key == pygame.K_DOWN:                
            loli.moving_down = False
    