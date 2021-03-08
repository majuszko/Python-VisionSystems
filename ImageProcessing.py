import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from time import perf_counter

def menu():

    choice = input("""
                      1-3: Wybor zadania
                      Esc: Wyjscie

                      """)

    if choice == "1":
        Z1()
    elif choice == "2":
        Z2()
    elif choice == "3":
        Z3()
    else:
        menu()



def empty_callback(value):
    print(f'Trackbar reporting for duty with value: {value}')

def Z1():
    img = cv.imread('lena_salt_and_pepper.bmp')
    cv.namedWindow('image')

    switch_trackbar_name = 'Rozmiar'
    cv.createTrackbar(switch_trackbar_name, 'image', 10, 100, empty_callback)

    blur = cv.blur(img, (5, 5))
    blur_gauss = cv.GaussianBlur(img, (5, 5), 0)
    median = cv.medianBlur(img, 5)
    blur2 = cv.bilateralFilter(img, 9, 75, 75)

    while True:
        key_code = cv.waitKey(10)
        if key_code == 27:
            break

        # cv.imshow('base', img)
        cv.imshow('Blurred', blur)
        cv.imshow('Blurred2', blur_gauss)
        cv.imshow('Blurred3', median)
        # cv.imshow('Blurred4', blur2)

        s = cv.getTrackbarPos(switch_trackbar_name, 'image')

        if s % 2 == 1:
            s2 = s * 10
            img_scaled = cv.resize(blur_gauss, dsize=(s2, s2))
            cv.imshow('image', img_scaled)


        elif s % 2 == 0:
            s1 = s * 10 - 1
            if s1 < 0:
                pass
            else:
                img_scaled1 = cv.resize(blur_gauss, dsize=(s1, s1))
                cv.imshow('image', img_scaled1)

        else:
            pass

    cv.destroyAllWindows()

def Z2():
    img = cv.imread('lena_noise.bmp', 0)
    cv.namedWindow('image')
    switch_trackbar_name = 'Rozmiar'
    cv.createTrackbar(switch_trackbar_name, 'image', 1, 10, empty_callback)
    kernel = np.ones((5, 5), np.uint8)

    opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)
    closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)
    # tophat = cv.morphologyEx(img, cv.MORPH_TOPHAT, kernel)
    # blackhat = cv.morphologyEx(img, cv.MORPH_BLACKHAT, kernel)
    ret, thresh1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)

    gradient = cv.morphologyEx(thresh1, cv.MORPH_GRADIENT, kernel)

    dilation = cv.dilate(thresh1, kernel, iterations=1)

    while True:

        cv.imshow('closing', closing)
        cv.imshow('opening', opening)
        cv.imshow('progowanie', thresh1)
        cv.imshow('dilation', dilation)

        k = cv.waitKey(10)
        if k == 27:
            break

        s = cv.getTrackbarPos(switch_trackbar_name, 'image')

        if s >= 1:
            kernel = np.ones((5, 5), np.uint8)
            erosion = cv.erode(img, kernel, iterations=s)
            cv.imshow('image', erosion)
        else:
            pass

    cv.destroyAllWindows()

def Z3():
    img = cv.imread('uuu.jpg', 0)
    im=cv.imread('uuu.jpg',0)
    imx = cv.imread('uuu.jpg', 0)
    cv.namedWindow('image')
    mean = 0
    print(np.shape(img))
    wys, szer = img.shape
    w,s=im.shape
    imgg=cv.blur(im, (3,3))

    for i in range(wys):
        for j in range(szer):
            if i % 3 == 0:
                if j % 3 == 0:
                    img[i][j] = 255


    for i in range(w-1):
        for j in range(s-1):
            if(i>1 and j>1):
                x=int(im[i][j-1])+int(im[i][j])+int(im[i][j+1])+int(im[i-1][j-1])+int(im[i-1][j])+int(im[i-1][j+1])+int(im[i+1][j-1])+int(im[i+1][j])+int(im[i+1][j+1])

    ob=cv.blur(im, (3,3))

    cv.imshow('im', img)
    cv.imshow('fot',imx)
    cv.imshow('fot2',imgg)
    cv.waitKey()
    cv.destroyAllWindows()

menu()