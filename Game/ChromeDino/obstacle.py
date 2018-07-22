import pygame
import random

class Obstacle:
    images = ["obstacle_large_3","obstacle_large_2","obstacle_small_2","obstacle_small_3","obstacle_small_1"]
    def __init__(self,gameDisplay,clock):
        imgPath =random.choice(images,1)
        self.obstacle = pygame.image.load(imgPath)
        self.gameDisplay = gameDisplay
        self.clock=clock

    def addToDisplay(self,x,y):
        gameDisplay.fill((255,255,255))
        self.gameDisplay.blit(self.obstacle,(x,y))
        pygame.display.update()
