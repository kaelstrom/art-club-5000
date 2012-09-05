import pygame, image

class Editor(object):
    def __init__(self):
        self.activecolor=(255,0,0)
        self.activetool = ''
        self.image = image.Image()
        self.imagerect = self.image.surf.get_rect().move(192+144, 120)
        self.image.reset()
        
        self.color1 = (255,0,0)
        self.color2 = (0,255,0)
        self.color3 = (0,0,255)
        self.activetool = self.tool1 = self.image.drawsquare
        self.tool2 = self.image.drawcircle
        
        self.color1surf = pygame.Surface((64,64))
        self.color1surf.fill(self.color1)
        self.color1rect = self.color1surf.get_rect().move(64, 72)
        self.color2surf = pygame.Surface((64,64))
        self.color2surf.fill(self.color2)
        self.color2rect = self.color1surf.get_rect().move(64, 72*2)
        self.color3surf = pygame.Surface((64,64))
        self.color3surf.fill(self.color3)
        self.color3rect = self.color1surf.get_rect().move(64, 72*3)
        
        self.tool1surf = pygame.Surface((64,64))
        self.tool1surf.fill((0,0,0))
        self.tool1surf.fill((255,255,255), (8,8,48,48))
        self.tool1rect = self.color1surf.get_rect().move(64, 72*5)
        self.tool2surf = pygame.Surface((64,64))
        self.tool2surf.fill((0,0,0))
        pygame.draw.circle(self.tool2surf, (255,255,255), (32,32), 24)
        self.tool2rect = self.color1surf.get_rect().move(64, 72*6)
        
    def mouse_click(self, pos):
        if self.color1rect.collidepoint(pos):
            self.activecolor = self.color1
        if self.color2rect.collidepoint(pos):
            self.activecolor = self.color2
        if self.color3rect.collidepoint(pos):
            self.activecolor = self.color3
            
        if self.tool1rect.collidepoint(pos):
            self.activetool = self.tool1
        if self.tool2rect.collidepoint(pos):
            self.activetool = self.tool2
            
        if self.imagerect.collidepoint(pos):
            self.activetool(pos[0]-self.imagerect.x, pos[1]-self.imagerect.y, self.activecolor)
        
    def draw(self, screen):
        screen.fill((255,255,255),(self.color1rect.left-16, self.color1rect.top-48, 64+32, 32+72*3+16))
        surf = self.font.render('COLOR', True, (50,50,50))
        rect = surf.get_rect()
        rect.center = (64+32, 48)
        screen.blit(surf, rect)
        screen.blit(self.color1surf, self.color1rect)
        screen.blit(self.color2surf, self.color2rect)
        screen.blit(self.color3surf, self.color3rect)
        
        screen.fill((255,255,255),(self.tool1rect.left-16, self.tool1rect.top-48, 64+32, 32+72*2+16))
        surf = self.font.render('TOOL', True, (50,50,50))
        rect = surf.get_rect()
        rect.center = (64+32, 48+72*4)
        screen.blit(surf, rect)
        screen.blit(self.tool1surf, self.tool1rect)
        screen.blit(self.tool2surf, self.tool2rect)
        
        screen.fill((80,80,80), self.imagerect.inflate(20,20))
        screen.blit(self.image.surf, self.imagerect)
        
        
        