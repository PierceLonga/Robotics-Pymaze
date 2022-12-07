import argparse
import time

import cv2
import numpy as np
import serial

from CountsPerSec import CountsPerSec
from VideoGet import VideoGet
from VideoShow import VideoShow


def putIterationsPerSec(frame, iterations_per_sec):
    """
    Add iterations per second text to lower-left corner of a frame.
    """

    cv2.putText(frame, "{:.0f} iterations/sec".format(iterations_per_sec),
        (50, 600), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255))
    return frame


ser = serial.Serial('/dev/ttyUSB0', 115200)  # open serial port
print(ser.name)        # check which port was really used

# def nothing(x): 
#     pass 

# cv2.namedWindow('Trackbars')
# cv2.moveWindow('Trackbars',1320,0)

# cv2.createTrackbar('hueLower', 'Trackbars',96,179,nothing)
# cv2.createTrackbar('hueUpper', 'Trackbars',120,179,nothing)

# cv2.createTrackbar('hue2Lower', 'Trackbars',50,179,nothing)
# cv2.createTrackbar('hue2Upper', 'Trackbars',0,179,nothing)

# cv2.createTrackbar('satLow', 'Trackbars',157,255,nothing)
# cv2.createTrackbar('satHigh', 'Trackbars',255,255,nothing)
# cv2.createTrackbar('valLow','Trackbars',100,255,nothing)
# cv2.createTrackbar('valHigh','Trackbars',255,255,nothing)


dispW=1000
dispH=800
offset = 1


# flip=2 # need to unflip



#Uncomment These next Two Line for Pi Camera
# camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
# cam= cv2.VideoCapture(camSet)

#Or, if you have a WEB cam, uncomment the next line
#(If it does not work, try setting to '1' instead of '0')
#cam=cv2.VideoCapture(0)

source=0
cam = VideoGet(source).start()
cps = CountsPerSec().start()

# width=cam.get(cv2.CAP_PROP_FRAME_WIDTH)
# height=cam.get(cv2.CAP_PROP_FRAME_HEIGHT)
width = 800
height = 600
oldnum = 0
offset = 2

print('width:',width,'height:',height)
while True:
    if (cv2.waitKey(1) == ord("q")) or cam.stopped:
        cam.stop()
        break
    # ret, frame = cam.read()
    frame = cam.frame
    frame = putIterationsPerSec(frame, cps.countsPerSec())

    # frame = cv2.flip(frame,1)

    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    hueLow=30
    # hueLow=cv2.getTrackbarPos('hueLower', 'Trackbars')
    hueUp = 77
    # hueUp=cv2.getTrackbarPos('hueUpper', 'Trackbars')
    hue2Low = 155
    # hue2Low=cv2.getTrackbarPos('hue2Lower', 'Trackbars')
    hue2Up = 0
    # hue2Up=cv2.getTrackbarPos('hue2Upper', 'Trackbars')
    Ls = 119
    # Ls=cv2.getTrackbarPos('satLow', 'Trackbars')
    Us = 255
    # Us=cv2.getTrackbarPos('satHigh', 'Trackbars')
    Lv = 99
    # Lv=cv2.getTrackbarPos('valLow', 'Trackbars')
    Uv = 171
    # Uv=cv2.getTrackbarPos('valHigh', 'Trackbars')

    l_b=np.array([hueLow,Ls,Lv])
    u_b=np.array([hueUp,Us,Uv])

    l_b2=np.array([hue2Low,Ls,Lv])
    u_b2=np.array([hue2Up,Us,Uv])

    FGmask=cv2.inRange(hsv,l_b,u_b)
    FGmask2=cv2.inRange(hsv,l_b2,u_b2)
    FGmaskComp=cv2.add(FGmask,FGmask2)
    #cv2.imshow('FGmaskComp',FGmaskComp)
    cv2.moveWindow('FGmaskComp',0,200)
    contours, hierarchy=cv2.findContours(FGmaskComp,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    contours=sorted(contours,key=lambda x:cv2.contourArea(x),reverse=True)
    for cnt in contours:
        area=cv2.contourArea(cnt)
        (x,y,w,h)=cv2.boundingRect(cnt)
        if area>=50:
            cv2.drawContours(frame,[cnt],0,(255,0,0),3)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)
            objX=x+w/2
            objY=y+h/2
            nl = '\n'
            inobjX = int(objX)
            sobjX = str(inobjX)
            if inobjX > oldnum + offset or inobjX < oldnum - offset:
            
            
                ser.write(sobjX.encode())
                ser.write(nl.encode())
                print(inobjX)
                oldnum = inobjX            

 


            break        

    cv2.imshow('Video',frame)
    cv2.moveWindow('nanoCam',0,0)
    cps.increment()

    if cv2.waitKey(1)==ord('q'):
        break
cam.stop()
cv2.destroyAllWindows()
