import image, pygame, gallerycompare, sys, critic, os, editor

def run_game():
    g = Game()

class Game(object):
    def __init__(self):
        pygame.init()
        self.font = pygame.font.SysFont("pftempestaseven", 20)
        self.font48 = pygame.font.SysFont("pftempestaseven", 48)
        self.objects = []
        self.gc = gallerycompare.GalleryCompare()
        self.critic = critic.Critic(self.font)
        self.editor = editor.Editor(self.font)
        pygame.display.set_caption('ARTCLUB 5000')
        self.screen = pygame.display.set_mode((720,640))
        self.generate_curtains()
        self.clock = pygame.time.Clock()
        self.running = True
        self.images = []
        for i in range(12):
            self.images.append(image.Image())
        self.image_a_index = 0
        self.image_b_index = 1
        self.curtain_percent = 1
        self.curtain_delta = -.01
        self.gc.set_images(self.images[self.image_a_index], self.images[self.image_b_index])
        self.actions = {}
        self.actions['cycle image a'] = False
        self.actions['cycle image b'] = False
        self.actions['critic phase'] = True
        self.actions['editor phase'] = False
        self.actions['draw gallery compare'] = True
        self.actions['draw editor'] = False
        self.actions['draw results'] = False
        self.game_loop()
        
    def generate_curtains(self):
        
        self.curtaina = pygame.Surface((self.screen.get_rect().width, self.screen.get_rect().height))
        self.curtainb = pygame.Surface((self.screen.get_rect().width, self.screen.get_rect().height))
        self.curtaina.fill((50,50,50))
        self.curtainb.fill((50,50,50))
        crect = self.curtaina.get_rect()
        surf = self.font48.render('ART', True, (255,255,255))
        rect = surf.get_rect()
        rect.right = crect.right
        rect.top = crect.top + crect.height * .3
        self.curtaina.blit(surf,rect)
        surf = self.font48.render('50', True, (255,255,255))
        rect = surf.get_rect()
        rect.right = crect.right
        rect.top = crect.top + crect.height * .6
        self.curtaina.blit(surf,rect)
        surf = self.font48.render('CLUB', True, (255,255,255))
        rect = surf.get_rect()
        rect.left = crect.left
        rect.top = crect.top + crect.height * .3
        self.curtainb.blit(surf,rect)
        surf = self.font48.render('00', True, (255,255,255))
        rect = surf.get_rect()
        rect.left = crect.left
        rect.top = crect.top + crect.height * .6
        self.curtainb.blit(surf,rect)
        
    
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
                if self.actions['critic phase']:
                    if event.key == pygame.K_LEFT:
                        self.actions['cycle image b'] = True
                    if event.key == pygame.K_RIGHT:
                        self.actions['cycle image a'] = True
                    
                if event.key == pygame.K_ESCAPE:  
                    self.running = False
                    sys.exit()
                    
            if self.actions['draw editor']:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.editor.mouse_click(event.pos)
        
    def logic(self):
        if self.actions['critic phase'] and self.actions['cycle image a']:
            self.actions['cycle image a'] = False
            self.critic.vs(self.images[self.image_b_index], self.images[self.image_a_index])
            self.images.pop(self.image_a_index)
            if len(self.images) <= 2:
                self.end_critic_phase()
            else:
                self.advance_a()
                self.advance_b()
                self.gc.set_images(self.images[self.image_a_index], self.images[self.image_b_index])
        
        if self.actions['critic phase'] and self.actions['cycle image b']:
            self.actions['cycle image b'] = False
            self.critic.vs(self.images[self.image_a_index], self.images[self.image_b_index])
            self.images.pop(self.image_b_index)
            if len(self.images) <= 2:
                self.end_critic_phase()
            else:
                self.advance_a()
                self.advance_b()
                self.gc.set_images(self.images[self.image_a_index], self.images[self.image_b_index])
                
        if self.actions['editor phase']:
            if self.editor.done:
                self.end_editor_phase()
        

    def draw(self):
        self.screen.fill((0,0,0))
        if self.actions['draw gallery compare']:
            self.gc.draw(self.screen)
            self.draw_gc_text()
        if self.actions['draw editor']:
            self.editor.draw(self.screen)
        if self.actions['draw results']:
            self.critic.draw(self.screen)
        for e in self.objects:
            if e.draw:
                e.draw(self.screen)
        self.draw_curtain()
        pygame.display.flip()
        
    def draw_curtain(self):
        recta = self.screen.get_rect()
        rectb = self.screen.get_rect()
        recta.right = self.curtain_percent * (recta.width/2.0)
        rectb.left = self.curtain_percent * -(recta.width/2.0) + recta.width
        self.curtain_percent += self.curtain_delta
        self.screen.blit(self.curtaina,recta)
        self.screen.blit(self.curtainb,rectb)
        if self.curtain_percent >= 1:
            self.curtain_delta *= -1
            
            if self.actions['draw gallery compare'] == True:
                self.actions['draw editor'] = True
                self.actions['editor phase'] = True
                self.actions['draw gallery compare'] = False
            elif self.actions['draw editor'] == True:
                self.actions['draw results'] = True
                self.actions['draw editor'] = False
        
    def draw_gc_text(self):
        text = ''
        if self.actions['critic phase']:
            text = '%d judgements to go!'%(len(self.images)-2)
        textsurf = self.font.render(text, True, (255,255,255))
        textrect = textsurf.get_rect()
        textrect.center = self.screen.get_rect().center
        textrect.top = 8
        self.screen.blit(textsurf,textrect)
        
    def end_critic_phase(self):
        self.actions['critic phase'] = False
        self.curtain_percent = 0
        self.curtain_delta *= -1
        
    def end_editor_phase(self):
        self.actions['editor phase'] = False
        self.curtain_percent = 0
        self.curtain_delta *= -1
        self.critic.determine_profile()
        self.critic.judge(self.editor.image)
        
    def advance_a(self):
        self.image_a_index = (self.image_a_index + 1) % len(self.images)
        if self.image_a_index == self.image_b_index:
            self.advance_a()
            
    def advance_b(self):    
        self.image_b_index = (self.image_b_index + 1) % len(self.images)
        if self.image_a_index == self.image_b_index:
            self.advance_b()