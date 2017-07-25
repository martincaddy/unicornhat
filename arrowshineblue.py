import unicornhat, signal
from time import sleep
from bluedot import BlueDot
from signal import pause

#function for brightness
bright = unicornhat.brightness

#list for brightness values
shine = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
i = iter

#quick function for show and sleep in other functions
def show():
    unicornhat.show()
    sleep(0.1)

#function for arrow to get brighter
def arrowshine():    
        pixels = [[(0, 0, 0), (0, 0, 0), (0, 0, 0), (255, 0, 255), (255, 0, 255), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (255, 0, 255), (255, 0, 255), (255, 0, 255), (255, 0, 255), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (255, 0, 255), (255, 0, 255), (255, 0, 255), (255, 0, 255), (255, 0, 255), (255, 0, 255), (0, 0, 0)], [(255, 0, 255), (255, 0, 255), (255, 0, 255), (255, 0, 255), (255, 0, 255), (255, 0, 255), (255, 0, 255), (255, 0, 255)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (255, 0, 255), (255, 0, 255), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (255, 0, 255), (255, 0, 255), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (255, 0, 255), (255, 0, 255), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (255, 0, 255), (255, 0, 255), (0, 0, 0), (0, 0, 0), (0, 0, 0)]]
        unicornhat.set_pixels(pixels)
        shine.sort()
        for i in shine:
            bright(i)
            show()
            
#function for arrow to fade values reversed in list            
def arrowfade():    
        pixels = [[(0, 0, 0), (0, 0, 0), (0, 0, 0), (255, 0, 255), (255, 0, 255), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (255, 0, 255), (255, 0, 255), (255, 0, 255), (255, 0, 255), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (255, 0, 255), (255, 0, 255), (255, 0, 255), (255, 0, 255), (255, 0, 255), (255, 0, 255), (0, 0, 0)], [(255, 0, 255), (255, 0, 255), (255, 0, 255), (255, 0, 255), (255, 0, 255), (255, 0, 255), (255, 0, 255), (255, 0, 255)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (255, 0, 255), (255, 0, 255), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (255, 0, 255), (255, 0, 255), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (255, 0, 255), (255, 0, 255), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (255, 0, 255), (255, 0, 255), (0, 0, 0), (0, 0, 0), (0, 0, 0)]]
        unicornhat.set_pixels(pixels)
        shine.reverse()
        for i in shine:
            bright(i)
            show()
            
#function to repeat for different directions of arrow
def fs():
    arrowshine()
    sleep(1)
    arrowfade()
    sleep(1)

# Commented out code to test the different functions
##arrowshine()
##sleep(1)
##shine.reverse()
##arrowfade()
##unicornhat.clear()
##unicornhat.show()



#Main loop once input takens
##while True:
##    unicornhat.clear()
##    unicornhat.show()
##    direction = input ('What direction do you want to go in enter Up, Down, Left or Right: ')
    
def swipe(swiped):   
    if swipe.left:
        unicornhat.rotation(0)
        fs()
                    
    elif swipe.up:
        unicornhat.rotation(90)
        fs()
                    
    elif swipe.right:
        unicornhat.rotation(180)
        fs()
                    
    elif swipe.down:
        unicornhat.rotation(270)
        fs()
        
##    elif direction == "Q":
##        break
    
    
##    unicornhat.clear()
##    unicornhat.show()
##    sleep(1)
##
bd = BlueDot()
bd.when_swiped = swipe
pause()
        