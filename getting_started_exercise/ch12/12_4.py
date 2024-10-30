import pygame
import sys


def run_game():
    pygame.init()

    screen_width = 800
    screen_height = 400
    blackground_color = (0, 0, 0)
    text_color = (255, 255, 255)

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Pygame")

    font = pygame.font.SysFont(None, 48)
    text = font.render('Hello, Pygame!', 1, text_color)  # 渲染文字
    text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))  # 獲取文字的矩形，並設定其中心位置

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print(event.key)                  
                                           
        screen.fill(blackground_color)
        screen.blit(text, text_rect) 
        pygame.display.flip()

run_game()