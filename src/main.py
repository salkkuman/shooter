import pygame
import Event
import Player
import EnemyUnit
import random
import Ammo
import Vector
import HighScore
import Merge

def collision(item1, item2):
    hitrange = item1.hitboxd + item2.hitboxd
    distance = Vector.Distance(item1.place, item2.place)
    if(distance - hitrange < 0):
        return 1
    for hitbox in item1.hitbox:
        for hitbox in item2.hitbox:
            1 == 1
    return 0

def play_music(music_file):
    clock2 = pygame.time.Clock()
    try:
        pygame.mixer.music.load(music_file)
        print("Music file loaded!")
    except pygame.error:
        print ("File not found!")
        return
    pygame.mixer.music.play(0)
    while pygame.mixer.music.get_busy():
        clock2.tick(30)
    
def save(highscorelist):
    f = open('../config/highscore', 'a')
    
    #Merge.mergesort(highscorelist)
    for score in highscorelist:
        f.write(str(score.score))
        f.write(' ')
        f.write(score.name)
        f.write('\n')

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

music_file = "../bgm/istgp_track01.mp3"
try:
    pygame.mixer.music.load(music_file)
    print("Music file loaded!")
except pygame.error:
    print ("File not found!")
# optional volume 0 to 1.0
pygame.mixer.music.set_volume(0.85)


size = [1024, 720]
screen = pygame.display.set_mode(size)
screen.set_colorkey(transparent)

font = pygame.font.Font(None, 21)

clock = pygame.time.Clock()

# load images
background_tile = pygame.image.load("../kuvat/tile.png").convert()

player = Player.Player()

# This sets the width and height of each grid location in background
marginX = 40
marginY = 40
width = 40
height = 40


gameEvent = Event.Event()
hit = 0
bestscore = 0
pygame.display.set_caption("istg")
iteration = 0
bulletlist = []
enemylist = []
ammolist = []
highscorelist = []
score = 0
keystate_left = False
keystate_right = False
keystate_up = False
keystate_down = False
speedx = 0
speedy = 0
mov_speed = 3 #default movement speed
menudone = False
mainmenu = 0
menu_state = 0 #0 = mainmenu, 1 = character select, 2 = stage select, 3 = extra, 4 = settings, 5 = highscore
menuclock = pygame.time.Clock()
music_playing = 0
character_select = False
character_selected = 0 #0 = punanen hahmo, 1 = sininen, 2 = vihree
menu_button_down = False

menu0 = font.render('Start Game', True, (white), (black))
menu1 = font.render('Extra', True, (white), (black))
menu2 = font.render('Settings', True, (white), (black))
menu3 = font.render('Highscore', True, (white), (black))
menu4 = font.render('Quit', True, (white), (black))   
menuy = 220
hahmomenuy = 233
stagemenuy = 200
stage_selected = 1
substage1 = 1
substage2 = 1
substage3 = 1
substage4 = 1
substage5 = 1

hahmo0 = font.render('Hahmo 1    Power: 1 Speed: 3', True, (white), (black))
hahmo1 = font.render('Hahmo 2    Power: 1 Speed: 6', True, (white), (black))
hahmo2 = font.render('Hahmo 3    Power: 1 Speed: 9', True, (white), (black))

hahmosprite0 = pygame.image.load("../kuvat/temp_hahmo.png").convert()
hahmosprite0.set_colorkey(transparent)
hahmosprite1 = pygame.image.load("../kuvat/temp_hahmo2.png").convert()
hahmosprite1.set_colorkey(transparent)
hahmosprite2 = pygame.image.load("../kuvat/temp_hahmo3.png").convert()
hahmosprite2.set_colorkey(transparent)

while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    while menudone == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menudone = True
                done = True
        if menu_state == 0:
            #pahoittelut, HIRVEETA MENU-KOODIA EDESSA:
            #TODO: fiksumpi menu logiikka, kaikki keyinputtie luku samaa blokkiin koodia
