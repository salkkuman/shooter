import pygame
import Bullet
import math
import Vector

class EnemyUnit():
    
    def __init__(self, x, y, types):
        self.name = "def"
        self.place = Vector.Vector(x, y)
        self.speed = Vector.Vector(0, 0)

        #list of hitboxes items are in form [xcoordinate, ycoordinate]
        self.hitbox = []
        self.hitboxd = 10
        self.timer = 0
        self.timetoshoot = 0
        self.hp = 1
        self.bulletype = 1
        self.type = types
        if(types == 1):
            self.speed.y = 1
            self.hitbox = [0, 40], [0, 40]
            self.sprite = pygame.image.load("../kuvat/enemy.png").convert()
            self.sprite.set_colorkey((255, 0, 255))
            self.timetoshoot = 0
            self.bulletype = 3
        if(types == 2):
            self.hitboxd = 60
            self.speed.y = 0
            self.hitbox = [10, 120], [0, 140]
            self.sprite = pygame.image.load("../kuvat/paivi150.png").convert()
            self.sprite.set_colorkey((255, 0, 255))
            self.timetoshoot = 0
            self.hp = 10
            self.bulletype = 5
        if(types == 7):
            self.hitboxd = 60
            self.speed.y = 0
            self.hitbox = [10, 120], [0, 140]
            self.sprite = pygame.image.load("../kuvat/paivi150.png").convert()
            self.sprite.set_colorkey((255, 0, 255))
            self.timetoshoot = 0
            self.hp = 10
            self.bulletype = 3
        if(types == 3):

            self.speed.__iadd__((0, 1))
            self.hitbox = [0, 50], [0, 50]
            self.sprite = pygame.image.load("../kuvat/pacman_ghost1.png").convert()
            self.sprite.set_colorkey((0, 0, 0))
            self.timetoshoot = 0
            self.hp = 2
            self.bulletype = 4
        if(types == 4):

            self.hitbox = [0, 50], [0, 50]
            self.sprite = pygame.image.load("../kuvat/pacman_ghost2.png").convert()
            self.sprite.set_colorkey((0, 0, 0))
            self.timetoshoot = 0
            self.hp = 2
            self.bulletype = 4
        if(types == 5):

            self.hitbox = [0, 50], [0, 50]
            self.sprite = pygame.image.load("../kuvat/pacman_ghost3.png").convert()
            self.sprite.set_colorkey((0, 0, 0))
            self.timetoshoot = 0
            self.hp = 2
            self.bulletype = 4
        if(types == 6):

            self.hitbox = [0, 50], [0, 50]
            self.sprite = pygame.image.load("../kuvat/pacman_ghost4.png").convert()
            self.sprite.set_colorkey((0, 0, 0))
            self.timetoshoot = 0
            self.hp = 2
            self.bulletype = 4
    def hit(self):
        
        self.hp -= 1
        if (self.hp == 0):
            return 1
        return 0
    def draw(self, screen):
        screen.blit(self.sprite, [int(self.place.x), int(self.place.y)])
    
    def move(self):
        if(self.type == 3 or self.type == 4 or self.type == 5 or self.type == 6):
            datime = 150
            if(self.timer % datime == 0):
                self.speed.y = 0
                self.speed.x = 2
            if(self.timer % datime == int(datime / 4)):
                self.speed.y = 2
                self.speed.x = 0
            if(self.timer % datime == int(datime / 2)):
                self.speed.y = 0
                self.speed.x = -2
            if(self.timer % datime == int(datime * 3 / 4)):
                self.speed.y = 2
                self.speed.x = 0
        
        self.place.x += self.speed.x
        if(self.place.x < 40):
            return 1
           
        if(self.place.x > 720):
            return 1   
            
        self.place.y += self.speed.y
        if(self.place.y < 0):
            return 1
            
        if(self.place.y > 720):
            return 1
        return 0
    
    def time(self):
        self.timer += 1
    
    
            
    def shoot(self, bulletlist, player):
        if(self.type == 7):
            if(self.timer % 20 == 0):
                
                for vector in ringCoord(8):
                    
                    speed1 = vector
                    placeadd = speed1.__mul__(100)
                    place = self.place + placeadd
                    speed = vector
                    speed = Vector.Rotate(speed, 90)
                    speed.__imul__(2.4)
                    #speed = Vector.Vector(3,3)
                    newBullet = Bullet.Bullet(place, speed, self.bulletype)
                    newBullet.setFocus(self.place)
                    bulletlist.append(newBullet)
        
        #hakeutuvia bullettei
        
        if(self.type == 3 or self.type == 4 or self.type == 5 or self.type == 6):
            if(self.timer % 20 == 0):
                speedx1 = player.place.x - self.place.x - 25
                speedy1 = player.place.y - self.place.y - 25
                speedx = 7 * speedx1 / (math.sqrt(speedx1 * speedx1 + speedy1 * speedy1))
                speedy = 7 * speedy1 / (math.sqrt(speedx1 * speedx1 + speedy1 * speedy1))
                speed = Vector.Vector(speedx, speedy)
                place = self.place.__add__((0, 0))
                bulletlist.append(Bullet.Bullet(place, speed, self.bulletype))
        if(self.type == 1 or self.type == 2):
                if(self.timer % 20 == 0):
                    speed = Vector.Vector(2, 5)
                    place = self.place.__add__((0, 0))
                    bulletlist.append(Bullet.Bullet(place, speed, self.bulletype))
                
#yksikkovektoreita count kertaa tasaisesti ympyralle                
def ringCoord(count):
        coordList = []
       
        for i in range(count):
            coordList.append(Vector.AngleVector(i * 360 / count))   
            
        return coordList      
                 
