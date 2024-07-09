import pygame
import components

win_h = 720
win_w = 550

window = pygame.display.set_mode([win_w,win_h])

ground = components.Ground(win_w)

pipes = []