#!/usr/bin/env python3
import pygame
import time
import random
from player import Player
from obstacle import Obstacle

display_width = 1300  #DISPLAY
display_height = 500  #DIMENSIONS
player_init_position_X = 50
player_init_position_Y = 150
obstacle_init_position_X = 1200
obstacle_init_position_Y = 300
white = (255,255,255)
black = (0,0,0)
playerJumpStrength = 3 # RATE WHICH THE TREX MOVES UP AND DOWN
playerJumpHeight = player_init_position_Y-85 # HEIGHT TO WHICH AGENT IS GOING TO JUMP
movement_change_cycle = 1050000
duck_count_limit = 50

currentY=player_init_position_Y # CURRENT ELEVATION OF PLAYER
playerDirection = 0 # 0 : PLAYER AT GROUND; -1 : PLAYER IS GOING UP; 1 : PLAYER IS GOING DOWN
obstacle_spawn_rate = 160 # OBSTACLE APPEARS AFTER EVERY 160 FRAMES
obstacle_movement_rate = 3.5 # RATE AT WHICH OBSTACLES MOVE TOWARDS THE PLAYER
score = 0 # CURRENT SCORE
reward = 1 # AMOUNT TO BE ADDED TO SCORE
rewardRate = 20 # AFTER 20 FRAMES REWARD IS GOING TO BE ADDED TO SCORE
nCycles = 0 #NUMBER OF CYCLES COMPLETED
spawnCycle = 0
movementRateCycle = 0
obstacles = [] #LIST OF ALL OBSTACLE OF THE SCENE
frameRate = 800 # CLOCK/FRAME RATE
spawnRateLowerBound = 80
spawnRateHigherBound = 150
shouldDuck = False
duckCount = 0
episodes = 0


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text,x,y):
    largeText = pygame.font.Font('freesansbold.ttf',20)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((x),(y))
    gameDisplay.blit(TextSurf, TextRect)


def updateFrame(clock):
    global spawnCycle
    global movementRateCycle
    global nCycles
    movementRateCycle+=1
    pygame.display.update()
    nCycles+=1
    spawnCycle+=1

    clock.tick(frameRate)

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
    cactus = Obstacle(gameDisplay)
    cactus.addToDisplay(obstacle_init_position_X,obstacle_init_position_Y)
    global obstacles
    obstacles.append(cactus)
    global nCycles
    nCycles=0

def moveObstaclesLeft():
    global obstacles
    global obstacle_movement_rate
    if(len(obstacles)==0):
        return
    for cactus in obstacles:
        cactusX = cactus.moveLeftBy(obstacle_movement_rate)
        if(cactusX <= 0):
            obstacles.remove(cactus)
            del cactus

def jumpAction():
    global playerDirection
    global obstacle_movement_rate
    playerDirection = -1*playerJumpStrength

def duckAction():
    global duckCount
    duckCount=1

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

def updateMovementRate():
    global movementRateCycle
    global movement_change_cycle
    global obstacle_movement_rate
    global display_width
    global spawnRateLowerBound
    global spawnRateHigherBound
    if(movementRateCycle%movement_change_cycle == 0 and obstacle_movement_rate < 7.5):
        obstacle_movement_rate += 0.2
        movementRateCycle = 0
        if(spawnRateLowerBound < spawnRateHigherBound-45):
            spawnRateLowerBound += 40

def resetMovementRate():
    global spawnRateLowerBound
    global spawnRateHigherBound
    global obstacle_spawn_rate
    global obstacle_movement_rate
    spawnRateLowerBound = 80
    spawnRateHigherBound = 150
    obstacle_movement_rate = 3.5
    obstacle_spawn_rate = 160

def resetWithMovementRate():
    reset()
    resetMovementRate()

def reset():
    global score
    global currentY
    global playerDirection
    global rewardRate
    global reward
    global nCycles
    global obstacles
    global spawnCycle
    score=0
    currentY = player_init_position_Y
    playerDirection=0
    rewardRate = 20
    reward=1
    nCycles=0
    obstacles=[]
    spawnCycle = 0
    #time.sleep(2)

