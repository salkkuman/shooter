import pygame
import Player
import EnemyUnit
import Bullet

pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
pi = 3.141592653
done = False

size = [1024, 720]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
# load images
background_tile = pygame.image.load("tile.png").convert()

player = Player.Player()

# This sets the width and height of each grid location in backround
marginX=40
marginY=40
width=40
height=40

pygame.display.set_caption("Herpderpsburdoborde:DDDDDD:D")

while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    #moving player
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
    
    pygame.draw.line(screen, white, [768, 0], [768, 767], 10) #sivupalkki
    
    
    #backroundArea = screen.subsurface((0,200,0,200))
    #backroundArea.fill(blue)
    #moving backround 
    for x in range(17):
        for y in range(19):
            screen.blit(background_tile, [x*width+marginX,(height)*y-marginY])
    
    marginY-=1
    if marginY==0:
        marginY=40
        
    #draw player
    player.move()
    pygame.draw.circle(screen, red, (player.x, player.y), 10, 0)
    
    
    pygame.display.flip()    
    clock.tick(60)
pygame.quit()
    
