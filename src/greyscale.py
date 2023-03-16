from PIL import Image
from IPython.display import display
from random import random
import math


# program to apply black and white effect on an image

filename = "landscape.jpg"
image = Image.open(filename)
[width,height] = image.size 
new_image = Image.new( 'RGB', (width,height), "black") 

pixels_old = image.load()
pixels_new = new_image.load() # creates the pixel map

val = int(random()*255)

for i in range(new_image.size[0]):    
    for j in range(new_image.size[1]):  
        r = pixels_old[i,j][0]
        g = pixels_old[i,j][1]
        b = pixels_old[i,j][2]

        val = (int)(math.sqrt(r*r + g*g + b*b))

        pixels_new[i,j] = (val,val,val)

new_image.save("new_image.jpg")