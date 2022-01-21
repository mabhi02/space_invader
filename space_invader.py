###########################
#   AVM's Space Game      #
#                         #
#                         #
#    Description:         #
#   A fun Space Game      #
#                         #
#                         #
###########################

import pygame

HEIGHT = 600
WIDTH = 800
SHIPHEIGHT = 60
SHIPWIDTH = 80



pygame.init()

background = 'img\\plans.jpg'
bg = pygame.image.load(background)
bg = pygame.transform.scale(bg,(WIDTH,HEIGHT))
screen = pygame.display.set_mode((WIDTH,HEIGHT))

defender = 'img\\jet.png'
rocket = pygame.image.load(defender)
rocket = pygame.transform.scale(rocket,(SHIPWIDTH,SHIPHEIGHT))

invader = 'img\\rock.png'
vader = pygame.image.load(invader)
vader = pygame.transform.scale(vader,(SHIPWIDTH,SHIPHEIGHT))

running = True
while running:
    screen.fill((0,0,0))
    screen.blit(bg,(0,0))
    screen.blit(rocket,(0,500))
    screen.blit(vader,(0,0))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()