def init():
    #INITIATION
    global clock
    global gameDisplay
    pygame.init()

    #DISPLAY AND INITIATION
    gameDisplay = pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption("Chrome Dino")
    clock = pygame.time.Clock()

def restart(onFrameUpdate=None,onCollide=None, onCrossedObstacle=None,onExit=None):
    resetWithMovementRate()
    init()
    startEnvironment(onFrameUpdate,onCollide, onCrossedObstacle,onExit)

def restartWithMovementRate(onFrameUpdate=None,onCollide=None, onCrossedObstacle=None,onExit=None):
    reset()
    init()
    startEnvironment(onFrameUpdate,onCollide, onCrossedObstacle,onExit)

def changeEpisode():
    global episodes
    episodes+=1


def startEnvironment(onFrameUpdate=None, onCollide=None, onCrossedObstacle=None,onExit=None):
    global agent
    global crashed
    global currentY
    global playerDirection
    global obstacle_movement_rate
    global spawnCycle
    global obstacle_spawn_rate
    global shouldDuck
    global spawnRateLowerBound
    global spawnRateHigherBound
    global episodes
    global duckCount
    gameDisplay.fill(white)
    agent = Player(gameDisplay)
    agent.setPlayerAt(player_init_position_X,player_init_position_Y,False)

    crashed = False
    x = player_init_position_X
    while not crashed:
        gameDisplay.fill(white)
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                onExit(score)
                crashed=True
            elif (event.type==pygame.KEYDOWN):
                if(event.key == pygame.K_SPACE):
                    jumpAction() # START JUMP ACTION
                elif(event.key == pygame.K_DOWN):
                    duckAction()
                elif(event.key == pygame.K_x):
                    restart(onFrameUpdate,onCollide,onCrossedObstacle,onExit)
                    return


        currentY += playerDirection # CHANGE Y POSITION ACCORDING TO DIRECTION OF JUMP
        agent.setPlayerAt(player_init_position_X,player_init_position_Y+currentY,duckCount != 0)
        if(duckCount%duck_count_limit != 0):
            duckCount+=1
        else:
            duckCount=0
        if(nCycles%rewardRate == 0):
            giveReward() # INCREASE THE SCORE OF THE PLAYER

        updateMovementRate()

        if(spawnCycle%obstacle_spawn_rate == 0):
            addObstacle(gameDisplay,clock) # ADD A NEW OBSTACLE TO THE SCENCE
            obstacle_spawn_rate = random.randint(spawnRateLowerBound,spawnRateHigherBound)
            spawnCycle = 0

        moveObstaclesLeft() # MOVE OBSTACLES TOWARDS LEFT

        if(currentY > player_init_position_Y):
            playerDirection=0
            currentY = player_init_position_Y
        elif currentY <= playerJumpHeight:
            playerDirection=playerJumpStrength

        message_display("Episode : "+str(episodes),70,30)
        message_display("Movement Rate : "+str(obstacle_movement_rate),650,30)
        message_display("Score : "+str(score),1100,30)

        updateFrame(clock) # DRAW ALL THE ELEMENTS OF THE SCENE ON THE SCREEN

        if(collisionDetected()):
            if(onCollide != None):
                nextObstacleInfo = nextObstacleInformation()
                 #CALL THE METHOD FROM TRAIN WHEN COLLISION IS DETECTED
                onCollide(score,
                (currentY != player_init_position_Y),
                duckCount != 0,
                nextObstacleInfo[0],
                nextObstacleInfo[1],
                nextObstacleInfo[2],
                obstacle_movement_rate)
                return
        if(onCrossedObstacle!=None and hasCrossedObstacle()):
            nextObstacleInfo = nextObstacleInformation()
            del obstacles[0]
            onCrossedObstacle(nextObstacleInfo[0],
            nextObstacleInfo[1],
            nextObstacleInfo[2],
            obstacle_movement_rate)

        if(onFrameUpdate != None):
            nextObstacleInfo = nextObstacleInformation()
            onFrameUpdate((currentY != player_init_position_Y),
            duckCount != 0,
            nextObstacleInfo[0],
            nextObstacleInfo[1],
            nextObstacleInfo[2],
            obstacle_movement_rate)
    pygame.quit()
#init()
#startEnvironment()
