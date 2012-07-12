import pygame
import Bullet
import math
import Vector
class EnemyUnit():
    
    def __init__(self,x,y, types):
        self.name= "def"
        self.place = Vector.Vector(x,y)
        self.place.x = x
        self.place.y = y
        self.place.x0 = x
        self.place.y0 = y
        self.speedX = 0
        self.speedY = 0
        self.accX = 0
        self.accY = 0
        #list of hitboxes items are in form [xcoordinate, ycoordinate]
        self.hitbox = []
        self.hitboxd=1
        self.timer = 0
        self.timetoshoot = 0
        self.hp = 1
        self.bulletype =1
        self.type=types
        if(types==1):
            self.speedY = 1
            self.hitbox=[0,40],[0,40]
            self.sprite = pygame.image.load("enemy.png").convert()
            self.sprite.set_colorkey((255,0,255))
            self.timetoshoot = 0
            self.bulletype=3
        if(types==2):
            self.speedY = 0
            self.hitbox=[10,120],[0,140]
            self.sprite = pygame.image.load("paivi150.png").convert()
            self.sprite.set_colorkey((255,0,255))
            self.timetoshoot = 0
            self.hp = 200
            self.bulletype=5
        if(types==3):
            self.speedY = 0
            self.speedX = 1
            self.hitbox=[0,50],[0,50]
            self.sprite = pygame.image.load("pacman_ghost1.png").convert()
            self.sprite.set_colorkey((0,0,0))
            self.timetoshoot = 0
            self.hp = 2
            self.bulletype=4
        if(types==4):
            self.speedY = 0
            self.speedX = 1
            self.hitbox=[0,50],[0,50]
            self.sprite = pygame.image.load("pacman_ghost2.png").convert()
            self.sprite.set_colorkey((0,0,0))
            self.timetoshoot = 0
            self.hp = 2
            self.bulletype=4
        if(types==5):
            self.speedY = 0
            self.speedX = 1
            self.hitbox=[0,50],[0,50]
            self.sprite = pygame.image.load("pacman_ghost3.png").convert()
            self.sprite.set_colorkey((0,0,0))
            self.timetoshoot = 0
            self.hp = 2
            self.bulletype=4
        if(types==6):
            self.speedY = 0
            self.speedX = 1
            self.hitbox=[0,50],[0,50]
            self.sprite = pygame.image.load("pacman_ghost4.png").convert()
            self.sprite.set_colorkey((0,0,0))
            self.timetoshoot = 0
            self.hp = 2
            self.bulletype=4
    def hit(self):
        self.hp-=1
        if (self.hp == 0):
            return 1
        return 0
    def draw(self,screen):
        screen.blit(self.sprite, [int(self.place.x),int(self.place.y)])
    
    def move(self):
        if(self.type==3 or self.type==4 or self.type==5 or self.type==6 ):
            datime=150
            if(self.timer%datime==0):
                self.speedY=0
                self.speedX=2
            if(self.timer%datime==int(datime/4)):
                self.speedY=2
                self.speedX=0
            if(self.timer%datime==int(datime/2)):
                self.speedY=0
                self.speedX=-2
            if(self.timer%datime==int(datime*3/4)):
                self.speedY=2
                self.speedX=0
        
        self.place.x+=self.speedX
        if(self.place.x<40):
            return 1
           
        if(self.place.x>720):
            return 1   
            
        self.place.y+=self.speedY
        if(self.place.y<0):
            return 1
            
        if(self.place.y>720):
            return 1
        return 0
    
    def time(self):
        self.timer+=1
    def shoot(self,bulletlist,player):
        #hakeutuvia bullettei
        if(self.type==3 or self.type==4 or self.type==5 or self.type==6 ):
            if(self.timer%20==0):
                speedx1=player.place.x-self.place.x-25
                speedy1=player.place.y-self.place.y-25
                speedx=7*speedx1/(math.sqrt(speedx1*speedx1+speedy1*speedy1))
                speedy=7*speedy1/(math.sqrt(speedx1*speedx1+speedy1*speedy1))
            
                bulletlist.append(Bullet.Bullet(self.place.x+(self.hitbox[0][1]-self.hitbox[0][0])/2, self.place.y,speedx,speedy, [[0,40],[0,40]],self.bulletype))
        else:
            if(self.timer%20==0):
           
                bulletlist.append(Bullet.Bullet(self.place.x+((self.hitbox[0][1]-self.hitbox[0][0])/2), self.place.y,1,5, [[0,40],[0,40]],self.bulletype))
                bulletlist.append(Bullet.Bullet(self.place.x+((self.hitbox[0][1]-self.hitbox[0][0])/2), self.place.y,-1,5, [[0,40],[0,40]],self.bulletype))