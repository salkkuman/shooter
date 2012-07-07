import pygame
import Player
import EnemyUnit
import Bullet
import random
pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
transparent = (255, 0, 255)
pi = 3.141592653
done = False

size = [1024, 720]
screen = pygame.display.set_mode(size)
screen.set_colorkey((255,0,255))

clock = pygame.time.Clock()
# load images
background_tile = pygame.image.load("tile.png").convert()

player = Player.Player()

# This sets the width and height of each grid location in backround
marginX=40
marginY=40
width=40
height=40

hit = 0
pygame.display.set_caption("Herpderpsburdoborde:DDDDDD:D")
iteration = 0
bulletlist = []
enemylist = []
while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    # Set the speed based on the key pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changeacc(-0.3,0)
            if event.key == pygame.K_RIGHT:
                player.changeacc(0.3,0)
            if event.key == pygame.K_UP:
                player.changeacc(0,-0.3)
            if event.key == pygame.K_DOWN:
                player.changeacc(0,0.3)
                 
        # Reset speed when key goes up      
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changeacc(0.3,0)
                player.stopX()
                
            if event.key == pygame.K_RIGHT:
                player.changeacc(-0.3,0)
                player.stopX()
                
            if event.key == pygame.K_UP:
                player.changeacc(0,0.3)
                player.stopY()
                
            if event.key == pygame.K_DOWN:
                player.changeacc(0,-0.3)
                player.stopY()
                
    
    screen.fill(black)
    
    pygame.draw.line(screen, transparent, [768, 0], [768, 767], 10) #sivupalkki
    
    
    #backroundArea = screen.subsurface((0,200,0,200))
    #backroundArea.fill(blue)
    #moving backround 
    for x in range(17):
        for y in range(19):
            screen.blit(background_tile, [x*width+marginX,(height)*y-marginY])
    
    marginY-=1
    if marginY==0:
        marginY=40
    
        
    #draw player and move player
    player.move()
    pygame.draw.circle(screen, red, (player.x, player.y), 10, 0)
    
    #add bullets and enemy units
    if(iteration%3==0):
        
        bulletlist.append(Bullet.Bullet(random.randint(40, 720),0,0,5, [[0,40],[0,40]]))
        #bulletlist.append(Bullet.Bullet(40,40,0,5, [[10,20],[10,20]]))
    
    for bullet in bulletlist:
        
        if(player.x>bullet.x+bullet.hitbox[0][0] and player.x<bullet.x+bullet.hitbox[0][1] and player.y>bullet.y+bullet.hitbox[1][0] and player.y<bullet.y+bullet.hitbox[1][1]):
            hit = 1
        
        if (hit==1):    
            bulletlist = []
            enemylist = []
            player.reset()
            iteration = 0
            hit=0
            
    #draw and move enemy unit and bullets
    for x in bulletlist:
        x.move()
        x.draw(screen)
    #       bulletlist.remove(x)
    
    iteration += 1
    pygame.display.flip()    
    clock.tick(60)
pygame.quit()
    
