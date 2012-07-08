import pygame
import Bullet
class EnemyUnit():
    
    def __init__(self,x,y, type):
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
        self.hp = 1
        if(type==1):
            self.speedY = 1
            self.hitbox=[0,40],[0,40]
            self.sprite = pygame.image.load("enemy.png").convert()
            self.sprite.set_colorkey((255,0,255))
            self.timetoshoot = 0
        if(type==2):
            self.speedY = 0
            self.hitbox=[10,120],[0,140]
            self.sprite = pygame.image.load("paivi150.png").convert()
            self.sprite.set_colorkey((255,0,255))
            self.timetoshoot = 0
            self.hp = 200
    def hit(self):
        self.hp-=1
        if (self.hp == 0):
            return 1
        return 0
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
        
        if(self.timer%20==0):
            print
            bulletlist.append(Bullet.Bullet(self.x+int((self.hitbox[0][1]-self.hitbox[0][0])/2), self.y+int((self.hitbox[1][1]-self.hitbox[1][0])/2),1,5, [[0,40],[0,40]]))
            bulletlist.append(Bullet.Bullet(self.x+int((self.hitbox[0][1]-self.hitbox[0][0])/2), self.y+int((self.hitbox[1][1]-self.hitbox[1][0])/2),-1,5, [[0,40],[0,40]]))