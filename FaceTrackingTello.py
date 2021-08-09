from utlis import *
import cv2

w,h = 360, 240
pid = [0.5, 0.5, 0]
pError = 0
startCounter = 0

myDrone = initialiazeTello()

while True:


    if startCounter == 0:
        myDrone.takeoff()
        startCounter = 1


    ## step1
    img = telloGetFrame(myDrone,w,h)
    ## step2
    img, info = findFace(img)
    ## step3
    pError = trackFace(myDrone,info,w,pid,pError)

    # print(info[0][0])
    cv2.imshow('Image', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        myDrone.land()
        break




