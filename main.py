#initilaizes all parts of pygame 

import pygame

from sys import exit

def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time 
    score_surf = test_font.render(f'Score: {current_time}',False,(219, 255, 219))
    score_rect = score_surf.get_rect(center = (400,50))
    screen.blit(score_surf,score_rect)



pygame.init()
screen = pygame.display.set_mode((600,400))
pygame.display.set_caption('Snailgame')
clock = pygame.time.Clock()
test_font = pygame.font.Font('Fonts/Pixeltype.ttf', 50)
game_active = False
start_time = 0 


#surfaces
castle_surf = pygame.image.load('graphics/Enviroment/backround.jpg').convert()
ground_surf = pygame.image.load('graphics/Enviroment/marble.jpg').convert()


# score_surf = test_font.render('Xgame', False, (64,64,64) )
# score_rect = score_surf.get_rect(center = (300,50))

snail_surf = pygame.image.load('graphics/Snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(midbottom = (500,300))

player_surf = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))
player_gravity = 0

#intro screen
player_stand = pygame.image.load('graphics/Player/player_stand.png').convert_alpha()
player_stand = pygame.transform.scale(player_stand,(200, 300))
player_stand_rect = player_stand.get_rect(center = (300,200))

while True:
     #--------game-------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #synonimous with the x button of the window
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
                    player_gravity = -20

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True 
                snail_rect.left = 600
                start_time = int(pygame.time.get_ticks() / 1000)
    
    if game_active:
        screen.blit(castle_surf,(0,0))
        screen.blit(ground_surf,(0,300))
        # pygame.draw.rect(screen, '#c0e8ec',score_rect)
        # pygame.draw.rect(screen, '#c0e8ec',score_rect,10)
        # screen.blit(score_surf,score_rect) 
        display_score()   
        snail_rect.x -= 4
        if snail_rect.right <= 0: snail_rect.left = 800 
        screen.blit(snail_surf, snail_rect)

        #player
        player_gravity += 1
        player_rect.y += player_gravity
        # this one line makes the player stand
        if player_rect.bottom >= 300: player_rect.bottom = 300
        screen.blit(player_surf,player_rect)
        
        #collision
        if snail_rect.colliderect(player_rect):
            game_active = False
    #-------------game--------------------------------

    #--------------game over screen---------------
    else:
        screen.fill((94,129,162))
        screen.blit(player_stand,player_stand_rect)

    pygame.display.update()
    clock.tick(60)






