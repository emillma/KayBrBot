# -*- coding: utf-8 -*-
"""
Created on Sun May  3 14:11:40 2020

@author: emilm
"""


import cv2
import mss
import numpy
import pytesseract
import pyautogui
import numpy as np
import webbrowser

# webbrowser.open(''.join(
#     [chr(ord(i)-1) for i in 'iuuqt;00xxx/zpvuvcf/dpn0xbudi@w>eRx5x:XhYdR']))

TYPETIME = 0.1
pytesseract.pytesseract.tesseract_cmd = (
    r'C:\Program Files\Tesseract-OCR\tesseract.exe')
CONFIG = (
    '-c tessedit_char_whitelist="C_ abcdefghijklmnopqrstuvwxyz" --psm 4')
def textwriter(text):
    for c in text:
        yield pyautogui.write(c, interval=0)

with mss.mss() as sct:
    run = False
    # Part of the screen to capture
    monitor = {"top": 450, "left": 450, "width": 1100, "height": 155}


    while "Screen capturing":
        img = numpy.array(sct.grab(monitor))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imshow("OpenCV/Numpy normal", img)
        if cv2.waitKey(100) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break
        if np.abs(img[45,25] - 232) > 20:
            continue

        text = pytesseract.image_to_string(img, config = CONFIG)
        text = text.replace('_', ' ')
        text = text.replace('  ', ' ')
        text = text.replace('   ', ' ')
        text = text.replace('\n', ' ')

        if (text[-17:] == 'Click to activate'
            and np.count_nonzero(np.abs(img - 136) < 10) > 1000):
            if not run:
                print('ready to go')
            run = True
        elif run:
            print(text)
            pyautogui.write(text, interval=TYPETIME)



