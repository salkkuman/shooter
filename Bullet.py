
import pygame
import math

class Bullet():
    
    def __init__(self, x, y, speedX, speedY, hitbox, type1):
        self.name = "def"
        self.x = x
        self.y = y
        self.speedX = speedX
        self.speedY = speedY
        self.accX = 0
        self.accY = 0
        #list of hitboxes items are in form [[x1, x2], [y1,y2]]
        self.hitbox = hitbox
        self.sprite = pygame.image.load("kaitendama32.png").convert()
        self.sprite.set_colorkey((0, 100, 100))
        self.rotate_angle = 0
        self.angle = 0
        self.time = 0
        self.timeout = -1
        self.bullettype = 0
        self.targeting = 0
        if(type1==1):
            self.hitbox = hitbox
            self.sprite = pygame.image.load("kaitendama32.png").convert()
            self.sprite.set_colorkey((0, 100, 100))
            self.angle = 3
            self.rotate_angle = 32
        if(type1==2):
            self.hitbox = hitbox
            self.sprite = pygame.image.load("bullet2.png").convert()
            self.sprite.set_colorkey((255, 0, 255))
            self.angle = 0
        if(type1==3):
            self.hitbox = hitbox
            self.sprite = pygame.image.load("bullet3.png").convert()
            self.sprite.set_colorkey((0,0,0))
            self.angle = 0
        if(type1==4):
            self.hitbox = hitbox
            self.sprite = pygame.image.load("pacman40.png").convert()
            self.sprite.set_colorkey((255,255,255))
            self.angle = 0
            
        if(type1==5):
            self.hitbox = hitbox
            self.sprite = pygame.image.load("bullet4_40.png").convert()
            self.sprite.set_colorkey((0,0,0))
            self.angle = 0
            self.timeout = 40
            self.bullettype = 1
            self.targeting = 1
    
    def move(self):
        
        self.x += self.speedX
        if(self.x < 40):
            return 1
           
            
        if(self.x > 720):
            return 1
            
            
            
        self.y += self.speedY
        if(self.y < 0):
            return 1
            
            
        if(self.y > 720):
            return 1
        self.time+=1
        if(self.time==self.timeout):
            
            return 2
            
        return 0
    
    def draw(self, screen):
        self.angle+= self.rotate_angle #rotate nopeus
        if self.angle >= 359:
            self.angle = 0   
        screen.blit(pygame.transform.rotate(self.sprite, self.angle), [int(self.x), int(self.y)])
    
    def shoot(self,bulletlist,player):
    #hakeutuvia bullettei
        print("hajoava ampuu")
        if(self.targeting == 1):
            
            speedx1=player.x-self.x-25
            speedy1=player.y-self.y-25
            speedx=7*speedx1/(math.sqrt(speedx1*speedx1+speedy1*speedy1))
            speedy=7*speedy1/(math.sqrt(speedx1*speedx1+speedy1*speedy1))
        
            bulletlist.append(Bullet(self.x+(self.hitbox[0][1]-self.hitbox[0][0])/2, self.y,speedx,speedy, [[0,40],[0,40]],self.bullettype))
        else:
            
       
            bulletlist.append(Bullet(self.x+((self.hitbox[0][1]-self.hitbox[0][0])/2), self.y,1,5, [[0,40],[0,40]],self.bullettype))
            bulletlist.append(Bullet(self.x+((self.hitbox[0][1]-self.hitbox[0][0])/2), self.y,-1,5, [[0,40],[0,40]],self.bullettype))
