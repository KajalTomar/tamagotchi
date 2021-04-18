from microbit import *
import random

# ----------------------------------------------------------
# FILE:     tamagotchi.py

# Author:   Kajal Tomar

# REMARKS:  This is a much simplified implementation of a 
#           tamagotchi. The player can shake the micro:bit 
#           to view the pet's mood. If the pet is sad then
#           it is either hungry or sleepy (and it's health 
#           decreases). The player can press button A to try 
#           to feed their pet and button B to put their pet 
#           to bed. This restores the pet's health.
#           If the pet's health drops to 0 then it dies.
# ----------------------------------------------------------

# We are going to make a simplified version of this game where the pet can either become hungry
# or tired. The user can make the pet happy again by pressing either the A or the B button.


# create variables 

happy = True  # note: capitalize F
hungry = False
sleepy= False
dead = False 
MAX_HEALTH = 70    # must a number over 20
health = MAX_HEALTH
gameOver = False

# functions

#--------------------------------------------------------------------
# calculateMood
#
# PURPOSE:  If the pet is happy, pick a number from 1 to MAX_HEALTH.
#           If the number picked is between 1 and 10 then the pet's mood 
#           will change from happy to sad (and the pet will become hungry 
#           or sleepy). Then, it will call the function showMood to 
#           display the mood. 
#--------------------------------------------------------------------
def calculateMood():

    global MAX_HEALTH
    global happy
    global hungry
    global sleepy
    
    if(happy):
        moodChance = random.randint(1, MAX_HEALTH)   # picks a random number from 1 to MAX_HEALTH
        
        # these if statements will decide if the pet is hungry or sleepy 
        # depending on the random number moodChance
        if(moodChance <= 5):
            # the pet is hungry
            happy = False 
            hungry = True
            sleepy = False 
        elif(moodChance > 5 and moodChance <=10):
            # the pet is sleepy 
            happy = False
            hungry = False 
            sleepy = True

    showMood()  

#--------------------------------------------------------------------
# showMood
#
# PURPOSE:  Display an image to the user and
#           update it's health depending on how the pet feels.
#           If the pet is sad (hungry or sleepy) AND it's health is 
#           zero, then display a ghost image and 'game over' and 
#           end the game. 
#--------------------------------------------------------------------
def showMood():      
    
    global gameOver
    global happy
    global hungry
    global sleepy
    global dead
    global health

    display.clear()
   
    # if the pet is hungry or sad AND it's health has reached 0
    # the the pet is dead :(
    if((hungry or sleepy) and (health == 0)):
        display.show(Image.GHOST)   # show ghost image
        sleep(2000)                 
        gameOver = True              # make gameOver = true
        display.scroll("GAME OVER")  # the player must restart their mcro:bit
                                     # to start a new game 
     
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
        
    # if the pet is hungry or sad (note: its health is greater than 0)
    if(hungry or sleepy):
      
        # display a sad face 
        display.show(Image.SAD)
        sleep(2000)
        
        # decrease the pet's health by 1
        health = health - (MAX_HEALTH/10)   # so right now: health = health - (70/10) = health - 7
                                        
        
    display.clear()
    
#--------------------------------------------------------------------
# feed
#
# PURPOSE:  if the pet is hungry then restore it's health and display
#           a heart to let the player know!
#           If the pet is not hungry, then do nothing.
#--------------------------------------------------------------------      
def feed():

    global hungry
    
    if(hungry):    
        restoreHealth() # restore the pet's health
        
        # clear the display and show a growing heart
        # to let the player know that their pet has been fed
        display.clear()
        
        display.show(Image.HEART_SMALL)
        sleep(500)
        display.show(Image.HEART)
        sleep(2000)
        
        display.clear()
        
  
   
#--------------------------------------------------------------------
# putToBed
#
# PURPOSE:  if the pet is sleepy then restore it's health and display
#           a smiley face to let the player know!
#           If the pet is not sleepy, then do nothing.
#--------------------------------------------------------------------  
def putToBed():
   
    global sleepy
    
    if(sleepy):      
        restoreHealth() # restore the pet's health
        
        # clear the display and show a smiley face
        # to let the player know that their pet has gotten enough sleep      
        display.clear()
        
        display.show(Image.SMILE)
        sleep(500)
        display.show(Image.HAPPY)
        sleep(1000)
        
        display.clear()

#--------------------------------------------------------------------
# restoreHealth
#
# PURPOSE:  if the pet is sad (hungry or sleepy) 
#           set happy to true, set both sleepy and hungry to false
#           restore health to the MAX_HEALTH
#-------------------------------------------------------------------- 
def restoreHealth():

    global MAX_HEALTH
    global happy
    global hungry
    global sleepy
    global health

    if(hungry or sleepy):
        
        # set the pet's mood to happy 
        happy = True
        hungry = False
        sleepy = False   
        
        # restore health to MAX_HEALTH
        health = MAX_HEALTH

#--------------------------------------------------------------------
# main loop
#
# PURPOSE:  main script. This is like the manager of our program. 
#           It will call the correct methods depending on how we 
#           interact with the microbit. 
#
#           The player usually sees an image of their pet. 
#           If they shake the pet then they should see an image of
#           the pet's mood. 
#           They can press button A to try to feed their pet
#           and button B to put their pet to bed 
#-------------------------------------------------------------------- 
while not(gameOver):
    # show a picture of the pet, you can choose any from: 
    # RABBIT, COW, DUCK, TORTOISE, BUTTERFLY, GIRAFFE, SNAKE
    
    display.show(Image.GIRAFFE)
    
    if(accelerometer.was_gesture('shake')):
        calculateMood()
        
    if(button_a.is_pressed()):
        feed()
        
    if(button_b.is_pressed()):
        putToBed()


