from gpiozero import MotionSensor
import RPi.GPIO as gpio
import time
import pygame, sys
from pygame.locals import *
x=0
pir = MotionSensor(4)

def init():
    #gpio.setmode(gpio.BOARD)
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
init()

pygame.init()
windowSurfaceObj = pygame.display.set_mode((640,480),1,16)

while True:
    x=0
    for event in pygame.event.get():
     if pir.wait_for_motion():
         print("stop")
    if event.type == KEYDOWN and event.key == K_w:
          forward(0.5)
          print("fd")
          x=1
          
    if event.type == KEYDOWN and event.key == K_s:
          print("bk")
          reverse(0.5)
          x=1
    if event.type == KEYDOWN and event.key == K_d:
          turn_right(0.1)
          print("rt")
          x=1
    if event.type == KEYDOWN and event.key == K_a:
          turn_left(0.1)
          print("lt")
          x=1
    if x==0:
          pass
         
