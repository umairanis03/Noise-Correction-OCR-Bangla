import numpy as np
from PIL import ImageFont, ImageDraw, Image
import cv2
import time
## Make canvas and set the color
img = np.zeros((150,2400,3),np.uint8)
b,g,r,a = 0,255,0,0
## Use bengali font to write bengali.
fontpath = "./Siyamrupali.ttf"
font = ImageFont.truetype(fontpath, 24)
img_pil = Image.fromarray(img)
draw = ImageDraw.Draw(img_pil)
f = open("input.txt", "r")
text=f.read()
f.close()
draw.text((80, 40),text, font = font, fill = (b, g, r, a))
img = np.array(img_pil)
cv2.imwrite("./res2.png", img)
