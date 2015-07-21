import pygame
import time
import random

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
yellow = (0,155,0)
green = (0,155,0)

width = 800
height  = 600

gameDisplay = pygame.display.set_mode((width,height))
pygame.display.set_caption("ALOK's SNAKE ")



clock = pygame.time.Clock()

block_size = 10
FPS = 20

font = pygame.font.SysFont(None, 25)

def snake(block_size, snakelist):
    for XnY in snakelist:
        pygame.draw.rect(gameDisplay, green, [XnY[0],XnY[1],block_size,block_size])
    

def message_to_screen(msg,color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [width/2, height/2])
    

def gameloop():
    gameExit = False
    gameOver = False
    
    lead_x = width/2
    lead_y = height/2

    lead_x_change = 0
    lead_y_change = 0

    snakeList = []
    snakeLength = 1

    randAppleX = round(random.randrange(0, width-block_size)/10.0)*10.0
    randAppleY = round(random.randrange(0, height-block_size)/10.0)*10.0
    

    
    while not gameExit:

        while gameOver == True:
            gameDisplay.fill(yellow)
            message_to_screen("suck Alok's Dick . press c to start again or q to exit", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.key == pygame.K_q:
                    gameExit = True
                    gameOver = False
                if event.key == pygame.K_c:
                    gameloop()
                    
            



            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0

        if lead_x >= width or lead_x < 0 or lead_y >= height or lead_y < 0:
            gameOver = True
      

        lead_x += lead_x_change
        lead_y += lead_y_change
        gameDisplay.fill(white)
        AppleThickness = 30
        pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY, AppleThickness, AppleThickness])
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]

        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True
        snake(block_size, snakeList)
        pygame.display.update()

      #  if lead_x == randAppleX and lead_y == randAppleY:
      #      randAppleX = round(random.randrange(0, width-block_size)/10.0)*10.0
      #     randAppleY = round(random.randrange(0,
       #                                         height-block_size)/10.0)*10.0

        if lead_x >= randAppleX and lead_x <= randAppleX + AppleThickness:
                if lead_y >= randAppleY and lead_y <= randAppleY + AppleThickness:
                    randAppleX = round(random.randrange(0, width-block_size)/10.0)*10.0
                    randAppleY = round(random.randrange(0, height-block_size)/10.0)*10.0
                    snakeLength += 1  
               

        clock.tick(FPS)
        
    
    pygame.quit()
    quit()
 
gameloop()
