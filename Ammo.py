import pygame
import Vector
import copy
class Ammo(object):
    '''
    classdocs
    '''
    def __init__(self, place):
        self.name= "def"
        self.place = copy.copy(place)
        
        
        self.speedY = -7
        
        #list of hitboxes items are in form [[x1, x2], [y1,y2]]
        self.hitbox = [[0,0],[1,1]]
        self.hitboxd = 3
        
    def move(self):
        self.place.y += self.speedY
        if(self.place.y>0):
            return 0
        return 1