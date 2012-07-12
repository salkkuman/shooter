
import pygame
import math
import Vector

class Bullet():
    
    def __init__(self, place, speed, type1):
        self.name = "def"
        self.place = place
        self.speed = speed
        
        self.acc = Vector.Vector(0,0)
        #list of hitboxes items are in form [[x1, x2], [y1,y2]]
        self.hitboxd=10
        self.hitbox = [[0,0],[20,20]]
        self.sprite = pygame.image.load("../kuvat/kaitendama32.png").convert()
        self.sprite.set_colorkey((0, 100, 100))
        self.rotate_angle = 0
        self.angle = 0
        self.time = 0
        self.timeout = -1
        self.bullettype = 0
        #if 1 goes to player way
        self.targeting = 0
        self.focus = None
        
        if(type1==1):
            
            self.sprite = pygame.image.load("../kuvat/kaitendama32.png").convert()
            self.sprite.set_colorkey((0, 100, 100))
            self.angle = 3
            self.rotate_angle = 32
        if(type1==2):
            
            #ympyra ratainen
            self.sprite = pygame.image.load("../kuvat/bullet2.png").convert()
            self.sprite.set_colorkey((255, 0, 255))
            self.angle = 0
            
        if(type1==3):
            
            self.sprite = pygame.image.load("../kuvat/bullet3.png").convert()
            self.sprite.set_colorkey((0,0,0))
            self.angle = 0
        if(type1==4):
            
            self.sprite = pygame.image.load("../kuvat/pacman40.png").convert()
            self.sprite.set_colorkey((255,255,255))
            self.angle = 0
            
        if(type1==5):   
            self.sprite = pygame.image.load("../kuvat/bullet4_40.png").convert()
            self.sprite.set_colorkey((0,0,0))
            self.angle = 0
            self.timeout = 40
            self.bullettype = 1
            self.targeting = 1
    
    def move(self):
        if(self.focus!=None):
            #v^2/r
            r=Vector.Distance(self.place, self.focus)
            v2=Vector.LengthSqrd(self.speed)
            #v2*=v2
            v2*=v2
            #keskikiihtyvyys=(v2/r)-0.13
            keskikiihtyvyys=(v2/r)+0.7
            suunta=self.place.__sub__(self.focus)
            #print(suunta)
            a=Vector.Normalize(suunta)
            a.__imul__(keskikiihtyvyys)
            self.acc=a
        self.speed+=self.acc
        self.place+=self.speed
        #tangentialize speed
        if(self.focus!=None):
            vector = self.focus.__sub__(self.place)
            speed = vector
            speed = Vector.Rotate(speed,90)
            speed = Vector.Normalize(speed)
            speed.__imul__(2.4)
            self.speed=speed
        if(self.place.x < 40):
            return 1
           
            
        if(self.place.x > 720):
            return 1
            
            
            
        
        if(self.place.y < 0):
            return 1
            
            
        if(self.place.y > 720):
            return 1
        self.time+=1
        if(self.time==self.timeout):
            
            return 2
            
        return 0
    def setFocus(self, vectr):
        self.focus = vectr
    def draw(self, screen):
        self.angle+= self.rotate_angle #rotate nopeus
        if self.angle >= 359:
            self.angle = 0   
        screen.blit(pygame.transform.rotate(self.sprite, self.angle), [int(self.place.x), int(self.place.y)])
    
    def shoot(self,bulletlist,player):
    #hakeutuvia bullettei
       
        if(self.targeting == 1):
            
            speedx1=player.place.x-self.place.x-25
            speedy1=player.place.y-self.place.y-25
            speedx=7*speedx1/(math.sqrt(speedx1*speedx1+speedy1*speedy1))
            speedy=7*speedy1/(math.sqrt(speedx1*speedx1+speedy1*speedy1))
            speed = Vector.Vector(speedx, speedy)
            bulletlist.append(Bullet(self.place, speed,self.bullettype))
        else:
            
            speed = Vector.Vector(2,5)
            bulletlist.append(Bullet(self.place, speed,self.bullettype))
            
