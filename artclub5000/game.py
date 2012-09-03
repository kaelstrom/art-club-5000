import image, pygame, gallerycompare, sys

def run_game():
    g = Game()

class Game(object):
    def __init__(self):
        self.objects = []
        self.objects.append(gallerycompare.GalleryCompare())
        self.objects[0].set_images(image.Image(), image.Image())
        self.screen = pygame.display.set_mode((720,640))
        self.clock = pygame.time.Clock()
        self.running = True
        self.game_loop()
        
    def game_loop(self):
        while self.running:
            self.clock.tick(60)
            self.input()
            self.logic()
            self.draw()
        
    def input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                sys.exit()
        
    def logic(self):
        pass
    
    def draw(self):
        for e in self.objects:
            if e.draw:
                e.draw(self.screen)
        pygame.display.flip()