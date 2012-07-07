'''
Created on 2012/07/05

@author: Eero
'''

class EnemyUnit():
    
    def __init__(self,x,y,speedX,speedY, hitbox):
        self.name= "def"
        self.x = 200
        self.y = 200
        self.speedX = 0
        self.speedY = 0
        self.accX = 0
        self.accY = 0
        #list of hitboxes items are in form [xcoordinate, ycoordinate]
        self.hitbox = [hitbox]
        self.time = 0

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
        