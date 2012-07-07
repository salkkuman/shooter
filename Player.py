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
        
    def changespeed(self,x,y):    
        self.speedX+=x
        self.speedY+=y
        
    def changeacc(self,x,y):     
        self.accX+=x
        self.accY+=y
        if(self.accX>0.42):
            self.accX=0.42
        if(self.accY>0.42):
            self.accY=0.42
        
        if(self.accX<-0.42):
            self.accX=-0.42
        if(self.accY<-0.42):
            self.accY=-0.42
        
        if(self.accX<0.1 and self.accX>0):
            self.accX=0.1
        if(self.accX>-0.1 and self.accX<0):
            self.accX=-0.1
            
        if(self.accY<0.1 and self.accY>0):
            self.accY=0.1
        if(self.accY>-0.1 and self.accY<0):
            self.accY=-0.1
    
    def stop(self):
        self.speedX = 0
        self.speedY = 0
        self.accX = 0
        self.accY = 0
        
    def stopX(self):
        self.speedX = 0
        
        
        
    def stopY(self):
        
        self.speedY = 0
        
        
   
    
    def move(self):
        self.x+=int(self.speedX)
        if(self.x<40):
            self.x=40
            
        if(self.x>720):
            self.x=720
            
        self.y+=int(self.speedY)
        if(self.y<0):
            self.y=0
            
        if(self.y>720):
            self.y=720
           
        self.speedX+=self.accX
        self.speedY+=self.accY
        
        minspeed=0.1
        if(self.speedY<minspeed and self.speedY>0):
            self.speedY=minspeed
        if(self.speedX<minspeed and self.speedX>0):
            self.speedX=-minspeed
        if(self.speedY>minspeed and self.speedY<0):
            self.speedY=minspeed
        if(self.speedX>minspeed and self.speedX<0):
            self.speedX=-minspeed
        
        maxspeed=4.2
        if(self.speedY>maxspeed):
            self.speedY=maxspeed
        if(self.speedX>maxspeed):
            self.speedX=maxspeed
        if(self.speedY<-maxspeed):
            self.speedY=-maxspeed
        if(self.speedX<-maxspeed):
            self.speedX=-maxspeed
    # hp = ""
    #x = 0
    #y = 0
    