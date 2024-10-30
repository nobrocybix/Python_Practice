from star import Star
import pygame

def create_star_row(screen, stars):
    num_stars = 8
    x_offset = 50

    for num_star in range(num_stars):
        star = Star(screen)
        star.rect.x = x_offset
        x_offset += 200
        stars.add(star)

def update(screen, image, image_rect, stars): 
    screen.blit(image, image_rect)
    stars.draw(screen)
    pygame.display.flip()