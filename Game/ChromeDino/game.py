#!/usr/bin/env python3
import pygame
from player import Player
from obstacle import Obstacle

display_width = 1300  #DISPLAY
display_height = 500  #DIMENSIONS
player_init_position_X = 50
player_init_position_Y = 150
obstacle_init_position_X = 1200
obstacle_init_position_Y = 300
white = (255,255,255)
currentY=player_init_position_Y
playerDirection = 0 # 0 : PLAYER AT GROUND; -1 : PLAYER IS GOING UP; 1 : PLAYER IS GOING DOWN
playerJumpHeight = player_init_position_Y-90 # HEIGHT TO WHICH AGENT IS GOING TO JUMP
playerJumpStrength = 4 # RATE WHICH THE TREX MOVES UP AND DOWN
obstacle_spawn_rate = 160 # OBSTACLE APPEARS AFTER EVERY 160 FRAMES
obstacle_movement_rate = 3.5 # RATE AT WHICH OBSTACLES MOVE TOWARDS THE PLAYER
score = 0 # CURRENT SCORE
reward = 1 # AMOUNT TO BE ADDED TO SCORE
rewardRate = 20 # AFTER 20 FRAMES REWARD IS GOING TO BE ADDED TO SCORE
nCycles = 0 #NUMBER OF CYCLES COMPLETED
obstacles = [] #LIST OF ALL OBSTACLE OF THE SCENE




def updateFrame(clock):
    pygame.display.update()
    global nCycles
    nCycles+=1
    clock.tick(80)

def giveReward():
    global score
    score+=reward

def onCollision():
    print("Collided")

def collisionDetected():
    global obstacles
    if(len(obstacles)==0):
        return False
    nearestCactus = obstacles[0]
    return pygame.sprite.collide_rect(agent,nearestCactus)

def addObstacle(gameDisplay,clock):
    cactus = Obstacle(gameDisplay,clock)
    cactus.addToDisplay(obstacle_init_position_X,obstacle_init_position_Y)
    global obstacles
    obstacles.append(cactus)
    global nCycles
    nCycles=0

def moveObstaclesLeft():
    global obstacles
    for cactus in obstacles:
        cactusX = cactus.moveLeftBy(obstacle_movement_rate)
        if(cactusX <= 0):
            obstacles.remove(cactus)
            del cactus

def jump():
    global playerDirection
    playerDirection = -1*playerJumpStrength

def runAtFrame(callback):
    global frameFunc
    frameFunc = callback

def startEnvironment(callback = None):
    #INITIATION
    global agent
    global crashed
    global currentY
    global playerDirection
    pygame.init()

    #DISPLAY AND INITIATION
    gameDisplay = pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption("Chrome Dino")
    clock = pygame.time.Clock()

    gameDisplay.fill(white)
    agent = Player("res/agent.png",gameDisplay,clock)
    agent.setPlayerAt(player_init_position_X,player_init_position_Y)


    crashed = False
    x = player_init_position_X
    while not crashed:
        gameDisplay.fill(white)
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                crashed=True
            elif (event.type==pygame.KEYDOWN and event.key == pygame.K_SPACE):
                jump() # START JUMP ACTION

        currentY +=playerDirection
        agent.setPlayerAt(player_init_position_X,player_init_position_Y+currentY)

        if(nCycles%rewardRate == 0):
            giveReward() # INCREASE THE SCORE OF THE PLAYER

        if(nCycles%obstacle_spawn_rate == 0):
            addObstacle(gameDisplay,clock) # ADD A NEW OBSTACLE TO THE SCENCE

        moveObstaclesLeft() # MOVE OBSTACLES TOWARDS LEFT

        if(currentY >= player_init_position_Y):
            playerDirection=0
            currentY = player_init_position_Y
        elif currentY <= playerJumpHeight:
            playerDirection=playerJumpStrength

        updateFrame(clock) # DRAW ALL THE ELEMENTS OF THE SCENE ON THE SCREEN
        if(collisionDetected()):
            print("d")

    pygame.quit()
    quit()

startEnvironment()
