import pygame
import Player
import EnemyUnit
import Bullet
import random
import Ammo
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

font = pygame.font.Font(None, 21)

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
bestscore=0
pygame.display.set_caption("Herpderpsburdoborde:DDDDDD:D")
iteration = 0
bulletlist = []
enemylist = []
ammolist = []
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
    
    marginY-=3
    if marginY<=0:
        marginY=40
    
        
    #draw player and move player
    player.move()
    pygame.draw.circle(screen, red, (player.x, player.y), 10, 0)
    #ammo
    
    for ammo in ammolist:
        print(ammo.y)
        if(not ammo.move()):
            pygame.draw.circle(screen, red, (ammo.x, ammo.y), 2, 0)
        else:
            ammolist.remove(ammo)
    
    #add bullets and enemy units
    if(iteration%3==0):
        ammolist.append(Ammo.Ammo(player.x,player.y))
        
    if(iteration%10==0):
        
        enemylist.append(EnemyUnit.EnemyUnit(random.randint(40, 720),0,1))
   
        #bulletlist.append(Bullet.Bullet(40,40,0,5, [[10,20],[10,20]]))
    
    for enemy in enemylist:
        enemy.shoot(bulletlist)
        enemy.time()
        if(player.x>enemy.x+enemy.hitbox[0][0] and player.x<enemy.x+enemy.hitbox[0][1] and player.y>enemy.y+enemy.hitbox[1][0] and player.y<enemy.y+enemy.hitbox[1][1]):
            hit = 1
        
        if (hit==1):    
            bulletlist = []
            enemylist = []
            player.reset()
            iteration = 0
            hit=0
            
    #draw and move enemy unit and bullets
    for enemy in enemylist:
        if(enemy.move()):
            enemylist.remove(enemy)
        else:
            enemy.draw(screen)
    
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
    for bullet in bulletlist:
        if(bullet.move()):
            bulletlist.remove(bullet)
        else:
            bullet.draw(screen)
    #       bulletlist.remove(x)
    
    for enemy in enemylist:
        
        if(player.x>enemy.x+enemy.hitbox[0][0] and player.x<enemy.x+enemy.hitbox[0][1] and player.y>enemy.y+enemy.hitbox[1][0] and player.y<enemy.y+enemy.hitbox[1][1]):
            hit = 1
        
        if (hit==1):    
            bulletlist = []
            enemylist = []
            ammolist = []
            player.reset()
            iteration = 0
            hit=0
            
    #draw and move enemy unit and bullets
    for enemy in enemylist:
        if(enemy.move()):
            enemylist.remove(enemy)
        else:
            enemy.draw(screen)
    # Render the text for score
    
    if(iteration>bestscore):
        bestscore=iteration
    text = font.render('Best Score'+str(bestscore), True, (white), (black))
    
    text1 = font.render('Current Score'+str(iteration), True, (white), (black))
    # Create a rectangle
    textRect = text.get_rect()
    textRect1 = text1.get_rect()
    # Center the rectangle
    textRect.centerx = 900
    textRect.centery = 200
    textRect1.centerx = 900
    textRect1.centery = 180
    # Blit the text
    screen.blit(text, textRect)
    screen.blit(text1, textRect1)


    
    iteration += 1
    pygame.display.flip()    
    clock.tick(60)
pygame.quit()
    
