import pygame

class Critic(object):
    def __init__(self, font):
        self.color = (127,127,127)
        self.squares = .5
        self.circles = .5
        self.squarestmp = []
        self.circlestmp = []
        self.negative_space = .5
        self.clustering = .5
        self.winners = []
        self.images = []
        self.rank = 1
        
        self.font = font
        self.playerimage = pygame.Surface((240,240))
        self.imagesurf = self.playerimage.get_rect()
        self.imagesurf.center = (360,240)
        
        self.bannersurf = self.font.render('JUDGING', True, (255,255,255))
        self.bannerrect = self.bannersurf.get_rect()
        self.bannerrect.center = (360, 128)
        
        
    def vs(self, winner, loser):
        self.winners.append(winner)
        self.images.append(winner)
        self.images.append(loser)
        
    def determine_profile(self):
        for w in self.winners:
            self.squarestmp.append(w.squares)
            self.circlestmp.append(w.circles)
            
        self.squares = sum(self.squarestmp)/len(self.squarestmp)
        self.circles = sum(self.circlestmp)/len(self.circlestmp)
        
    def set_rating(self, image):
        image.rating = abs(image.squares - self.squares) + abs(image.circles - self.circles)
        
    def judge(self, image):
        self.playerimage = image
        for image in self.images:
            self.set_rating(image)
        self.set_rating(self.playerimage)
        for image in self.images:
            if image.rating < self.playerimage.rating:
                self.rank += 1
        
    def draw(self, screen):
        screen.blit(self.bannersurf, self.bannerrect)
        screen.blit(self.playerimage.surf, self.imagesurf)
        self.scoresurf = self.font.render('Your rank: #' + str(self.rank), True, (255,255,255))
        self.scorerect = self.scoresurf.get_rect()
        self.scorerect.center = (360, 400)
        screen.blit(self.scoresurf, self.scorerect)