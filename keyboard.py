import keyboard
import signal
import flicklib
import time
# This code was Made by Aditya Kamath
while True :
        @flicklib.move()
        def move(x, y, z):
                keyboard_matrix=[['a','b','c','d','e','f','g','h','i','j'],['k','l','m','n','o','p','q','r','s','t'],['u','v','w','x','y','z','shift',',','.','space'],['1','2','3','4','5','6','7','8','9','0']]
                x_coord = int(x/.100)
                y_coord = int(y/.250)
                keyboard.press_and_release(keyboard_matrix[x_coord][y_coord])
                time.sleep(1)
