from microbit import *
import random

# We are going to make a simplified version of this game where the pet can either become hungry
# or tired. The user can make the pet happy again by pressing either the A or the B button.


# create variables 

happy = True  # note: capitalize F
hungry = False
sleepy= False
dead = False 
MAX_HEALTH = 100
health = MAX_HEALTH
gameOver = False

# functions

#--------------------------------------------------------------------
def mood():
    # calculate and display pet's mood 
    
    global gameOver
    global happy
    global hungry
    global sleepy
    global dead
    global health
    
    display.clear()
    
    # figure out if the pet is happy, sleepy, or hungry
    if(happy):
        moodChance = random.randint(1, MAX_TIMER)   # picks a random number from 1 - MAX-TIMER
        
        # these if statements will decide if the pet is hungry or sleepy 
        # depending on the random number moodChance
        if(moodChance <= 5):
            happy = False 
            hungry = True
            sleepy = False 
        elif(moodChance > 5 and moodChance <=10):
            happy = False
            hungry = False 
            sleepy = True
       
        
    # display an image to the user depending on how the pet feels 
    
    # if the pet is hungry or sad AND it's unhappy timer reached 0
    # the the pet is dead :(
    if((hungry or sleepy) and (unhappyTimer == 0)):
        display.show(Image.GHOST)
        sleep(2000)
        gameOver= True
        display.scroll("GAME OVER")
     
    # if the pet is happy!   
    if(happy):
        happyChance = random.randint(1, 3) # we will pick a number between 1 -3 
        
        # and show one of these moods based on what we got
        if(happyChance == 1):
            display.show(Image.FABULOUS)
        elif(happyChance == 2):
            display.show(Image.SILLY)
        else:
            display.show(Image.HAPPY)

        sleep(2000)
        
    # if the pet is hungry or sad 
    if(hungry or sleepy):
      
        # display a sad face 
        display.show(Image.SAD)
        sleep(2000)
        
        # decrease the pet's health by 1
        health = health - 1
    display.clear()
    
 #--------------------------------------------------------------------       
def feed():
    # feed the pet if it's hungry, otherwise do nothing
    
    global MAX_HEALTH
    global happy
    global hungry
    global sleepy
    global health
    
    display.clear()
    
    if(hungry):
        happy = True
        hungry = False
        sleepy = False
        
        # update health to be MAX_HEALTH
        health = MAX_HEALTH
        
        # show a heart animation to let to player know
        # that their pet has been fed
        display.show(Image.HEART_SMALL);
        sleep(500)
        display.show(Image.HEART);
        sleep(2000)
        
    display.clear()
   
#-------------------------------------------------------------------- 
def putToBed():
    # put the pet to bed if it's sleepy, otherwise do nothing
    
    global MAX_HEALTH
    global happy
    global hungry
    global sleepy
    global health
    
    display.clear()
    
    if(sleepy):
        happy = True
        hungry = False
        sleepy = False 
        
        # update health to be MAX_HEALTH
        health = MAX_HEALTH
        
        # show a smiling animation
        display.show(Image.SMILE);
        sleep(500)
        display.show(Image.HAPPY);
        sleep(1000)
        
    display.clear()
    
# -------------------------------------------------------------------------------------------
# main loop

# main script. This is like the manager of our program. It will call the correct methods 
# depending on how we interact with the microbit

while not(gameOver):
    
    # show a picture our our pet they can choose any from: 
    # RABBIT, COW, DUCK, TORTOISE, BUTTERFLY, GIRAFFE, SNAKE
    
    display.show(Image.GIRAFFE)
    
    if(accelerometer.was_gesture('shake')):
        mood()
        
    if(button_a.is_pressed()):
        feed()
        
    if(button_b.is_pressed()):
        putToBed()
