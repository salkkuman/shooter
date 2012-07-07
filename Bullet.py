
import pygame


class Bullet():
    
    def __init__(self,x,y,speedX,speedY, hitbox):
        self.name= "def"
        self.x = x
        self.y = y
        self.speedX = speedX
        self.speedY = speedY
        self.accX = 0
        self.accY = 0
        #list of hitboxes items are in form [[x1, x2], [y1,y2]]
        self.hitbox = hitbox
        self.sprite = pygame.image.load("bullet2.png").convert()
        self.sprite.set_colorkey((255,0,255))
    
    
    
    def move(self):
        
        self.x+=int(self.speedX)
        if(self.x<40):
            return 1
           
            
        if(self.x>720):
            return 1
            
            
            
        self.y+=int(self.speedY)
        if(self.y<0):
            return 1
            
            
        if(self.y>720):
            return 1
        return 0
    
    def draw(self,screen):
        screen.blit(self.sprite, [self.x,self.y])
    
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
