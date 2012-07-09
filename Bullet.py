
import pygame


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
        return 0
    
    def draw(self, screen):
        self.angle+= self.rotate_angle #rotate nopeus
        if self.angle >= 359:
            self.angle = 0   
        screen.blit(pygame.transform.rotate(self.sprite, self.angle), [int(self.x), int(self.y)])
    

