#/--------------------------------------------------------------\#
#       ____        ____       ____        _   _      _   
#      |  _ \ _   _|  _ \ ___ | __ )      | \ | | ___| |_ 
#      | |_) | | | | |_) / _ \|  _ \ _____|  \| |/ _ \ __|
#      |  __/| |_| |  _ < (_) | |_) |_____| |\  |  __/ |_ 
#      |_|    \__, |_| \_\___/|____/      |_| \_|\___|\__|
#             |___/                                       
#
# Created By: Cyken Zeraux, 
# Edited By: 
# Last Updated: March 30, 2014
# 3/30/2014
#\--------------------------------------------------------------/#

import socket
import sys
try:
    import pygame
except:
    print 'Cannot locate Pygame.'
    sys.exit(0)
if pygame.version.ver != '1.9.2pre':
    print 'Incorrect version, please get 1.9.2a0.'
    time.sleep(5)
    sys.exit(0)
else:
    print 'hi'

import time
import datetime
import json
import os
import subprocess as sp
import random

HOST = 'localhost'
PORT = 9058
#waitdelay = 0.1 #Initial UDP wait delay

if os.name == 'nt':
    nt = True
else:
    nt = False

def bob():
    global hi
    hi = JSON
    return hi

def NormAxis(value, roundto): # makes sure axi are within range.
    if value > 1:
        value = 1
    elif value < -1:
        value = -1
    else:
        value = fixthrottle(round(value, roundto))
    return value

def fixthrottle(value): #fixes invalid value from throttle.
    if value < 0.007 and value > -0.007:
        value = 0
    else:
        value = value
    return value

def print_row(filename, status, file_type): # prints stuff.
    print " %-45s %5s %15s" % (filename, status, file_type)

#----------------------------------------------------------------------#

pygame.init() #Initializes Pygame. One-call.
pygame.joystick.init() #One-call Joystick Initialize

#Log
try:
    file = open("log.txt", "w") #File to create and use for logging
except:
    print 'Cannot create log file. Read-only? Check your privs?'

#Create Socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except:
    print 'Cannot create socket. Need a driver?'

#Set Socket Options
try:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
except:
    print 'Cannot set socket options. You broke it.'

#Connect with Socket
try:
    s.connect((HOST, PORT))
except:
    print 'Cannot create connection. Modify .py script settings.'


inplace = 0

while True:
#---Reset Variables and Lists-----------------------------------------------------------
    start_time = time.time() #Timing loop

    u = 0
    b = 0
    h = 0

    rawaxes = []
    rawbuttons = []
    rawhats = []
    name = ''
    
    netaxis = []
    netbuttons = []
    nethats = []

    modaxis = []
    modbuttons = []
    modhats = []

#---Initialize Controller----------------------------------------------------------------
    joystick_count = pygame.joystick.get_count()
    for count in range(joystick_count):
        pygame.event.pump() #Forces re-update of Pygame Events (Fixes lack of value update)
        joystick = pygame.joystick.Joystick(count) #Sets variable of joysticks.
        joystick.init() #initializes Controller data capture, also refreshes
#---Polling Info-------------------------------------------------------------------------
        name = joystick.get_name() #Gets hardware name of Joystick
        numaxes = joystick.get_numaxes() #Gets the number of axes on the controller
        numbuttons = joystick.get_numbuttons()
        numhats = joystick.get_numhats()

        for i in range(numaxes):
            modaxis.insert(i, NormAxis(joystick.get_axis(i), 5))
        for i in range(numbuttons):
            modbuttons.insert(i, joystick.get_button(i))
        for i in range(numhats):
            modhats.insert(i, joystick.get_hat(i))

        netaxis = modaxis
        netbuttons = modbuttons
        nethats = modhats
#-------Raw-->Modify-->Net


        data1 = {u'dat': inplace, u'a': netaxis, u'b': netbuttons, u'c': nethats, u'd': (name, numaxes, numbuttons, numhats)}
        JSONdat = json.dumps(data1)
        unJSON = json.loads(JSONdat)
#-----Send-----------#
        s.send(JSONdat)
#---Printer----------------------------------------------------------------------------
        receiveaxes = unJSON['a']
        receivebuttons = unJSON['b']
        receivehats = unJSON['c']
        rnumaxes = len(receiveaxes)
        rnumbut = len(receivebuttons)
        rnumhat = len(receivehats)
        inplace = inplace + 1
        receiveaxes = unJSON["a"]
        receivebuttons = unJSON['b']
        receivehats = unJSON['c']
        rnumaxes = len(receiveaxes)
        rnumbut = len(receivebuttons)
        rnumhat = len(receivehats)
        if __name__ == "__main__":
            sp.call('cls',shell=True)
            for i in range(rnumaxes):
                 print receiveaxes[i]
            for i in range(rnumbut):
                print receivebuttons[i]
            for i in range(rnumhat):
                print receivehats[i]
            print len(JSONdat)
            JSON = {}
        else:
            JSON = data1
#--------------------#





	
	
	
	
	
	
	
	
	
	
	
	
	
	