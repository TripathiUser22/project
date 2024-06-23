import pygame
from sys import exit #this code is used in program to trminate the while loop 
#it is most important to add sound and picture
pygame.init()
#it is use to set the display resolution
screen=pygame.display.set_mode((600,400))
pygame.display.set_caption('RAEBARELI RUNNER')#it is use to give name to our game window
#creating a clock module for framerates
clock=pygame.time.Clock()
test_font=pygame.font.Font('Projects/Graphics/font/Pixeltype.ttf',50)#it is used to add font into a screen first->style,second->size
#creating a surface display 
# sky_surface=pygame.Surface((100,200)) 
# ground_surface=pygame.Surface((100,600))
# test_surface.fill('red')#filling the color on test surface
sky_surface=pygame.image.load('Projects/Graphics/Ground/Sky.png').convert() #it is used to add image to the screen
ground_surface=pygame.image.load('Projects/Graphics/Ground/ground.png').convert()# use to add ground 
test_surface=test_font.render('My Game',False,'Black')
snail_surface=pygame.image.load('Projects/Graphics/Snail/snail1.png').convert_alpha()
player_surface=pygame.image.load('Projects/Graphics/Player/player_walk_1.png')
snail_rect=snail_surface.get_rect(bottomright=(600,300)) 
player_rect=player_surface.get_rect(midbottom=(80,300))
  # snail_x_position=500
# player_x_position=0
#we can also make rectangle for setting a player and ground length




while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()#it is used to exit the current loop
            exit()
    screen.blit(sky_surface,(0,0))#blit is used to palced one surface on other surface
    screen.blit(ground_surface,(0,300))#here order is very important
    screen.blit(test_surface,(200,40))#used to give position of a text
    # snail_x_position-=4#It is used to move snail to left side
    # if snail_x_position<-100:#here we apply snail position so that our snail is repeated 
    #     snail_x_position=800
    screen.blit(snail_surface,snail_rect)#used to give snail position
    snail_rect.x-=4#it is used to give speed
    if snail_rect.left<=0:#giving ending point
        snail_rect.right=800#giving starting point
    # player_x_position+=4
    # if player_x_position>600:
    #     player_x_position=-100
    screen.blit(player_surface,player_rect)
    pygame.display.update()
    clock.tick(60)#this will give you about framerate that your while do not run fast than 60 milisec