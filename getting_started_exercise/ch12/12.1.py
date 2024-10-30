import pygame
import sys

def run_game():
    pygame.init()

    screen_width = 1600
    screen_height = 800
    blackground_color = (0,44, 130)

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Pygame")

    running = True  
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                sys.exit()

        screen.fill(blackground_color)
        pygame.display.flip()

run_game()