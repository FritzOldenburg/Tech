# This script is a game that measures reaction time. 3 leds blink and a user inputs the
# corresponding vlaues. There are 3 levels and 1 survival mode that runs through all the levels.
# If the user is fast the large LEDs blink fast, if they are slow but correct the large LEDs blink green.
# if they are wrong, the game ends and Large LEDs blink red. The Piranha gives a light show during the countdown.

# The following print functions display directions on how to play to the user
print('What LED blinked?')
print('The LEDs are labled as 1,2,3 respectivly')
print('All the LEDs will blink for 5 seconds and then turn off for 10')
print('Make sure you click in the workspace!!!!')

import random
import time
import RPi.GPIO as GPIO # brings in a library called RPI.GPIO
from time import sleep # brings in time and sleep
GPIO.setwarnings(False) # written to not give warning when the script is run
GPIO.setmode(GPIO.BCM)

GPIO.setup(16,GPIO.OUT) # small red led
GPIO.setup(20,GPIO.OUT) # small red led
GPIO.setup(26,GPIO.OUT) # small red led
GPIO.setup(17,GPIO.OUT) # blue RGB tricolor
GPIO.setup(27,GPIO.OUT) # green RGB tricolor
GPIO.setup(22,GPIO.OUT) # red RGB tricolor
GPIO.setup(23,GPIO.OUT) # blue piranha
GPIO.setup(24,GPIO.OUT) # red piranha
GPIO.setup(25,GPIO.OUT) # green piranha

L=[16,20,26]
T=[]

def blinky(): # blinky is a function that makes the piranha blink
    GPIO.output((23),False)
    sleep(0.1)
    GPIO.output((23),True)
    sleep(0.1)
    GPIO.output((24),False)
    sleep(0.1)
    GPIO.output((24),True)
    sleep(0.1)
    GPIO.output((25),False)
    sleep(0.1)
    GPIO.output((25),True)
    sleep(0.1)

def setgame(): # setgame is a function that prints ready,set,go inorder with the piranha light show in between
    for x in range(0,2):
        blinky()
    print('Ready')
    for x in range(0,2):
        blinky()
    print('Set')
    for x in range(0,2):
        blinky()
    print('Go')
    for x in range(0,1):
        GPIO.output((16,20,26),True)
        sleep(2)
        GPIO.output((16,20,26),False)
        sleep(1)
        
def fastsetgame(): #fastsetgame is a function that turns on the 3 red LEDs for 5 sec and then off for 2. It is used before the game starts
    for x in range(0,1):
        GPIO.output((16,20,26),True)
        sleep(5)
        GPIO.output((16,20,26),False)
        sleep(2)

