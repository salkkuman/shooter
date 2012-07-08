
import pygame


class Bullet():
    
    def __init__(self, x, y, speedX, speedY, hitbox):
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
    
    
    
    def move(self):
        
        self.x += int(self.speedX)
        if(self.x < 40):
            return 1
           
            
        if(self.x > 720):
            return 1
            
            
            
        self.y += int(self.speedY)
        if(self.y < 0):
            return 1
            
            
        if(self.y > 720):
            return 1
        return 0
    
    def draw(self, screen, angle):
        screen.blit(pygame.transform.rotate(self.sprite, angle), [self.x, self.y])
    

