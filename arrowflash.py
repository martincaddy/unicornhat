#!/usr/bin/env python
import unicornhat, signal
from time import sleep

bright = unicornhat.brightness

def arrowflash():
    for i in range(10):
        pixels = [[(0, 0, 0), (0, 0, 0), (0, 0, 0), (255, 0, 255), (255, 0, 255), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (255, 0, 255), (255, 0, 255), (255, 0, 255), (255, 0, 255), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (255, 0, 255), (255, 0, 255), (255, 0, 255), (255, 0, 255), (255, 0, 255), (255, 0, 255), (0, 0, 0)], [(255, 0, 255), (255, 0, 255), (255, 0, 255), (255, 0, 255), (255, 0, 255), (255, 0, 255), (255, 0, 255), (255, 0, 255)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (255, 0, 255), (255, 0, 255), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (255, 0, 255), (255, 0, 255), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (255, 0, 255), (255, 0, 255), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (255, 0, 255), (255, 0, 255), (0, 0, 0), (0, 0, 0), (0, 0, 0)]]
        unicornhat.set_pixels(pixels)
        bright(0.2)
        unicornhat.show()
        sleep(0.2)
        unicornhat.clear()
        unicornhat.show()
        sleep(0.2)
 
while True: 
    direction = input ('What direction do you want to go in enter Up, Down, Left or Right: ')

    if direction == "Left":
        unicornhat.rotation(0)
        arrowflash()
        unicornhat.show()
        sleep(1)
            
    elif direction == "Up":
        unicornhat.rotation(90)
        arrowflash()
        sleep(1)
            
    elif direction == "Right":
        unicornhat.rotation(180)
        arrowflash()
        sleep(1)
            
    elif direction == "Down":
        unicornhat.rotation(270)
        arrowflash()
        sleep(1)
