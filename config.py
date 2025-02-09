import components
import pygame


win_height = 720
win_width = 550
window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Flappy bird( Generic algorithm )")


ground = components.Ground(win_width)
pipes = []