#------------------------MAINMENU-------------------------------------               
            if event.type == pygame.KEYDOWN:
                if menu_button_down == False:
                    if event.key == pygame.K_DOWN:
                        if mainmenu < 4:
                            mainmenu += 1
                            menuy += 20
                            menu_button_down = True
                    if event.key == pygame.K_UP:
                        if mainmenu > 0:
                            mainmenu -= 1
                            menuy -= 20
                            menu_button_down = True
                    if event.key == pygame.K_RETURN:
                        menu_button_down = True
                        if mainmenu == 0:
                            #menudone = True
                            menu_state = 1
                            #characterselectiin
                            #todo: stage select
                        if mainmenu == 1:
                            print("Extra Mode")
                        #todo: toinen peli moodi
                        if mainmenu == 2:
                            print("Settings")
                        #todo: settings valikko
                        if mainmenu == 3:
                            print("Highscore");
                        #todo: highscore list
                        if mainmenu == 4:
                            menudone = True
                            done = True 
                        #quit
            if event.type == pygame.KEYUP:
                menu_button_down = False
            screen.fill(black)
            pygame.draw.circle(screen, white, (460, menuy), 5, 0)
        
        
    # menu valikot. todo: kunnon grafiikat menuun
            menuRect0 = menu0.get_rect()
            menuRect1 = menu1.get_rect()
            menuRect2 = menu2.get_rect()
            menuRect3 = menu3.get_rect()
            menuRect4 = menu4.get_rect()
    # menu tekstien positiot
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
    # piirra menuttekstit ruudulle
            screen.blit(menu0, menuRect0)
            screen.blit(menu1, menuRect1)
            screen.blit(menu2, menuRect2)            
            screen.blit(menu3, menuRect3)
            screen.blit(menu4, menuRect4)
#------------------------//MAINMENU-----------------------------------            
            
#------------------------CHARACTER SELECT-----------------------------
        if menu_state == 1:
            if event.type == pygame.KEYDOWN:
                if menu_button_down == False:
                    if event.key == pygame.K_DOWN:
                        if character_selected < 2:
                            character_selected += 1
                            hahmomenuy += 100
                            menu_button_down = True
                    if event.key == pygame.K_UP:
                        if character_selected > 0:
                            character_selected -= 1
                            hahmomenuy -= 100
                            menu_button_down = True
                    if event.key == pygame.K_RETURN:
                        character_select = True
                        menu_button_down = True
                        menu_state = 2
                        if character_selected == 0:
                            alus = pygame.image.load("../kuvat/temp_hahmo.png").convert()
                            player.movespeed(3)
                        elif character_selected == 1:
                            alus = pygame.image.load("../kuvat/temp_hahmo2.png").convert()
                            player.movespeed(6)
                        elif character_selected == 2:
                            alus = pygame.image.load("../kuvat/temp_hahmo3.png").convert()
                            player.movespeed(9)
                        alus.set_colorkey(transparent)
            if event.type == pygame.KEYUP:
                menu_button_down = False
                    
            screen.fill(black)
            pygame.draw.circle(screen, white, (180, hahmomenuy), 5, 0)
        
    # menu valikot. todo: kunnon grafiikat menuun
    
            screen.blit(hahmosprite0, [200, 200])
            screen.blit(hahmosprite1, [200, 300])
            screen.blit(hahmosprite2, [200, 400])
            
            hahmoRect0 = hahmo0.get_rect()
            hahmoRect1 = hahmo1.get_rect()
            hahmoRect2 = hahmo2.get_rect()
            hahmoRect0.centerx = 400
            hahmoRect0.centery = 230
            hahmoRect1.centerx = 400
            hahmoRect1.centery = 330
            hahmoRect2.centerx = 400
            hahmoRect2.centery = 430
            screen.blit(hahmo0, hahmoRect0)
            screen.blit(hahmo1, hahmoRect1)
            screen.blit(hahmo2, hahmoRect2)
#------------------------//CHARACTER SELECT---------------------------
        
#------------------------STAGE SELECT---------------------------------
        if menu_state == 2:
            if event.type == pygame.KEYDOWN:
                if menu_button_down == False:
                    if event.key == pygame.K_DOWN:
                        if stage_selected < 6:
                            stage_selected += 1
                            stagemenuy += 100
                            menu_button_down = True
                    if event.key == pygame.K_UP:
                        if stage_selected > 0:
                            stage_selected -= 1
                            stagemenuy -= 100
                            menu_button_down = True
                    if event.key == pygame.K_RETURN:
                        menudone = True
                        menu_button_down = True
                        menu_state = 0
            if event.type == pygame.KEYUP:
                menu_button_down = False
            #stageselect piirto
            #TODO: hienompi stage select    
            screen.fill(black)
            pygame.draw.circle(screen, white, (180, stagemenuy), 5, 0)
            
#------------------------//STAGE SELECT-------------------------------
        pygame.display.flip()
        menuclock.tick(60)
    
#-------------------------//MENU--------------------------------------
    
