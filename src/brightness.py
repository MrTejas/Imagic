from PIL import Image
from IPython.display import display
from random import random
import math

# program to change brightness on an image

filename = "landscape.jpg"
image = Image.open(filename)
[width,height] = image.size 
new_image = Image.new( 'RGB', (width,height), "black") 

pixels_old = image.load()
pixels_new = new_image.load() # creates the pixel map

# defines the percentage increase in brightness of the image
percent = 5

for i in range(new_image.size[0]):    
    for j in range(new_image.size[1]):  
        r = pixels_old[i,j][0]
        g = pixels_old[i,j][1]
        b = pixels_old[i,j][2]
        
        red = int(r+255*percent/100.0)
        green = int(g+255*percent/100.0)
        blue = int(b+255*percent/100.0)

        pixels_new[i,j] = (red,green,blue)

new_image.save("new_image.jpg")