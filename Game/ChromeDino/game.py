#!/usr/bin/env python3
import pygame
from player import Player

display_width = 1300
display_height = 300
player_init_position_X = 50
player_init_position_Y = 150
white = (255,255,255)
#INITIATION
pygame.init()

#DISPLAY AND INITIATION
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Chrome Dino")
clock = pygame.time.Clock()

gameDisplay.fill(white)

agent = Player("res/agent.png",gameDisplay,clock)
agent.setPlayerAt(player_init_position_X,player_init_position_Y)
#agent.setPlayerAt(player_init_position_X+100,player_init_position_Y)


crashed = False
x = player_init_position_X
while not crashed:
    gameDisplay.fill(white)
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            crashed=True
        elif (event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE):
            if(agent.getPlayerPosition()[1]==player_init_position_Y):
                agent.jump(26)
    agent.setPlayerAt(x,player_init_position_Y)
    pygame.display.update()
    clock.tick(400)
pygame.quit()
quit()