def startgamelevel1(): #definies level 1 as the function 'startgamelevel1' 
    for x in range (0,5): #creats a loop of 5. A red LED will blink 5 times.
        fast = time.perf_counter() #defines the current time as 'fast'
        p = random.choice(L) # defines random value in the matrix L as P. Matrix L is defined above.
        GPIO.output(p,True) # turns the choosen LED (P) on for .25 sec
        sleep(0.25)
        GPIO.output(p,False) # turns the choosen LED (P) on off 2 sec
        sleep(2)
        y=0 # defines y as 0
        if p == 26: # if p(the randomly choosen value in the matrix) equals 26 then y equals 1
            y = 1
        if p == 16: # if p(the randomly choosen value in the matrix) equals 16 then y equals 2
            y = 2
        if p == 20: # if p(the randomly choosen value in the matrix) equals 20 then y equals 3
            y = 3
        x=int(input()) # prompts the user for an input
        if x == y: # if the user input equals the choosen LED do print stuff and define 'slow' as the end time
            print('You are smart')
            slow = time.perf_counter()
        else: # if the user input does not equal the choosen LED then the loop is broken
            break
        yourtime = slow-fast # the time is calculated by subtracting the end time from the beginning time. It is then displayed.
        T.append(yourtime)
        print(yourtime)
    if len(T)<5: # T was originally defined as an empty matrix. If the length of T is less than 5 (meaning the user did get 5 time values and got an answer wrong)
        print('You lost. Better luck next time') # print better luck next time
        for x in range(0,5): # blink the RGB tricolor leds twice
            GPIO.output((22), False) #red on
            sleep(.2)
            GPIO.output((22), True) #red off
            sleep(.2)
            GPIO.output((22, 27, 17), True) #turn off
    else: # if T equals 5 then do the following
        avg = sum(T)/len(T) # calculated the average time
        finalavg = avg-2 # subtracts 2 because the LEDs turn off for 2 sec so you cant be faster than 2
        print("The average is ", round(finalavg,5)) # prints a rounded average value
        if finalavg>.3: # if the average is less then .3 the RGB tricolor LEDs blink green
            for x in range(0,5):
                GPIO.output((27), False) #green on
                sleep(.2)
                GPIO.output((27), True) #green off
                sleep(.2)
                GPIO.output((22, 27, 17), True) #turn off
        else: # if the average is less then .3 the RGB tricolor LEDs blink different colors fast
            for x in range(0,5):
                GPIO.output((27), False) #blue on
                sleep(.01)
                GPIO.output((27), True) #blue off
                sleep(.01)
                GPIO.output((27,17), False) # blue and green on
                sleep(.01)
                GPIO.output((27,17), True) # blue and green off
                sleep(.01)
                GPIO.output((27,22), False) # blue and red on
                sleep(.01)
                GPIO.output((27,22), True) # blue and red off
                sleep(.01)
                GPIO.output((17), False) #green on
                sleep(.01)
                GPIO.output((17), True) #green off
                sleep(.01)
                GPIO.output((22), False) #red on
                sleep(.01)
                GPIO.output((22), True) #red off
                sleep(.01)
                GPIO.output((22, 27, 17), True) #turn off

def startgamelevel2(): # level 2 is defined as 'startgamelevel2'. It is twice as long with 10 blinks as level 1 and the LEDs blink for only .15 sec and sleeps for 1 sec
    for x in range (0,10):
        fast = time.perf_counter()
        p = random.choice(L)
        GPIO.output(p,True)
        sleep(0.15) 
        GPIO.output(p,False)
        sleep(1)
        y=0
        if p == 26:
            y = 1
        if p == 16:
            y = 2
        if p == 20:
            y = 3
        x=int(input())
        if x == y:
            print('You are smart')
            slow = time.perf_counter()
        else:
            break
        yourtime = slow-fast
        T.append(yourtime)
        print(yourtime)
    if len(T)<10:
        print('You lost. Better luck next time')
        for x in range(0,5):
            GPIO.output((22), False) #red on
            sleep(.2)
            GPIO.output((22), True) #red off
            sleep(.2)
            GPIO.output((22, 27, 17), True) #turn off
    else:
        avg = sum(T)/len(T)
        finalavg = avg-1
        print("The average is ", round(finalavg,5))
        if finalavg>.3:
            for x in range(0,5):
                GPIO.output((27), False) #green on
                sleep(.2)
                GPIO.output((27), True) #green off
                sleep(.2)
                GPIO.output((22, 27, 17), True) #turn off
        else:
            for x in range(0,5):
                GPIO.output((27), False) #blue on
                sleep(.01)
                GPIO.output((27), True) #blue off
                sleep(.01)
                GPIO.output((27,17), False) # blue and green on
                sleep(.01)
                GPIO.output((27,17), True) # blue and green off
                sleep(.01)
                GPIO.output((27,22), False) # blue and red on
                sleep(.01)
                GPIO.output((27,22), True) # blue and red off
                sleep(.01)
                GPIO.output((17), False) #green on
                sleep(.01)
                GPIO.output((17), True) #green off
                sleep(.01)
                GPIO.output((22), False) #red on
                sleep(.01)
                GPIO.output((22), True) #red off
                sleep(.01)
                GPIO.output((22, 27, 17), True) #turn off

