import pygame

class Critic(object):
    def __init__(self):
        self.color = (127,127,127)
        self.squares = .5
        self.circles = .5
        self.negative_space = .5
        self.clustering = .5
        self.judgements = []
        
    def vs(self, winner, loser):
        self.judgements.append([winner, loser])
        
    def judge(self, image):
        rating = 0
        
    def draw(self, screen):
        pass
        