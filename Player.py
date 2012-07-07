import pygame
import math

class Player:
    def __init__(self):
        self.name= "def"
        self.x = 200
        self.y = 200
        self.speedX = 0
        self.speedY = 0
        self.accX = 0
        self.accY = 0
        self.mov_speed = 3
    
    def movespeed(self,movespeed):
        self.mov_speed = movespeed
    def reset(self):
        self.x = 200
        self.y = 200
        self.speedX = 0
        self.speedY = 0
        #self.accX = 0
        #self.accY = 0
    def changeplace(self,x,y):    
        self.x+=x
        self.y+=y
        
    def changespeedX(self,x):    
        self.speedX=x
    def changespeedY(self,y):    
        self.speedY=y
        
        

    
    def move(self):
        x = self.speedX * self.mov_speed
        y = self.speedY * self.mov_speed
        self.x+=x
        if(self.x<40):
            self.x=40
            
        if(self.x>720):
            self.x=720
            
        self.y+=y
        if(self.y<0):
            self.y=0
            
        if(self.y>720):
            self.y=720
           
        
        

    # hp = ""
    #x = 0
    #y = 0
    