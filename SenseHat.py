from sense_hat import SenseHat #import SenseHat from Python Library
from time import sleep
import numpy as np
import time

sense = SenseHat()

y = [255,255,0] #yellow 
x = [0,0,0] #background
b = [0,0,255] #blue
r = [255,0,0] #red

charx = 0 #defines the x value of the character as 0
chary = 0 #defines the y value of he character as 0

# defines each led as x or y. Background acts as sense.clear
background = [
    x,x,x,x,x,x,x,x,
    x,x,x,x,x,x,x,x,
    x,x,x,x,x,x,x,x,
    x,x,x,x,x,x,x,x,
    x,x,x,x,x,x,x,x,
    x,x,x,x,x,x,x,x,
    x,x,x,x,x,x,x,x,
    x,x,x,x,x,x,x,x
    ]

import random #imports random number from python library
apple_xvalue = random.randint(0,7) #generates a random x cordinate for the apple
apple_yvalue = random.randint(0,7) #generates a random y cordinate for the apple

start = time.perf_counter() #defines the variable start as the current time 

while True: #starts a while true loop
    sense.set_pixels(background) #clears all the pixels
    sense.set_pixel(charx, chary, b) #sets the user as a blue pixel at 0,0
    sense.set_pixel(apple_xvalue,apple_yvalue,r) #sets an apple at a random spot

    pitch = sense.get_orientation()['pitch'] #defines pitch
    roll = sense.get_orientation()['roll'] #defines roll

    #print('pitch:', pitch) #prints the pitch
    #print('roll:', roll) #prints the roll
    
    if 270 < pitch < 315 and charx <7: #change x right
        charx += 1
        
    if 45 < pitch < 90 and charx >0: #change x position left
        charx -= 1
        
    if 45 < roll < 90 and chary <7: #change y position down
        chary += 1
        
    if 270 < roll < 315 and chary >0: #change y position up
        chary -= 1
        
    if 200 < pitch < 350 and charx <7 and 15 < roll < 45 and chary <7: #down and right
        charx += 1
        chary += 1
        
    if 15 < pitch < 45 and charx >0 and 300 < roll < 345 and chary >0: #up and left
        charx -= 1
        chary -= 1
        
    if 20 < pitch < 40 and charx >0 and 15 < roll < 45 and chary <7: #down and left
        charx -= 1
        chary += 1
        
    if 200 < pitch < 350 and charx <7 and 300 < roll < 345 and chary >0: #up and right
        charx += 1
        chary -= 1
        
    character = [charx,chary] #defines character as the x and y values of the user
    apple = [apple_xvalue,apple_yvalue] #defines apple as the x and y values of the apple

    if character == apple: #if the user hits the apple make the user grow to 4*4 
        #print("yeah")
        sense.clear() #clear
        if charx > 6 and chary <7: #If the user is in the specifed range draw the 4*4 a specific way so it does not go off the page. right side of the board
            sense.set_pixel(charx,chary,b)
            sense.set_pixel(charx-1,chary+1,b)
            sense.set_pixel(charx-1,chary,b)
            sense.set_pixel(charx,chary+1,b)
            break
        elif charx > 6 and chary >6: #right side of the board
            sense.set_pixel(charx,chary,b)
            sense.set_pixel(charx-1,chary-1,b)
            sense.set_pixel(charx-1,chary,b)
            sense.set_pixel(charx,chary-1,b)
            break
        elif charx <1 and chary <7: #left side of the board
            sense.set_pixel(charx,chary,b)
            sense.set_pixel(charx+1,chary+1,b)
            sense.set_pixel(charx+1,chary,b)
            sense.set_pixel(charx,chary+1,b)
            break
        elif charx <1 and chary >6: #left side of the board
            sense.set_pixel(charx,chary,b)
            sense.set_pixel(charx+1,chary-1,b)
            sense.set_pixel(charx+1,chary,b)
            sense.set_pixel(charx,chary-1,b)
            break
        elif chary <1 and charx <7: #top of the board
            sense.set_pixel(charx,chary,b)
            sense.set_pixel(charx+1,chary+1,b)
            sense.set_pixel(charx+1,chary,b)
            sense.set_pixel(charx,chary+1,b)
            break
        elif chary <1 and charx >6: #top of the board
            sense.set_pixel(charx,chary,b)
            sense.set_pixel(charx-1,chary+1,b)
            sense.set_pixel(charx-1,chary,b)
            sense.set_pixel(charx,chary+1,b)
            break
        elif chary >6 and charx <7: #bottom of the board
            sense.set_pixel(charx,chary,b)
            sense.set_pixel(charx+1,chary-1,b)
            sense.set_pixel(charx+1,chary,b)
            sense.set_pixel(charx,chary-1,b)
            break
        elif chary >6 and charx >6: #bottom of the board
            sense.set_pixel(charx,chary,b)
            sense.set_pixel(charx-1,chary-1,b)
            sense.set_pixel(charx-1,chary,b)
            sense.set_pixel(charx,chary-1,b)
            break
        else:
            sense.set_pixels(background)
            sense.set_pixel(charx,chary,b)
            sense.set_pixel(charx-1,chary+1,b)
            sense.set_pixel(charx-1,chary,b)
            sense.set_pixel(charx,chary+1,b)
            break

