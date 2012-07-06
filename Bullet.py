'''
Created on 2012/07/05

@author: Eero
'''

class Bullet():
    def __init__(self,x,y,speedX,speedY):
        self.name= "def"
        self.x = 200
        self.y = 200
        self.speedX = 0
        self.speedY = 0
        self.accX = 0
        self.accY = 0
    
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
