#!/usr/bin/python -u
#Copyright 2017 Michael Kirsch

import time
import os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD) #Use the same layout as the pins
LED=7
FAN=8
RESET=3
POWER=5
CHECK_PCB=10
GPIO.setup(LED, GPIO.OUT) #LED Output
GPIO.setup(POWER, GPIO.IN)  #set pin as input
GPIO.setup(RESET, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(CHECK_PCB, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def led(status):
  if status == 0:
    GPIO.output(LED, GPIO.LOW)
  if status == 1:
    GPIO.output(LED, GPIO.HIGH)

led(1)

while True:
    if GPIO.input(CHECK_PCB)==GPIO.LOW:
        led(1)
        if(GPIO.input(POWER) == GPIO.HIGH):
            led(0)
            os.system("shutdown -h now")
        if(GPIO.input(RESET) == GPIO.LOW):
            led(0)
            os.system("reboot")