def startgamelevel3(): # level 3 is defined as 'startgamelevel3'. It is 3 times as long with 15 blinks as level 1 and the LEDs blink for only .1 sec and sleep for .3 sec.
    for x in range (0,15):
        fast = time.perf_counter()
        p = random.choice(L)
        GPIO.output(p,True)
        sleep(0.1)
        GPIO.output(p,False)
        sleep(.3)
        y=0
        if p == 26:
            y = 1
        if p == 16:
            y = 2
        if p == 20:
            y = 3
        x=int(input())
        if x == y:
            print('You are smart')
            slow = time.perf_counter()
        else:
            break
        yourtime = slow-fast
        T.append(yourtime)
        print(yourtime)
    if len(T)<15:
        print('You lost. Better luck next time')
        for x in range(0,5):
            GPIO.output((22), False) #red on
            sleep(.2)
            GPIO.output((22), True) #red off
            sleep(.2)
            GPIO.output((22, 27, 17), True) #turn off
    else:
        avg = sum(T)/len(T)
        finalavg = avg-.3
        print("The average is ", round(finalavg,5))
        if finalavg>.3:
            for x in range(0,5):
                GPIO.output((27), False) #green on
                sleep(.2)
                GPIO.output((27), True) #green off
                sleep(.2)
                GPIO.output((22, 27, 17), True) #turn off
        else:
            for x in range(0,5):
                GPIO.output((27), False) #blue on
                sleep(.01)
                GPIO.output((27), True) #blue off
                sleep(.01)
                GPIO.output((27,17), False) # blue and green on
                sleep(.01)
                GPIO.output((27,17), True) # blue and green off
                sleep(.01)
                GPIO.output((27,22), False) # blue and red on
                sleep(.01)
                GPIO.output((27,22), True) # blue and red off
                sleep(.01)
                GPIO.output((17), False) #green on
                sleep(.01)
                GPIO.output((17), True) #green off
                sleep(.01)
                GPIO.output((22), False) #red on
                sleep(.01)
                GPIO.output((22), True) #red off
                sleep(.01)
                GPIO.output((22, 27, 17), True) #turn off

setgame() # initiates the set game function
print('Please choose the level you want to play 1,2,3.')
print('If you want to play survival and progress through the levels select 4.')

# the following code lets the user choose the game mode 
whatmode = input() # prompts for user input
if whatmode == '1': # if user input equals 1 then start both fastgamesetup and gamelevel1
    fastsetgame()
    startgamelevel1()
elif whatmode == '2': # if user input equals 2 then start both fastgamesetup and gamelevel2
    fastsetgame()
    startgamelevel2()
elif whatmode == '3': # if user input equals 3 then start both fastgamesetup and gamelevel3
    fastsetgame()
    startgamelevel3()
elif whatmode == '4': # if user input equals 4 then start both fastgamesetup and gamelevel1
    fastsetgame()
    startgamelevel1()
    if len(T)==5: # if T equlas 5 (The matrix has 5 vales meaning the user answer 5 times) then give the option to move to the next level
        T=[]
        print('You can move on to level 2')
        print('Press 1 to exit')
        print('Press 2 to keep going')
        nextlevel=str(input()) # prompts for input
        if nextlevel == '1': # if input equals 1 then print the following
            print('Please play again soon')
        if nextlevel == '2': # if input equals 2 then print the following
            print('This round is going to be faster and longer')
            print('Get ready')
            fastsetgame()
            startgamelevel2()
            
            if len(T)==10: # if T equlas 10 (The matrix has 10 vales meaning the user answer 10 times) then give the option to move to the next level
                T=[]
                print('You can move on to level 3')
                print('Press 1 to exit')
                print('Press 2 to keep going')
                nextlevel=str(input())
                if nextlevel == '1':
                    print('Please play again soon')
                if nextlevel == '2':
                    print('This round is going to be faster and longer')
                    print('Get ready')
                    fastsetgame()
                    startgamelevel3()
  
                    if len(T)==15: # if T equlas 15 (The matrix has 15 vales meaning the user answer 15 times) then give the option to move to the next level
                        T=[]
                        print('You are a legend')
                


