#!/usr/bin/env python3
import serial
import time
import RPi.GPIO as GPIO

mot_1_1 = 27
mot_1_2 = 17
mot_2_1 = 23
mot_2_2 = 24
pwm_1 = 25


GPIO.setmode(GPIO.BCM)
GPIO.setup([mot_1_1, mot_1_2, mot_2_1, mot_2_2, pwm_1], GPIO.OUT)
p = GPIO.PWM(pwm_1, 500)
p.start(10)


def forward():
    print("going forward")
    GPIO.output(mot_1_1, GPIO.HIGH)
    GPIO.output(mot_1_2, GPIO.LOW)
    GPIO.output(mot_2_1, GPIO.HIGH)
    GPIO.output(mot_2_2, GPIO.LOW)
    return

def rotate1():
    print("rotating 1")
    GPIO.output(mot_1_1, GPIO.HIGH)
    GPIO.output(mot_1_2, GPIO.LOW)
    GPIO.output(mot_2_1, GPIO.LOW)
    GPIO.output(mot_2_2, GPIO.HIGH)

def rotate2():
    print("rotating 1")
    GPIO.output(mot_1_1, GPIO.LOW)
    GPIO.output(mot_1_2, GPIO.HIGH)
    GPIO.output(mot_2_1, GPIO.HIGH)
    GPIO.output(mot_2_2, GPIO.LOW)

def backward():
    print("moving backward")
    GPIO.output(mot_1_1, GPIO.LOW)
    GPIO.output(mot_1_2, GPIO.HIGH)
    GPIO.output(mot_2_1, GPIO.LOW)
    GPIO.output(mot_2_2, GPIO.HIGH)

def stop():
    print("moving backward")
    GPIO.output(mot_1_1, GPIO.LOW)
    GPIO.output(mot_1_2, GPIO.LOW)
    GPIO.output(mot_2_1, GPIO.LOW)
    GPIO.output(mot_2_2, GPIO.LOW)

def set_speed(percent):
    if percent <= 100:
        p.start(percent)
    else:
        raise Exception("Invalid speed")

def cleanup():
    GPIO.cleanup()




