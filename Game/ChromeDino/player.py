import pygame
import math

class Player:
    def __init__(self,imgPath,gameDisplay,clock):
        self.playerImage = pygame.image.load(imgPath)
        self.gameDisplay = gameDisplay
        self.clock=clock

    def setPlayerAt(self,x,y):
        self.gameDisplay.fill((255,255,255))
        self.gameDisplay.blit(self.playerImage,(x,y))
        self.x=x
        self.y=y
        #pygame.display.update()
        #self.clock.tick(100)

    def getPlayer(self):
        return self.playerImage

    def getPlayerPosition(self):
        return (self.x,self.y)

    def goUp(self,velocity):
        if(velocity==0):
            return 0
        finalVelocity = velocity-vChange
        displacement = math.sqrt((velocity*velocity-finalVelocity*finalVelocity)/2*g)
        self.setPlayerAt(self.x,self.y-displacement)
        return finalVelocity

    def goDown(self,currentVelocity,groundVelocity):
        if(currentVelocity==groundVelocity):
            return groundVelocity
        finalVelocity = velocity+vChange
        displacement = math.sqrt((finalVelocity*finalVelocity-velocity*velocity)/2*g)
        self.setPlayerAt(self.x,self.y+displacement)
        return finalVelocity

    def jump(self,initialVelocity):
        g=2.45
        vChange = 2
        velocity = initialVelocity
        #GOING UP
        while(velocity>0):

            velocity=finalVelocity
        #GOING DOWN
        while(velocity<initialVelocity):

            velocity=finalVelocity
