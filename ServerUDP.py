#/--------------------------------------------------------------\#
# Created By: Cyken Zeraux, 
# Edited By: 
# Last Updated: April 3, 2014
# 3/3/2014
#\--------------------------------------------------------------/#

import socket, sys
import json
import subprocess as sp
import random
import time

HOST = '127.0.0.1'
PORT = 9058
BUFFER_SIZE = 300

socket.setdefaulttimeout(5)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))

inplace = 0
outplace = 0
while True:
    print 'Listening at', s.getsockname()
    data, address = s.recvfrom(BUFFER_SIZE)
    unJSON = json.loads(data)

    try:
        inplace = unJSON['dat']
    except:
        nuller = None

    if inplace < outplace:
        s.close()

    outplace = inplace
    print inplace

    receiveaxes = unJSON['a']
    receivebuttons = unJSON['b']
    receivehats = unJSON['c']
    
    rnumaxes = len(receiveaxes)
    rnumbut = len(receivebuttons)
    rnumhat = len(receivehats)

    for i in range(rnumaxes):
        print receiveaxes[i]
    for i in range(rnumbut):
        print receivebuttons[i]
    for i in range(rnumhat):
        print receivehats[i]

    sp.call('cls',shell=True)   
