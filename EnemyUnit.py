import pygame
import Bullet
class EnemyUnit():
    
    def __init__(self,x,y, type1):
        self.name= "def"
        self.x = x
        self.y = y
        self.speedX = 0
        self.speedY = 0
        self.accX = 0
        self.accY = 0
        #list of hitboxes items are in form [xcoordinate, ycoordinate]
        self.hitbox = []
        self.timer = 0
        self.timetoshoot = 0
        if(type1==1):
            self.speedY = 1
            self.hitbox=[0,40],[0,40]
            self.sprite = pygame.image.load("enemy.png").convert()
            self.sprite.set_colorkey((255,0,255))
            self.timetoshoot = 0
    
    def draw(self,screen):
        screen.blit(self.sprite, [self.x,self.y])
    
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
    
    def time(self):
        self.timer+=1
    def shoot(self,bulletlist):
        if(self.timer==self.timetoshoot):
            
            bulletlist.append(Bullet.Bullet(self.x, self.y,1,5, [[0,40],[0,40]]))
            bulletlist.append(Bullet.Bullet(self.x, self.y,-1,5, [[0,40],[0,40]]))