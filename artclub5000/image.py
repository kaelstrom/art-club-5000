import pygame
from random import randint

class Image(object):
    def __init__(self):
        self.reset()
        self.randomize()
        
    def reset(self):
        self.surf = pygame.Surface((240,240))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect()
        self.colors = [(200,0,0),(0,200,0),(0,0,200)]
        self.circles = 0
        self.squares = 0
        self.stamp_size = 40
        self.judged = False
        
    def draw(self, screen):
        screen.blit(self.surf, self.rect)
        
    def drawsquare(self, x, y, color=(255,255,255)):
        self.surf.fill(color, (x-self.stamp_size/2.0, y-self.stamp_size/2.0, self.stamp_size, self.stamp_size))
        
    def drawcircle(self, x, y, color=(255,255,255)):
        pygame.draw.circle(self.surf, color, (x,y), int(self.stamp_size/2.0))
        
    def randomize(self):
        self.surf.fill((255,255,255))
        self.colors = []
        for i in range(3):
            self.colors.append([randint(0,255), randint(0,255), randint(0,255)])
        for i in range(randint(0,10)*2):
            self.squares += 1
            self.drawsquare(randint(0,240),randint(0,240), self.colors[randint(0,2)])
        for i in range(randint(0,10)*2):
            self.circles += 1
            self.drawcircle(randint(0,240),randint(0,240), self.colors[randint(0,2)])