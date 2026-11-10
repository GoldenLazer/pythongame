#initilaizes all parts of pygame 
from sys import exit

import pygame

pygame.init()

#create the display surface named 'screen'
screen = pygame.display.set_mode((600,400))
#displays game name on top window
pygame.display.set_caption('X-Terminator')
clock = pygame.time.Clock()
test_font = pygame.font.Font('Fonts/Pixeltype.ttf', 50)
#surfaces
castle_surf = pygame.image.load('graphics/backround.jpg')
ground_surf = pygame.image.load('graphics/marble.jpg')


score_surf = test_font.render('Xgame', False, (64,64,64) )
score_rect = score_surf.get_rect(center = (300,50))

snail_surface = pygame.image.load('graphics/Snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (500,300))

player_surf = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))
player_gravity = 0

while True:
     
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #synonimous with the x button of the window
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
                player_gravity = -20

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                player_gravity = -20
            
    
    screen.blit(castle_surf,(0,0))
    screen.blit(ground_surf,(0,300))
    pygame.draw.rect(screen, '#c0e8ec',score_rect)
    pygame.draw.rect(screen, '#c0e8ec',score_rect,10)
    screen.blit(score_surf,score_rect)    

    snail_rect.x -= 4
    if snail_rect.right <= 0: snail_rect.left = 800 
    screen.blit(snail_surface, snail_rect)


    #player
    player_gravity += 1
    player_rect.y += player_gravity
    # this one line makes the player stand
    if player_rect.bottom >= 300: player_rect.bottom = 300
    screen.blit(player_surf,player_rect)


    pygame.display.update()
    clock.tick(60)






