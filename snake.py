import pygame
import random
mode = 'welcome'
block = 8
width = block
height = block
DIMENTIONS = [2**9, 2**9]
G_O_SCREEN =pygame.image.load('gameover.jpg')
WELCOME_SCREEN =pygame.image.load('welcome.jpg')


def picloc(merge):
    return [random.randint(merge*block, (DIMENTIONS[0] - block - merge*block) / block) * block,
            random.randint(merge*block, (DIMENTIONS[1] - block - merge*block) / block) * block]


pygame.init()

clock = pygame.time.Clock()
clock.tick(60)

win = pygame.display.set_mode((DIMENTIONS[0],DIMENTIONS[1]))
pygame.display.set_caption("My Game")

############################## HERO #######################################
run = True
while run:
    x = picloc(4)[0]
    y = picloc(4)[1]
    vel = 100
    dir = 'down'
    run = True


    if mode == 'game':
        tail = []
        tailLen = 23
        food_loc =picloc(0)

        def eat(food_loc):
            if food_loc[0] == x and food_loc[1] == y:
                return True
        ################################################# death function #####################################################

        def die(tail):
            if x >= DIMENTIONS[0] or x < 0:
                return  True
            if y >= DIMENTIONS[1] or y < 0:
                return True
            for link in tail:
                if x == link[0] and y == link[1]:
                    return True

        ############################## Touch the wall function
        while run:

            pygame.time.delay(vel)
            hero_loc = [x, y]
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
        # ******************* A loop to config controls & actions ****************************

            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT] and got_move == True:
                if dir != 'right':
                    dir = 'left'
                    got_move = False
            if keys[pygame.K_RIGHT] and got_move == True:
                if dir != 'left':
                    dir = 'right'
                    got_move = False
            if keys[pygame.K_UP] and got_move == True:
                if dir != 'down':
                    dir = 'up'
                    got_move = False
            if keys[pygame.K_DOWN] and got_move == True:
                if dir != 'up':
                    dir = 'down'
                    got_move = False
            win.fill((0,0,0,5))
        # ********************* A loop to make snake progress *******************************
            if dir == 'up':
                y -= block
            if dir == 'down':
                y += block
            if dir == 'right':
                x += block
            if dir == 'left':
                x -= block
            got_move = True
        #********************** Now finally draw snakes head **********************************

            pygame.draw.rect(win, (120,120,180),( x , y , width, height))


        # ********************* a method for food, death an all his friends *******************************************
            pygame.draw.rect(win, (180, 120 ,120) , (food_loc[0],food_loc[1], block, block))
            if die(tail):
                #print('Game Over')
                #pygame.quit()
                mode = 'game_over'
                break

            if eat(food_loc):
                tailLen += 12
                food_loc = [random.randint(0, DIMENTIONS[0] / block -1) * block, random.randint(0, DIMENTIONS[1] / block -1) * block]
                vel -= 3
                print((100 -vel)/3)


        #**********************and also a loop for tail ***************************************
            loc = [x,y]
            tail.append(loc)
            #print(tail)
            if len(tail) > tailLen:
                tail.pop(0)
            for link in tail:
                pygame.draw.rect(win, (120,120,180),(link[0], link[1], block, block))

            pygame.display.update()
    if mode == 'welcome':
        while run:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_BACKSPACE]:
                mode = 'game'
                print('executed')
                break

            win.fill((0, 0, 0, 5))
            win.blit(WELCOME_SCREEN, (0, 0))

            pygame.display.update()

    if mode == 'game_over':
        print('game over bitch')
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_BACKSPACE]:
               mode = 'game'
               print('executed')
               break

            win.fill((0,0,0,5))
            win.blit(G_O_SCREEN, (0, 0))

            pygame.display.update()
        #TODO:
         #WRITE A GAME OVER anouncement
         #Create a 'RETRY' button

pygame.quit()


