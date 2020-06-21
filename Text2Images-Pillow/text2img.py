rom PIL import Image, ImageFont, ImageDraw, ImageFilter
import cv2
#import numpy as np
#import random
import os

font_size= 60
image_size=(3500, 80)
font = 'Siyamrupali.ttf'
font = ImageFont.truetype(font,font_size)

path_lines = './lines_test/'
path_images = './lines_test_images/'
lines = os.listdir(path_lines)

j = 0
for line in lines:
        j+=1
        #print(line)
        #print(j)
        if j%100==0:
                #break
                print(j)
        with open(os.path.join(path_lines, line), 'r',encoding="utf-8") as f:
                doc = f.read()
                image = Image.new('L', image_size, 255)
                draw = ImageDraw.Draw(image)
                string=doc
                draw.text((5,5),string,font=font)
                path_image = os.path.join(path_images,line[:-4])
                image.save(path_image+'.jpg')

