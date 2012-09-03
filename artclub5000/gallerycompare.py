import pygame

class GalleryCompare(object):
    def __init__(self):
        self.image_a = pygame.Surface((240,240))
        self.image_b = pygame.Surface((240,240))
        self.image_a_rect = self.image_a.get_rect()
        self.image_b_rect = self.image_b.get_rect()
        self.image_a_rect.topright = (320, 80)
        self.image_b_rect.topleft = (400, 80)
        self.generate_backdrop()
        
    def set_images(self, image_a, image_b):
        self.image_a = image_a
        self.image_b = image_b
        
    def draw(self, screen):
        screen.blit(self.backdrop, (0,0))
        screen.blit(self.image_a.surf, self.image_a_rect)
        screen.blit(self.image_b.surf, self.image_b_rect)
        
    def generate_backdrop(self):
        self.backdrop = pygame.Surface((1080,640)) 
        self.backdrop.fill((0,0,0))
        self.backdrop.fill((80,80,80), self.image_a_rect.inflate(20,20))
        self.backdrop.fill((80,80,80), self.image_b_rect.inflate(20,20))