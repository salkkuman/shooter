import Vector

class Player:
    def __init__(self):
        self.name= "def"
        self.place = Vector.Vector(400,600)
        
        
        self.speedX = 0
        self.speedY = 0
        self.mov_speed = 3
        self.hitboxd=3
        self.hitbox=[[0,0],[3,3]]
    
    
    def reset(self):
        self.place = Vector.Vector(400,600)
        self.speedX = 0
        self.speedY = 0
        self.mov_speed = 3
        
    def movespeed(self,movespeed):
        self.mov_speed = movespeed

    def changeplace(self,x,y):    
        self.x+=x
        self.y+=y
        
    def changespeedX(self,x):    
        self.speedX=x
    def changespeedY(self,y):    
        self.speedY=y
        
        

    
    def move(self):
        x = self.speedX * self.mov_speed
        y = self.speedY * self.mov_speed
        change = Vector.Vector(x,y)
        self.place += change
       
        if(self.place.x<40):
            self.place.x=40
            
        if(self.place.x>720):
            self.place.x=720
            
        
        if(self.place.y<0):
            self.place.y=0
            
        if(self.place.y>720):
            self.place.y=720
           
        
        

    # hp = ""
    #x = 0
    #y = 0
    