#------------------------MAIN PELI LOOP-------------------------------   
    
    if music_playing == 0:
        pygame.mixer.music.play(-1)
        music_playing = 1
    menu_down_button = False
    # temp: vaihtaa hahmon nopeutta 1-9 
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
            #todo: pausemenu, jossa resume, restart ja quit to main menu. Main menuun menemisen pitaisi resetoida peli myos
            menudone = False
            menu_state = 0
            pygame.mixer.music.stop()
            music_playing = 0
            
    #pelin hahmon inputhandler
    #todo: nappeja skilleille, joissa cooldown
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
    
               
    screen.fill(black)
    #sivupalkki
    #todo: kunnon sivupalkit + grafiikat
    pygame.draw.line(screen, transparent, [768, 0], [768, 767], 10)

    
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
    screen.blit(alus, [player.place.x - 35, player.place.y - 70])
    pygame.draw.circle(screen, red, (int(player.place.x), int(player.place.y)), 7, 0)

    
    #add bullets and enemy units
    if(iteration % 15 == 0):
        ammolist.append(Ammo.Ammo(player.place))
    
    #saatana nousee -- salama: vahemman kryptiset kommentit plz
    if(gameEvent.event == 1):
        if(iteration == 20):
            gameEvent.trigger = 1
        if(iteration == 20):
            enemylist.append(EnemyUnit.EnemyUnit(300, 300, 7))
    
    #saatana nousee haudasta -- salama: vahemman kryptiset kommentit plz
    if(gameEvent.event == 2):
        if(iteration == 20):
            gameEvent.trigger = 1
        if(iteration == 20):
            enemylist.append(EnemyUnit.EnemyUnit(300, 0, 2))
    
    #4 pacman ghostia
    if(gameEvent.event == 3):
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
    if(gameEvent.event == 4):
        if(iteration == 0):
            gameEvent.trigger = 100
        if(iteration % 200 == 0):
            enemylist.append(EnemyUnit.EnemyUnit(random.randint(40, 720), 0, 1))
   
        
    #vihollisten logiikka
    for enemy in enemylist:
        enemy.shoot(bulletlist, player)
        enemy.time()
        if(collision(player, enemy)):
            hit = 1
        
        if (hit == 1):    
            bulletlist = []
            enemylist = []
            player.reset()
            iteration = 0
            hit = 0
            gameEvent.reset()
    #draw and move enemy unit and bullets
        if(enemy.move()):
            enemylist.remove(enemy)
            gameEvent.trigger -= 1
    for ammo in ammolist:
        
        if(not ammo.move()):
            pygame.draw.circle(screen, yellow, (int(ammo.place.x), int(ammo.place.y)), 2, 0)
        else:
            ammolist.remove(ammo)
        for enemy in enemylist:
            if(collision(ammo, enemy)):
                
                if(enemy.hit()):
                    
                    enemylist.remove(enemy)
                    gameEvent.trigger -= 1
                score += 100
            else:
                enemy.draw(screen)
                
    
    for bullet in bulletlist:
        pygame.draw.line(screen, white, [bullet.place.x, bullet.place.y], [bullet.place.x + bullet.speed.x, bullet.place.y + bullet.speed.y])
        if(collision(player, bullet)):
            hit = 1
        moved = bullet.move()
        if(moved):
            if(moved == 2):
                bullet.shoot(bulletlist, player)
            bulletlist.remove(bullet)
        else:
            bullet.draw(screen)
        if (hit == 1):    
            highscorelist.append(HighScore.HighScore(score, player.name))
            bulletlist = []
            enemylist = []
            player.reset()
            iteration = 0
            score = 0
            hit = 0
            gameEvent.reset()
            break
    
    for enemy in enemylist:
        
        if(collision(player, enemy)):
            hit = 1
        if (hit == 1):    
            bulletlist = []
            enemylist = []
            player.reset()
            iteration = 0
            score = 0
            hit = 0
            gameEvent.reset()
            break
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
    fps = int(clock.get_fps())
    text2 = font.render('FPS:' + str(fps), True, (white), (black))
    # sidebar tekstit
    textRect = text.get_rect()
    textRect1 = text1.get_rect()
    textRect2 = text2.get_rect()
    textRect.centerx = 900
    textRect.centery = 200
    textRect1.centerx = 900
    textRect1.centery = 180
    textRect2.centerx = 900
    textRect2.centery = 160
    # Blit the text
    screen.blit(text, textRect)
    screen.blit(text1, textRect1)
    screen.blit(text2, textRect2)
    iteration += 1
    if(gameEvent.trigger == 0):
        gameEvent.event += 1
        iteration = 0
        gameEvent.trigger = 100
    score += 1
    
      
    
    
    pygame.display.flip()    
    clock.tick(60)
save(highscorelist)
pygame.quit()
