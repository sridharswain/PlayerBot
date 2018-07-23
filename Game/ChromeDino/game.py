#!/usr/bin/env python3
import pygame
import time
from player import Player
from obstacle import Obstacle

display_width = 1300  #DISPLAY
display_height = 500  #DIMENSIONS
player_init_position_X = 50
player_init_position_Y = 150
obstacle_init_position_X = 1200
obstacle_init_position_Y = 300
white = (255,255,255)
playerJumpStrength = 3.5 # RATE WHICH THE TREX MOVES UP AND DOWN
playerJumpHeight = player_init_position_Y-110 # HEIGHT TO WHICH AGENT IS GOING TO JUMP

currentY=player_init_position_Y # CURRENT ELEVATION OF PLAYER
playerDirection = 0 # 0 : PLAYER AT GROUND; -1 : PLAYER IS GOING UP; 1 : PLAYER IS GOING DOWN
obstacle_spawn_rate = 160 # OBSTACLE APPEARS AFTER EVERY 160 FRAMES
obstacle_movement_rate = 3.5 # RATE AT WHICH OBSTACLES MOVE TOWARDS THE PLAYER
score = 0 # CURRENT SCORE
reward = 1 # AMOUNT TO BE ADDED TO SCORE
rewardRate = 20 # AFTER 20 FRAMES REWARD IS GOING TO BE ADDED TO SCORE
nCycles = 0 #NUMBER OF CYCLES COMPLETED
obstacles = [] #LIST OF ALL OBSTACLE OF THE SCENE
frameRate = 200 # CLOCK/FRAME RATE




def updateFrame(clock):
    pygame.display.update()
    global nCycles
    nCycles+=1
    clock.tick(frameRate)

def giveReward(scoreUpdated):
    global score
    score+=reward
    if(scoreUpdated!=None):
        scoreUpdated(score)

def onCollision():
    print("Collided")

def collisionDetected():
    global obstacles
    if(len(obstacles)==0):
        return False
    nearestCactus = obstacles[0]
    return pygame.sprite.collide_rect(agent,nearestCactus)

def addObstacle(gameDisplay,clock):
    cactus = Obstacle(gameDisplay)
    cactus.addToDisplay(obstacle_init_position_X,obstacle_init_position_Y)
    global obstacles
    obstacles.append(cactus)
    global nCycles
    nCycles=0

def moveObstaclesLeft():
    global obstacles
    if(len(obstacles)==0):
        return
    for cactus in obstacles:
        cactusX = cactus.moveLeftBy(obstacle_movement_rate)
        if(cactusX <= 0):
            obstacles.remove(cactus)
            del cactus

def jumpAction(onJump):
    global playerDirection
    playerDirection = -1*playerJumpStrength
    if(onJump!=None):
        nextObstacleInfo = nextObstacleInformation()
        onJump(nextObstacleInfo[0],nextObstacleInfo[1],nextObstacleInfo[2],frameRate)

def nextObstacleInformation():
    global obstacles
    if(len(obstacles)==0):
        return (9999,0)
    nextCactusIndex = 0
    agentX = agent.rect.x
    if(obstacles[nextCactusIndex].rect.x<agentX):
        nextCactusIndex+=1
    return (obstacles[nextCactusIndex].rect.x-agentX,obstacles[nextCactusIndex].rect.size[0],obstacles[nextCactusIndex].rect.size[1])

def hasCrossedObstacle():
    global obstacles
    if(len(obstacles)==0):
        return False
    agentX = agent.rect.x-(agent.rect.x/2)
    cactusX = obstacles[0].rect.x+(obstacles[0].rect.x/2)
    return (agentX > cactusX)


def reset():
    global score
    global currentY
    global playerDirection
    global obstacle_spawn_rate
    global obstacle_movement_rate
    global rewardRate
    global reward
    global nCycles
    global obstacles
    global frameRate
    score=0
    currentY = player_init_position_Y
    playerDirection=0
    obstacle_spawn_rate = 160
    obstacle_movement_rate = 3.5
    rewardRate = 20
    reward=1
    nCycles=0
    obstacles=[]
    frameRate=80
    #time.sleep(2)

def init():
    #INITIATION
    reset()
    global clock
    global gameDisplay
    pygame.init()

    #DISPLAY AND INITIATION
    gameDisplay = pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption("Chrome Dino")
    clock = pygame.time.Clock()

def restart(onFrameUpdate=None,onCollide=None, onJump=None, onCrossedObstacle=None,scoreUpdated=None):
    init()
    startEnvironment(onFrameUpdate,onCollide, onJump, onCrossedObstacle)


def startEnvironment(onFrameUpdate=None, onCollide=None, onJump=None, onCrossedObstacle=None,scoreUpdated=None):
    global agent
    global crashed
    global currentY
    global playerDirection
    global obstacle_movement_rate
    gameDisplay.fill(white)
    agent = Player("res/agent.png",gameDisplay)
    agent.setPlayerAt(player_init_position_X,player_init_position_Y)

    crashed = False
    x = player_init_position_X
    while not crashed:
        gameDisplay.fill(white)
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                crashed=True
            elif (event.type==pygame.KEYDOWN):
                if(event.key == pygame.K_SPACE):
                    jumpAction(onJump) # START JUMP ACTION
                elif(event.key == pygame.K_x):
                    restart(onFrameUpdate,onCollide,onJump,onCrossedObstacle,scoreUpdated)
                    return


        currentY +=playerDirection # CHANGE Y POSITION ACCORDING TO DIRECTION OF JUMP
        agent.setPlayerAt(player_init_position_X,player_init_position_Y+currentY)

        if(nCycles%rewardRate == 0):
            giveReward(scoreUpdated) # INCREASE THE SCORE OF THE PLAYER

        if(nCycles%obstacle_spawn_rate == 0):
            addObstacle(gameDisplay,clock) # ADD A NEW OBSTACLE TO THE SCENCE

        moveObstaclesLeft() # MOVE OBSTACLES TOWARDS LEFT

        if(currentY > player_init_position_Y):
            playerDirection=0
            currentY = player_init_position_Y
        elif currentY <= playerJumpHeight:
            playerDirection=playerJumpStrength

        updateFrame(clock) # DRAW ALL THE ELEMENTS OF THE SCENE ON THE SCREEN
        #print(nextObstacleInformation())
        if(collisionDetected()):
            if(onCollide != None):
                onCollide(score) # CALL THE METHOD FROM TRAIN WHEN COLLISION IS DETECTED
                return
        if(onCrossedObstacle!=None and hasCrossedObstacle()):
            nextObstacleInfo = nextObstacleInformation()
            del obstacles[0]
            onCrossedObstacle(nextObstacleInfo[0],nextObstacleInfo[1],nextObstacleInfo[2],frameRate)

        if(onFrameUpdate != None):
            nextObstacleInfo = nextObstacleInformation()
            onFrameUpdate((currentY != player_init_position_Y),nextObstacleInfo[0],nextObstacleInfo[1],nextObstacleInfo[2],frameRate)
    pygame.quit()
#init()
#startEnvironment()
