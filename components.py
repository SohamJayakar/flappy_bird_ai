import pygame

class Ground:
    ground_lvl = 500

    def  __init__(self, win_w):
        self.x, self.y = 0, Ground.ground_lvl
        self.rect = pygame.Rect(self.x,self.y, win_w, 5)

    def draw(self,window):
        pygame.draw.rect(window, (255,255,255), self.rect)