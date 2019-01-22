
import pygame
import time
import random
pygame.init()
score = 0
displayWidth = 640
displayHeight = 480
gameDisplay = pygame.display.set_mode((displayWidth , displayHeight))
pygame.display.set_caption("Gotham")


blockSize = 15

white =(255,255,255)
purple=(138,43,226)#it is actually purple
red =(255,0,0)
green=(0,255,0)
black =(192,192,192)
backofBatmobile =(50,50,50)
dark =(12,12,100)
discriptionColor =(0,0,255)
fps=15
level = 1
levelChanger =0
clock = pygame.time.Clock()

font2= pygame.font.SysFont(None,32)

bombThickness = 33
direction = 'right'

batImage = pygame.image.load('car.png')        #you dont have to mention the all path if it is in the same directory as the code.
bombImage =pygame.image.load('thebomb.png')
quoteImage =pygame.image.load('theQuote1.jpg')

infoImage = pygame.image.load('info.png')



def messageOnScreen(msg , color,xcord =displayHeight/3,ycord=displayWidth/3,size=31):
    font = pygame.font.SysFont("comicsansms", size)
    screenText = font.render(msg,True,color)
    gameDisplay.blit(screenText,[xcord,ycord])


def menuScreen():
    intro = True
    while intro:
        gameDisplay.blit(quoteImage,[0,0])
        messageOnScreen("Slither Gotham",purple,100,180,40)
        messageOnScreen("DESCRIPTION : ",red,100,230,20)
        messageOnScreen(" Help The Batman  save Gotham.",discriptionColor, 100,250,15 )
        messageOnScreen(" Ride the Batmobile & collect as many as bombs you can in order to ",discriptionColor,100,270,15)
        messageOnScreen(" save the Gotham City. ", discriptionColor, 100,290,15)
        messageOnScreen("press any key to start or I for info",green,100, 350 , 20)

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key != pygame.K_i:
                time.sleep(1)
                intro = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_i :
                information()
                intro = False

def information ():
    info = True
    while info :
        gameDisplay.blit(infoImage ,[0,0])
        pygame.display.update()
        for event in pygame.event.get():
            if event.type== pygame.KEYDOWN:
                info = False

def scoreDisplay(score):
    scoreText = font2.render("Score : "+str(score),True,black)
    gameDisplay.blit(scoreText,[0,0])
    pygame.display.update()

def levelDisplay(level):

    levelText = font2.render("Level: "+ str(level),True,red)
    gameDisplay.blit(levelText,[displayWidth - 90,00])

    pygame.display.update()

def batMobile ( bombList  ,blockSize,direction):
   if direction == 'right':
        head = pygame.transform.rotate(batImage,270)
   if direction == 'left':
        head = pygame.transform.rotate(batImage,90)
   if direction == 'up':
       head = pygame.transform.rotate(batImage, 0)
   if direction == 'down':
       head = pygame.transform.rotate(batImage, 180)

   gameDisplay.blit(head,(bombList[-1][0],bombList[-1][1]))
   for xny in bombList[:-1]:
       pygame.draw.rect(gameDisplay,backofBatmobile , [xny[0] ,xny[1],blockSize,blockSize])

def gameloop():
    leadX = displayHeight / 2
    leadY = displayWidth / 2
    leadXMove = 10  # this will keep the snake moving in the start
    leadYMove = 0
    score = 0
    gameExit = False
    gameOver = False



    direction = 'right'

    randBombX = round(random.randrange(0, displayWidth - 2 * blockSize) / 10.0) * 10.0
    randBombY = round(random.randrange(0, displayHeight - 2 * blockSize) / 10.0) * 10.0

    bombList = []
    bombSize = 1
    while(not gameExit):
        # gameDisplay.blit(boundry,[0,0])
         while gameOver:

             for event in pygame.event.get():
                 gameDisplay.fill(dark)
                # gameDisplay.blit(boundry, [0, 0])

                 messageOnScreen("press Q to quit and R to restart", green)
                 pygame.display.update()

                 if event.type== pygame.KEYDOWN:
                     if event.key == pygame.K_q:
                         gameExit = True
                         gameOver = False
                         messageOnScreen("GAME OVER",red,displayHeight/4,displayWidth/4,55)
                         pygame.display.update()

                     if event.key == pygame.K_r :
                         gameloop()

                         pygame.display.update()
                 if event.type == pygame.QUIT :
                     gameOver = False
                     gameExit = True

         for  event in pygame.event.get():
            gameDisplay.fill(dark)
            #gameDisplay.blit(boundry, [0, 0])
            print(event)
            if(event.type==pygame.QUIT):
                gameExit= True
                gameOver = False
                intro = False

            if (event.type==pygame.KEYDOWN):
                if(event.key==pygame.K_LEFT):
                    leadXMove = -blockSize
                    leadYMove = 0
                    direction= 'left'

                elif(event.key==pygame.K_RIGHT):               #advantage of using elif over if is that if one of the if's is done the rest won't be bothered
                    leadXMove =blockSize
                    leadYMove =0
                    direction ='right'

                elif(event.key==pygame.K_UP):
                    leadYMove = -blockSize
                    leadXMove =0
                    direction='up'

                elif(event.key==pygame.K_DOWN):
                    leadYMove = blockSize
                    leadXMove =0
                    direction ='down'

         if leadX >displayWidth-10 or leadX<0 or leadY>displayHeight -10or leadY<=0:    #setting of boundries
              gameOver = True

         leadX+= leadXMove
         leadY+= leadYMove
        # pygame.draw.rect(gameDisplay, purple,[randBombX,randBombY,bombThickness,bombThickness])
         gameDisplay.blit(bombImage,(randBombX,randBombY))

         batHead =[]
         batHead.append(leadX)
         batHead.append(leadY)
         bombList.append(batHead)
         if(len(bombList)> bombSize):
             del bombList[0]

         for eachSegment in bombList[:-1]:                                           #self eating
             if(eachSegment==batHead):

                 gameOver = True

         batMobile(bombList ,blockSize,direction)
         pygame.display.flip()
         scoreDisplay(score)
         levelDisplay(level)

         if leadX>=randBombX and leadX <= randBombX +bombThickness :
             if leadY>=randBombY and leadY <= randBombY + bombThickness:
                 randBombX = round(random.randrange(0, displayWidth - 2 * blockSize)/10.0)*10.0
                 randBombY = round(random.randrange(0, displayHeight - 2 * blockSize)/10.0)*10.0
                 score += 1
                 bombSize += 1



         clock.tick(fps)



    print('the score is',score)
    pygame.display.update()
    time.sleep(1)
    pygame.quit()
    quit()

menuScreen()
gameloop()
