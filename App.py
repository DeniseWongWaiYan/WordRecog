from PIL import Image, ImageFilter, ImageEnhance
import tesserpy
import cv2
import sys
reload(sys)
import pickle 
import numpy as np
import MySQLdb

tess = tesserpy.Tesseract("/Users/denisewong/Documents/Dev/WordRecog", language="chi_tra")

#im = Image.open('IMG_1852 copy 2.jpg')
#ImageEnhance.Color(im).enhance(0.0) #black and white
# im_enh = im.filter(ImageFilter.SHARPEN).load().split() #sharpen
im = cv2.imread('IMG_1852 copy 2.jpg', 1)

tess.set_image(im)
tess.get_utf8_text()

f = open('workfile.txt', 'w')

        
yellow_highlights = np.array([])
minR = 123
minG = 129
minB = 134
yellow_min = [(minR, minG, minB)]
#yellow_max = cv2.CV_RGB(maxR, maxG, maxB)

width, height = im.shape[:2]

def detect_highlight():
    for wpixel in range(width):
        for hpixel in range(height):
            if (im[wpixel][hpixel] == yellow_min).all() == True:
                np.append(yellow_highlights, [wpixel, hpixel])

def all_and_sort():
    for word in tess.words():
        word, topleft, topright, bottomleft, bottomright = word.text, word.bounding_box.top, word.bounding_box.left, word.bounding_box.right, word.bounding_box.bottom

        if :
            


    
        

all_words()
detect_highlight()
