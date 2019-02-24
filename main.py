# Import the pygame library and initialise the game engine
import pygame
import random

heart = pygame.image.load('1heart.png')
playerOne = pygame.image.load('playerOneWins.png')
playerTwo = pygame.image.load('playerTwoWins.png')

pygame.init()

# Define some colors
BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)

# Open a new window
size = (800, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My First Game")

# The loop will carry on until the user exit the game (e.g. clicks the close button).
carryOn = True
endGame = False
 
# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

bar = [175,175]

acceleration = 3
ball = [400,250]
velocity = [random.choice([-acceleration,acceleration]),random.choice([-acceleration,acceleration])]

life = [3,3]

last_time = 0
current_time = pygame.time.get_ticks()

moveAUp = False
moveADown = False

def displayLife():
    global carryOn
    global life
    global endGame
    if life[0] <= 0:
        screen.fill(BLACK)
        screen.blit(playerTwo,(0,0))
        pygame.display.update()
        carryOn = False
        endGame = True
    elif life[1] <= 0:
        screen.fill(BLACK)
        screen.blit(playerOne,(0,0))
        pygame.display.update()
        carryOn = False
        endGame = True

    for i in range(0, life[0]):
        screen.blit(heart,( 340 - (i*50),450))
    for i in range(0, life[1]):
        screen.blit(heart,( 410 + (i*50),450))


def change_direction(direction):
    global ball
    global velocity
    if direction == 1:
        if ball[0] <= 20 and ball[1] >= bar[0] and ball[1] <= bar[0]+150:
            velocity = [ acceleration, random.choice([-acceleration,acceleration]) ] 
        else:
            life[0] -= 1
            ball = [400,250]
            velocity = [random.choice([-acceleration,acceleration]),random.choice([-acceleration,acceleration])]
    elif direction == 2:
        velocity[1] = acceleration
    elif direction == 3:
        if ball[0] >= 780 and ball[1] >= bar[1] and ball[1] <= bar[1]+150:
            velocity = [ -acceleration, random.choice([-acceleration,acceleration]) ] 
        else:
            life[1] -= 1
            ball = [400,250]
            velocity = [random.choice([-acceleration,acceleration]),random.choice([-acceleration,acceleration])]
    elif direction == 4:
        velocity[1] = -acceleration

def colision_detect():
    if ball[0] <= 10 :
        change_direction(1)
    if ball[0] >= size[0]-10:
        change_direction(3)
    if ball[1] <= 10 :
        change_direction(2) 
    if ball[1] >= size[1]-10:
        change_direction(4)
    return True

def move_ball():
    global last_time
    global current_time
    if (current_time - last_time > 10) and colision_detect():
        ball[0] += velocity[0]
        ball[1] += velocity[1]
        last_time = current_time

# -------- Main Program Loop -----------
while carryOn:

    screen.fill(BLACK)

    # MIDDLE LINE
    pygame.draw.line(screen, WHITE, [400, 0], [400, 500], 3)

    # BAR 1
    bar[0] = ball[1] - 75
    pygame.draw.rect(screen, RED, (0,bar[0],10,150) ,2)
    # print("RED:",bar[0],bar[0] + 150)

    # BAR 2
    pygame.draw.rect(screen, GREEN, (790,bar[1],10,150) ,2)
    #X , Y , LARGURA , ALTURA (descendo) 
    print("GRENN:",bar[1],bar[1] + 150)
    print("BALL:",ball[0],ball[1])

    # BALL
    pygame.draw.circle(screen, WHITE, ball , 10)

    displayLife()

    event = pygame.event.poll()
    if event.type == pygame.QUIT: # If user clicked close
            carryOn = False # Flag that we are done so we exit this loop
    
    current_time = pygame.time.get_ticks()

    pygame.display.update()
    
    move_ball()

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP: 
            moveAUp = True   
        if event.key == pygame.K_DOWN: 
            moveADown = True
    elif event.type == pygame.KEYUP:
        if event.key == pygame.K_UP:
            moveAUp = False 
        if event.key == pygame.K_DOWN:
            moveADown = False

    if moveAUp and bar[1] > 0:
        bar[1] -= 5
    if moveADown and bar[1] < size[1]-150:
        bar[1] += 5

    # print(bar[1])
    clock.tick(60)
    
#Once we have exited the main program loop we can stop the game engine:
while endGame:
    event = pygame.event.poll()
    if event.type == pygame.QUIT: # If user clicked close
        pygame.quit()