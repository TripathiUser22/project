import pygame
from sys import exit
pygame.init()
screen=pygame.display.set_mode((600,400))
pygame.display.set_caption('RAEBARELI RUNNER')
clock=pygame.time.Clock()
test_font=pygame.font.Font('Projects/Graphics/font/Pixeltype.ttf',50)
sky_surface=pygame.image.load('Projects/Graphics/Ground/Sky.png').convert() 
ground_surface=pygame.image.load('Projects/Graphics/Ground/ground.png').convert() 
test_surface=test_font.render('My Game',False,'Black')
snail_surface=pygame.image.load('Projects/Graphics/Snail/snail1.png').convert_alpha()
player_surface=pygame.image.load('Projects/Graphics/Player/player_walk_1.png')
snail_rect=snail_surface.get_rect(bottomright=(600,300))
player_rect=player_surface.get_rect(midbottom=(80,300)) 
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(test_surface,(200,40))
    screen.blit(snail_surface,snail_rect)
    snail_rect.x-=4
    if snail_rect.right<=0:
        snail_rect.left=800
    screen.blit(player_surface,player_rect)
    pygame.display.update()
    clock.tick(60)