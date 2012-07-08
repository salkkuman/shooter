import pygame

import Player
import EnemyUnit
import random
import Ammo
pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
transparent = (255, 0, 255)
pi = 3.141592653
done = False

size = [1024, 720]
screen = pygame.display.set_mode(size)
screen.set_colorkey(transparent)

font = pygame.font.Font(None, 21)

clock = pygame.time.Clock()
# load images
background_tile = pygame.image.load("tile.png").convert()

player = Player.Player()
alus = pygame.image.load("alus.png").convert()
alus.set_colorkey(transparent)
# This sets the width and height of each grid location in background
marginX = 40
marginY = 40
width = 40
height = 40

while(1):
    hit = 0
    bestscore = 0
    pygame.display.set_caption("Herpderpsburdoborde:DDDDDD:D by Hermanni")
    iteration = 0
    bulletlist = []
    enemylist = []
    ammolist = []
    score = 0
    keystate_left = False
    keystate_right = False
    keystate_up = False
    keystate_down = False
    speedx = 0
    speedy = 0
    mov_speed = 3 #default movement speed
    pelievent = 1
    eventtrigger = 100
    while done == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                player.movespeed(1)
            if event.key == pygame.K_2:
                player.movespeed(2)
            if event.key == pygame.K_3:
                player.movespeed(3)
            if event.key == pygame.K_4:
                player.movespeed(4)
            if event.key == pygame.K_5:
                player.movespeed(5)
            if event.key == pygame.K_6:
                player.movespeed(6)
            if event.key == pygame.K_7:
                player.movespeed(7)
            if event.key == pygame.K_8:
                player.movespeed(8)
            if event.key == pygame.K_9:
                player.movespeed(9)
        #uus inputkoodi alku
        key = pygame.key.get_pressed()
        
        if keystate_left == False:
            if key[pygame.K_LEFT]:
                keystate_left = True
                player.changespeedX(-1)
        if keystate_right == False:
            if key[pygame.K_RIGHT]:
                keystate_right = True
                player.changespeedX(1)
        if keystate_up == False:
            if key[pygame.K_UP]:
                keystate_up = True
                player.changespeedY(-1)
        if keystate_down == False:
            if key[pygame.K_DOWN]:
                keystate_down = True
                player.changespeedY(1)
    
            
            
        if keystate_left == True:
            if key[pygame.K_LEFT] == False:
                keystate_left = False
                if key[pygame.K_RIGHT] == False:
                    player.changespeedX(0)
                else:
                    player.changespeedX(1)
                    
        if keystate_right == True:
            if key[pygame.K_RIGHT] == False:
                keystate_right = False
                if key[pygame.K_LEFT] == False:
                    player.changespeedX(0)
                else:
                    player.changespeedX(-1)
                
        if keystate_up == True:
            if key[pygame.K_UP] == False:
                keystate_up = False         
                if key[pygame.K_DOWN] == False:
                    player.changespeedY(0)
                else:
                    player.changespeedY(1)
                    
                    
        if keystate_down == True:
            if key[pygame.K_DOWN] == False:
                keystate_down = False
                if key[pygame.K_UP] == False:
                    player.changespeedY(0)
                else:
                    player.changespeedY(-1)
                    
        #uus inputcode loppu
        
                   
        screen.fill(black)
        
        pygame.draw.line(screen, transparent, [768, 0], [768, 767], 10) #sivupalkki
        
        
        #backroundArea = screen.subsurface((0,200,0,200))
        #backroundArea.fill(blue)
        #moving background 
        for x in range(17):
            for y in range(19):
                screen.blit(background_tile, [x * width + marginX, (height) * y - marginY])
        
        marginY -= 3
        if marginY <= 0:
            marginY = 40
        
            
        #draw player and move player
        
        player.move()
        screen.blit(alus, [player.x-35, player.y-70])
        pygame.draw.circle(screen, red, (player.x, player.y), 7, 0)
    
        
        #add bullets and enemy units
        if(iteration % 15 == 0):
            ammolist.append(Ammo.Ammo(player.x, player.y))
        
       
        if(pelievent==1):
            if(iteration == 20):
                eventtrigger=1
            if(iteration==20):
                enemylist.append(EnemyUnit.EnemyUnit(300, 0, 2))
        
        if(pelievent==2):
            if(iteration==0):
                eventtrigger=100
            if(iteration%200==0):
                enemylist.append(EnemyUnit.EnemyUnit(random.randint(40, 720), 0, 1))
       
            
        
        for enemy in enemylist:
            enemy.shoot(bulletlist)
            enemy.time()
            if(player.x > enemy.x + enemy.hitbox[0][0] and player.x < enemy.x + enemy.hitbox[0][1] and player.y > enemy.y + enemy.hitbox[1][0] and player.y < enemy.y + enemy.hitbox[1][1]):
                hit = 1
            
            if (hit == 1):    
                bulletlist = []
                enemylist = []
                player.reset()
                iteration = 0
                hit = 0
        #draw and move enemy unit and bullets
            if(enemy.move()):
                enemylist.remove(enemy)
    
        for ammo in ammolist:
            if(not ammo.move()):
                pygame.draw.circle(screen, yellow, (ammo.x, ammo.y), 2, 0)
            else:
                ammolist.remove(ammo)
            for enemy in enemylist:
                if(ammo.x > enemy.x + enemy.hitbox[0][0] and ammo.x < enemy.x + enemy.hitbox[0][1] and ammo.y > enemy.y + enemy.hitbox[1][0] and ammo.y < enemy.y + enemy.hitbox[1][1]):
                    if(enemy.hit()):
                        enemylist.remove(enemy)
                        eventtrigger-=1
                    score += 100
                else:
                    enemy.draw(screen)
        for bullet in bulletlist:
            
            if(player.x > bullet.x + bullet.hitbox[0][0] and player.x < bullet.x + bullet.hitbox[0][1] and player.y > bullet.y + bullet.hitbox[1][0] and player.y < bullet.y + bullet.hitbox[1][1]):
                hit = 1
            
            if (hit == 1):    
                bulletlist = []
                enemylist = []
                player.reset()
                iteration = 0
                score = 0
                hit = 0
            if(bullet.move()):
                bulletlist.remove(bullet)
            else:
                bullet.draw(screen)     
    
        
        for enemy in enemylist:
            
            if(player.x > enemy.x + enemy.hitbox[0][0] and player.x < enemy.x + enemy.hitbox[0][1] and player.y > enemy.y + enemy.hitbox[1][0] and player.y < enemy.y + enemy.hitbox[1][1]):
                hit = 1
        #jos osuma restart menu looppiin break ois parempi
        if (hit == 1):    
                break
        
               
        #draw and move enemy unit and bullets
        for enemy in enemylist:
            if(enemy.move()):
                enemylist.remove(enemy)
                eventtrigger-=1
            else:
                enemy.draw(screen)
        # Render the text for score
        
        if(score > bestscore):
            bestscore = score
        text = font.render('Best Score' + str(bestscore), True, (white), (black))
        
        text1 = font.render('Current Score' + str(score), True, (white), (black))
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
        if(eventtrigger==0):
            pelievent+=1
            iteration=0
        score += 1
        
        pygame.display.flip()    
        clock.tick(60)
    pygame.quit()
    