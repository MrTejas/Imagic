from PIL import Image
from IPython.display import display
from random import random
import math


# program to sketch effect on an image

filename = "landscape.jpg"
image = Image.open(filename)
[width,height] = image.size 
new_image = Image.new( 'RGB', (width,height), "black") 

pixels_old = image.load()
pixels_new = new_image.load() # creates the pixel map

sensitivity = -15

for i in range(0,new_image.size[0],2):    
    for j in range(0,new_image.size[1],2):  
        r1 = pixels_old[i,j][0]
        g1 = pixels_old[i,j][1]
        b1 = pixels_old[i,j][2]
        val1 = (int)(math.sqrt(r1*r1 + g1*g1 + b1*b1))

        r2 = pixels_old[i+1,j][0]
        g2 = pixels_old[i+1,j][1]
        b2 = pixels_old[i+1,j][2]
        val2 = (int)(math.sqrt(r2*r2 + g2*g2 + b2*b2))

        r3 = pixels_old[i,j+1][0]
        g3 = pixels_old[i,j+1][1]
        b3 = pixels_old[i,j+1][2]
        val3 = (int)(math.sqrt(r3*r3 + g3*g3 + b3*b3))

        r4 = pixels_old[i+1,j+1][0]
        g4 = pixels_old[i+1,j+1][1]
        b4 = pixels_old[i+1,j+1][2]
        val4 = (int)(math.sqrt(r4*r4 + g4*g4 + b4*b4))

        stroke1 = abs(val1-val3)+abs(val2-val4)
        stroke2 = abs(val1-val2)+abs(val3-val4)
        stroke3 = abs(val1-val4)+abs(val2-val3)

        if(stroke1>=stroke2 and stroke1>=stroke3):
            pixels_new[i,j]=(255*(val1>=val3+sensitivity),255*(val1>=val3+sensitivity),255*(val1>=val3+sensitivity))
            pixels_new[i,j+1]=(255*(val3>=val1+sensitivity),255*(val3>=val1+sensitivity),255*(val3>=val1+sensitivity))
            pixels_new[i+1,j]=(255*(val2>=val4+sensitivity),255*(val2>=val4+sensitivity),255*(val2>=val4+sensitivity))
            pixels_new[i+1,j+1]=(255*(val4>=val2+sensitivity),255*(val4>=val2+sensitivity),255*(val4>=val2+sensitivity))
        elif(stroke2>=stroke1 and stroke2>=stroke3):
            pixels_new[i,j]=(255*(val1>=val2+sensitivity),255*(val1>=val2+sensitivity),255*(val1>=val2+sensitivity))
            pixels_new[i+1,j]=(255*(val2>=val1+sensitivity),255*(val2>=val1+sensitivity),255*(val2>=val1+sensitivity))
            pixels_new[i,j+1]=(255*(val3>=val4+sensitivity),255*(val3>=val4+sensitivity),255*(val3>=val4+sensitivity))
            pixels_new[i+1,j+1]=(255*(val4>=val3+sensitivity),255*(val4>=val3+sensitivity),255*(val4>=val3+sensitivity))
        else:
            pixels_new[i,j]=(255*(val1>=val4+sensitivity),255*(val1>=val4+sensitivity),255*(val1>=val4+sensitivity))
            pixels_new[i+1,j+1]=(255*(val4>=val1+sensitivity),255*(val4>=val1+sensitivity),255*(val4>=val1+sensitivity))
            pixels_new[i,j+1]=(255*(val3>=val2+sensitivity),255*(val3>=val2+sensitivity),255*(val3>=val2+sensitivity))
            pixels_new[i+1,j]=(255*(val2>=val3+sensitivity),255*(val2>=val3+sensitivity),255*(val2>=val3+sensitivity))

new_image.save("new_image.jpg")
