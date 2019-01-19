from gpiozero import MotionSensor
import RPi.GPIO as gpio
import time
import sys
import pygame
from pygame.locals import *

pir = MotionSensor(4)


def init():
   # gpio.setmode(gpio.BOARD)
    gpio.setup(7, gpio.OUT)
    gpio.setup(11, gpio.OUT)
    gpio.setup(13, gpio.OUT)
    gpio.setup(15, gpio.OUT)

def reverse(tf):
    gpio.output(7, False)
    gpio.output(11, True)
    gpio.output(13, False)
    gpio.output(15, True)
    time.sleep(tf)
    
def forward(tf):
    gpio.output(7, True)
    gpio.output(11, False)
    gpio.output(13, True)
    gpio.output(15, False)
    time.sleep(tf)
    
def turn_right(tf):
    gpio.output(7, True)
    gpio.output(11, False)
    gpio.output(13, False)
    gpio.output(15, True)
    time.sleep(tf)
    
def turn_left(tf):
    gpio.output(7, False)
    gpio.output(11, True)
    gpio.output(13, True)
    gpio.output(15, False)
    time.sleep(tf)

def stop(tf):
    gpio.output(7, False)
    gpio.output(11, False)
    gpio.output(13, False)
    gpio.output(15, False)
    time.sleep(tf)
    #gpio.cleanup()

keys=pygame.key.get_pressed()
if keys[K_w]:
    forward(0.5)
if keys[K_s]
    reverse(0.5)
if keys[K_d]:
    turn_right(0.5)
if keys[K_a]
    turn_left(0.5)
        else:
            pass
