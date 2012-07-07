import pygame
class Ammo(object):
    '''
    classdocs
    '''
    def __init__(self, x,y):
        self.name= "def"
        self.x = x
        self.y = y
        
        self.speedY = -7
        
        #list of hitboxes items are in form [[x1, x2], [y1,y2]]
        self.hitbox = [[0,0],[20,20]]
        
    def move(self):
        self.y += self.speedY
        if(self.y>0):
            return 0
        return 1