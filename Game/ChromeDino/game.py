#!/usr/bin/env python3
import pygame
from player import Player
from obstacle import Obstacle

display_width = 1300
display_height = 500
player_init_position_X = 50
player_init_position_Y = 150
obstacle_init_position_X = 1200
white = (255,255,255)
currentY=player_init_position_Y
playerDirection = 0
playerJumpHeight = player_init_position_Y-90
playerJumpStrength = 4
obstacle_spawn_rate = 160
obstacle_movement_rate = 3.5
score = 0
reward = 1
rewardRate = 20
nCycles = 0
obstacles = []

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

def updateFrame():
    pygame.display.update()
    global nCycles
    nCycles+=1
    clock.tick(100)

def giveReward():
    global nCycles
    #nCycles=0
    global score
    score+=reward

def addObstacle():
    cactus = Obstacle(gameDisplay,clock)
    cactus.addToDisplay(obstacle_init_position_X,300)
    global obstacles
    obstacles.append(cactus)
    global nCycles
    nCycles=0

#def resetCycles

def moveObstaclesLeft():
    global obstacles
    for cactus in obstacles:
        cactusX = cactus.moveLeftBy(obstacle_movement_rate)
        if(cactusX <= 0):
            obstacles.remove(cactus)

def jump():
    global playerDirection
    playerDirection = -1*playerJumpStrength


crashed = False
x = player_init_position_X
while not crashed:
    gameDisplay.fill(white)
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            crashed=True
        elif (event.type==pygame.KEYDOWN and event.key == pygame.K_SPACE):
            jump()

    currentY +=playerDirection
    agent.setPlayerAt(player_init_position_X,player_init_position_Y+currentY)

    if(nCycles%rewardRate == 0):
        giveReward()

    if(nCycles%obstacle_spawn_rate == 0):
        print("added")
        addObstacle() #ADD A NEW OBSTACLE TO THE SCENCE

    moveObstaclesLeft() # MOVE OBSTACLES TOWARDS LEFT

    if(currentY>=player_init_position_Y):
        playerDirection=0
        currentY = player_init_position_Y
    elif currentY<=playerJumpHeight:
        playerDirection=playerJumpStrength

    updateFrame() #DRAW ALL THE ELEMENTS OF THE SCENE ON THE SCREEN



pygame.quit()
quit()
