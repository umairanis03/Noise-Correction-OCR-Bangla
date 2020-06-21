import cv2
import numpy as np
#import random
import os
from pytesseract import image_to_string
import re
import concurrent.futures
import time

path_images ='./lines_test_images/'
path_ocr = './lines_test_output//'
path_noisy_images = './noisy_lines_test_images/'
path_noisy_ocr ='./noisy_lines_test_output/'

def ocr(img_name):
    img_path = os.path.join(path_images,img_name)
    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thresh = 255 - cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    thresh = cv2.GaussianBlur(thresh, (3,3), 0)
    data = image_to_string(thresh, lang='ben', config='--psm 6')
    name = img_name[:-4]+'.txt'
    ## Save tesseract Output
    with open(os.path.join(path_ocr,name), 'w',encoding="utf-8") as f:
       f.write(data)
       
    ## Add Noise
    ## Uncomment this for adding noise to images, and save output
    
    #kernel = np.ones((3, 3), np.uint8)
    #img = cv2.erode(img, kernel, iterations=1)
    #noisy_path = os.path.join(path_noisy_images,img_name)
    #print(noisy_path)
    #cv2.imwrite(noisy_path,img)
    #gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #thresh = 255 - cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    #thresh = cv2.GaussianBlur(thresh, (3,3), 0)
    #data = image_to_string(thresh, lang='ben', config='--psm 6')
    #name = img_name[:-4]+'.txt'
    ## Save Noisy Image
    #cv2.imwrite(os.path.join(path_noisy_images,img_name),img)
    #with open(os.path.join(path_noisy_ocr,name), 'w',encoding="utf-8") as f:
    #   f.write(data)

    return img_name

os.environ['OMP_THREAD_LIMIT'] = '1'
def main():
    path =path_images 
    if os.path.isdir(path) == 1: 
        j = 0
        with concurrent.futures.ProcessPoolExecutor(max_workers=24) as executor:
            image_list = os.listdir(path)
            #image_list = image_list[:100]
            #print(image_list)
            for img_name,out_file in zip(image_list,executor.map(ocr,image_list)):
                #print(img_name + '  processed')
                if(j%1000==0):
                   print(j)
                j+=1

 
if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(end-start)

