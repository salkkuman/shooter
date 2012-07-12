import pygame
import Vector
class Ammo(object):
    '''
    classdocs
    '''
    def __init__(self, x,y):
        self.name= "def"
        self.place = Vector.Vector(x,y)
        
        
        self.speedY = -7
        
        #list of hitboxes items are in form [[x1, x2], [y1,y2]]
        self.hitbox = [[0,0],[20,20]]
        
    def move(self):
        self.place.y += self.speedY
        if(self.place.y>0):
            return 0
        return 1