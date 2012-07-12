import pygame
import Event
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


gameEvent = Event.Event()
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
menudone = True
mainmenu = 0
menuclock = pygame.time.Clock()

menu0 = font.render('Start Game', True, (white), (black))
menu1 = font.render('Extra', True, (white), (black))
menu2 = font.render('Settings', True, (white), (black))
menu3 = font.render('Highscore', True, (white), (black))
menu4 = font.render('Quit', True, (white), (black))   
menuy = 220     

while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    while menudone == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menudone = True
                done = True        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                if mainmenu < 4:
                    mainmenu += 1
                    menuy += 20
            if event.key == pygame.K_UP:
                if mainmenu > 0:
                    mainmenu -= 1
                    menuy -= 20
            if event.key == pygame.K_RETURN:
                if mainmenu == 0:
                    menudone = True
                if mainmenu == 1:
                    print("Extra Mode")
                if mainmenu == 2:
                    print("Settings")
                if mainmenu == 3:
                    print("Highscore");
                if mainmenu == 4:
                    menudone = True
                    done = True 
                    
        screen.fill(black)
        
        pygame.draw.circle(screen, white, (460, menuy), 5, 0)
    # Create a rectangle
        menuRect0 = menu0.get_rect()
        menuRect1 = menu1.get_rect()
        menuRect2 = menu2.get_rect()
        menuRect3 = menu3.get_rect()
        menuRect4 = menu4.get_rect()
    # Center the rectangle
        menuRect4.centerx = 511
        menuRect4.centery = 300
        menuRect3.centerx = 511
        menuRect3.centery = 280
        menuRect2.centerx = 511
        menuRect2.centery = 260
        menuRect1.centerx = 511
        menuRect1.centery = 240
        menuRect0.centerx = 511
        menuRect0.centery = 220
    # Blit the text
        screen.blit(menu0, menuRect0)
        screen.blit(menu1, menuRect1)
        screen.blit(menu2, menuRect2)            
        screen.blit(menu3, menuRect3)
        screen.blit(menu4, menuRect4)
                    
        pygame.display.flip()
        menuclock.tick(10)
    
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
        if event.key == pygame.K_ESCAPE:
            menudone = False
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
    screen.blit(alus, [player.x - 35, player.y - 70])
    pygame.draw.circle(screen, red, (player.x, player.y), 7, 0)

    
    #add bullets and enemy units
    if(iteration % 15 == 0):
        ammolist.append(Ammo.Ammo(player.x, player.y))
    
     #saatana nousee haudasta
    if(gameEvent.event == 1):
        if(iteration == 20):
            gameEvent.trigger = 1
        if(iteration == 20):
            enemylist.append(EnemyUnit.EnemyUnit(300, 0, 2))
    
    #4 pacman ghostia
    if(gameEvent.event == 2):
        if(iteration == 1):
            gameEvent.trigger = 4
        if(iteration == 20):
            enemylist.append(EnemyUnit.EnemyUnit(200, 0, 3))
        
        if(iteration == 60):
            enemylist.append(EnemyUnit.EnemyUnit(200, 0, 4))
        
        if(iteration == 100):
            enemylist.append(EnemyUnit.EnemyUnit(200, 0, 5))
        
        if(iteration == 140):
            enemylist.append(EnemyUnit.EnemyUnit(200, 0, 6))
        
    
  
    #random spawnia 100 mobia
    if(gameEvent.event == 3):
        if(iteration == 0):
            gameEvent.trigger = 100
        if(iteration % 200 == 0):
            enemylist.append(EnemyUnit.EnemyUnit(random.randint(40, 720), 0, 1))
   
        
    
    for enemy in enemylist:
        enemy.shoot(bulletlist, player)
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
            gameEvent.trigger -= 1
    for ammo in ammolist:
        
        if(not ammo.move()):
            pygame.draw.circle(screen, yellow, (ammo.x, ammo.y), 2, 0)
        else:
            ammolist.remove(ammo)
        for enemy in enemylist:
            if(ammo.x > enemy.x + enemy.hitbox[0][0] and ammo.x < enemy.x + enemy.hitbox[0][1] and ammo.y > enemy.y + enemy.hitbox[1][0] and ammo.y < enemy.y + enemy.hitbox[1][1]):
                if(enemy.hit()):
                    enemylist.remove(enemy)
                    gameEvent.trigger -= 1
                score += 100
            else:
                enemy.draw(screen)

    for bullet in bulletlist:
        pygame.draw.line(screen, white, [bullet.x, bullet.y], [bullet.x + bullet.speedX, bullet.y + bullet.speedY])
        if(player.x > bullet.x + bullet.hitbox[0][0] and player.x < bullet.x + bullet.hitbox[0][1] and player.y > bullet.y + bullet.hitbox[1][0] and player.y < bullet.y + bullet.hitbox[1][1]):
            hit = 1
        moved=bullet.move()
        if(moved):
            if(moved==2):
                bullet.shoot(bulletlist, player)
            bulletlist.remove(bullet)
        else:
            bullet.draw(screen)
        if (hit == 1):    
            bulletlist = []
            enemylist = []
            player.reset()
            iteration = 0
            score = 0
            hit = 0
            gameEvent.reset()
    
    
    for enemy in enemylist:
        
        if(player.x > enemy.x + enemy.hitbox[0][0] and player.x < enemy.x + enemy.hitbox[0][1] and player.y > enemy.y + enemy.hitbox[1][0] and player.y < enemy.y + enemy.hitbox[1][1]):
            hit = 1
    #jos osuma restart menu looppiin break ois parempi
    
    
           
    #draw and move enemy unit and bullets
    for enemy in enemylist:
        if(enemy.move()):
            enemylist.remove(enemy)
            gameEvent.trigger -= 1
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
    if(gameEvent.trigger == 0):
        gameEvent.event += 1
        iteration = 0
        gameEvent.trigger = 100
    score += 1
    
      
    
    pygame.display.flip()    
    clock.tick(60)
pygame.quit()