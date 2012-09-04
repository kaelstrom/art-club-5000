import image, pygame, gallerycompare, sys

def run_game():
    g = Game()

class Game(object):
    def __init__(self):
        self.objects = []
        self.gc = gallerycompare.GalleryCompare()
        self.screen = pygame.display.set_mode((720,640))
        self.clock = pygame.time.Clock()
        self.running = True
        self.images = []
        for i in range(20):
            self.images.append(image.Image())
        self.image_a_index = 0
        self.image_b_index = 1
        self.gc.set_images(self.images[self.image_a_index], self.images[self.image_b_index])
        self.actions = {}
        self.actions['cycle image a'] = False
        self.actions['cycle image b'] = False
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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.actions['cycle image b'] = True
                if event.key == pygame.K_RIGHT:
                    self.actions['cycle image a'] = True
        
    def logic(self):
        if self.actions['cycle image a']:
			self.actions['cycle image a'] = False
			self.image_a_index = (self.image_a_index + 1) % len(self.images)
			self.gc.set_images(self.images[self.image_a_index], self.images[self.image_b_index])
        if self.actions['cycle image b']:
			self.actions['cycle image b'] = False
			self.image_b_index = (self.image_b_index + 1) % len(self.images)
			self.gc.set_images(self.images[self.image_a_index], self.images[self.image_b_index])
    
    def draw(self):
        self.gc.draw(self.screen)
        for e in self.objects:
            if e.draw:
                e.draw(self.screen)
        pygame.display.flip()