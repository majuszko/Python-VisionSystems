import cv2 as cv
import numpy as np

kernel = np.ones((5,5), dtype=np.uint8)
cap = cv.VideoCapture(0)

def ex1():
    global cap, kernel
    def syf():
        pass

    cv.namedWindow('current_frame')
    cv.namedWindow('background')
    cv.namedWindow('foreground')

    cv.createTrackbar('threshold', 'current_frame', 20, 255, syf)



    img_gray = cv.cvtColor(cap.read()[1], cv.COLOR_BGR2GRAY)
    img_current = np.copy(img_gray)
    img_background = np.copy(img_gray)
    img_foreground = np.copy(img_gray)

    backSub = cv. createBackgroundSubtractorMOG2()
    #backSub = cv. createBackgroundSubtractorKNN()




    k = ord(' ')

    while k != ord('q'):
        ret, frame = cap.read()


        img_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        fgMask = backSub.apply(frame)

        #if k == ord('a'):
        #img_background = np.copy(img_gray)
        img_background[img_background<img_current] += 1
        img_background[img_background>img_current] -= 1
        #elif k == ord('x'):
        img_current = np.copy(img_gray)

        img_diff = cv.absdiff(img_background, img_current)
        t = cv.getTrackbarPos('threshold', 'current_frame')
        img_close = cv.morphologyEx(img_diff, cv.MORPH_CLOSE, kernel)
        ret, img_thresh = cv.threshold(img_close, t, 255, cv.THRESH_BINARY)
        #dilation = cv.dilate(img_thresh, kernel, iterations=1)
        #erosion = cv.erode(dilation, kernel, iterations=1)



        cv.imshow('current_frame', img_current)
        cv.imshow('background', img_background)
        cv.imshow('foreground', fgMask)

        k = cv.waitKey(10)



    cap.release()
    cv.destroyAllWindows()

ex1()