sleep(2) #show apple for 2 seconds
end = time.perf_counter() #define end as the current time 
time = end-start #subtract the end time from the start time to find the time passed
print("The time is ", round(time,5)) #print the time and round it to 5 places
sense.set_pixels(background) #clear 
sense.show_message("Next Level", text_colour = r, back_colour = y, scroll_speed = .09) #display Next Level across the screen
sense.set_pixels(background) #clear 

leadx = 0 #defines the lx value of the leading pixel in the new 4*4 user matrix
leady = 0 #defines the lx value of the leading pixel in the new 4*4 user matrix

import random #import a random value
bigapple_xvalue = random.randint(0,5) #generates a random x cordinate for the apple
bigapple_yvalue = random.randint(0,5) #generates a random y cordinate for the apple

def fatty(): #defines the function fatty as a 3*3 matrix
    sense.clear() #clear
    sense.set_pixel(leadx,leady,b) #sets a pixel at the specified coordinates 
    sense.set_pixel(leadx+1,leady,b) #bases the rest of the pixels off the first pixel 
    sense.set_pixel(leadx+2,leady,b)
    sense.set_pixel(leadx,leady+1,b)
    sense.set_pixel(leadx,leady+2,b)
    sense.set_pixel(leadx+1,leady+1,b)
    sense.set_pixel(leadx+1,leady+2,b)
    sense.set_pixel(leadx+2,leady+1,b)
    sense.set_pixel(leadx+2,leady+2,b)
    sleep(2) #show apple for 2 seconds
    sense.set_pixels(background) #clear the background
    sense.show_message("You won", text_colour = r, back_colour = y, scroll_speed = .09) #show the message you won
    sense.set_pixels(background) #clear
    quit()

def kill(): #defines the function kill
    sense.clear() #clear 
    fatty() #calls the fatty function

def bigapple(): #defines the function big apple
    sense.set_pixel(leadx,leady,b) #sets the first pixel in the 4*4 user matrix
    if bigapple_xvalue == leadx and bigapple_yvalue == leady: #the following lines check to see if the user matrix equals the apple to see if they have hit eachother 
        print('good job')
        kill() #if conditon is meet call the kill function
    sense.set_pixel(leadx+1,leady,b)
    if bigapple_xvalue == leadx+1 and bigapple_yvalue == leady:
        print('good job')
        kill()
    sense.set_pixel(leadx,leady+1,b)
    if bigapple_xvalue == leadx and bigapple_yvalue == leady+1:
        print('good job')
        kill()
    sense.set_pixel(leadx+1,leady+1,b)
    if bigapple_xvalue == leadx+1 and bigapple_yvalue == leady+1:
        print('good job')
        kill()
        
while True: #creates another while true loop for the 4*4 matrix
    sense.set_pixel(bigapple_xvalue,bigapple_yvalue,r) #sets an apple at a random spot
    pitch = sense.get_orientation()['pitch']
    roll = sense.get_orientation()['roll']
    #print('pitch:', pitch)
    #print('roll:', roll)

    if 270 < pitch < 315 and leadx <6: #change x right:
        leadx += 1 #changes the leadx value by 1
        #leady += 1
        sense.clear() #clears
        bigapple() #calls big apple
        #sleep(.1)
        #sense.clear()
        
    if 45 < pitch < 90 and leadx >0: #change x position left
        leadx -= 1
        sense.clear()
        bigapple()
        
    if 20 < roll < 30 and leady <6: #change y position down
        leady += 1
        sense.clear()
        bigapple()
        
    if 340 < roll < 350 and leady >0: #change y position up
        leady -= 1
        sense.clear()
        bigapple()
        
    if 200 < pitch < 350 and leadx <6 and 15 < roll < 45 and leady <6: #down and right
        leadx += 1
        leady += 1
        sense.clear()
        bigapple()
        
    if 10 < pitch < 45 and leadx >0 and 300 < roll < 355 and leady >0: #up and left
        leadx -= 1
        leady -= 1
        sense.clear()
        bigapple()
        
    if 20 < pitch < 40 and leadx >0 and 15 < roll < 45 and leady <6: #down and left
        leadx -= 1
        leady += 1
        sense.clear()
        bigapple()
        
    if 300 < pitch < 350 and leadx <6 and 300 < roll < 350 and leady >0: #up and right
        leadx += 1
        leady -= 1
        sense.clear()
        bigapple()

