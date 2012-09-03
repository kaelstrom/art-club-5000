import pygame
from random import randint

class Image(object):
    def __init__(self):
        self.surf = pygame.Surface((240,240))
        self.surf.fill((50,0,0))
        self.rect = self.surf.get_rect()
        self.colors = [(200,0,0),(0,200,0),(0,0,200)]
        self.stamp_size = 20
        #print 'making a new image'
        self.randomize()
        
    def draw(self, screen):
        screen.blit(self.surf, self.rect)
        
    def drawsquare(self, x, y, color=(255,255,255)):
        self.surf.fill(color, (x-self.stamp_size/2.0, y-self.stamp_size/2.0, self.stamp_size, self.stamp_size))
        
    def randomize(self):
        self.surf.fill((255,255,255))
        self.colors = []
        for i in range(3):
            self.colors.append([randint(0,255), randint(0,255), randint(0,255)])
        for i in range(randint(6,18)):
            self.drawsquare(randint(0,240),randint(0,240), self.colors[randint(0,2)])