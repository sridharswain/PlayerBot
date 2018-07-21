import pygame
import math

class Player:
    def __init__(self,imgPath,gameDisplay):
        self.playerImage = pygame.image.load(imgPath)
        self.gameDisplay = gameDisplay

    def setPlayerAt(self,x,y):
        self.gameDisplay.blit(self.playerImage,(x,y))
        self.x=x
        self.y=y
        pygame.display.update()

    def getPlayer(self):
        return self.playerImage

    def getPlayerPosition(self):
        return (self.x,self.y)

    def jump(self,initialVelocity):
        g=0.1
        velocity = initialVelocity
        #GOING UP
        #setPlayerAt(self.x+50,y)
        while(velocity>0):
            finalVelocity = velocity-0.1
            displacement = math.sqrt((velocity*velocity-finalVelocity*finalVelocity)/2*g)
            self.setPlayerAt(self.x,self.y-displacement)
            velocity=finalVelocity
        while(velocity<initialVelocity):
            finalVelocity = velocity+0.1
            displacement = math.sqrt((finalVelocity*finalVelocity-velocity*velocity)/2*g)
            self.setPlayerAt(self.x,self.y+displacement)
            velocity=finalVelocity
