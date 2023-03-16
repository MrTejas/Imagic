from PIL import Image
from IPython.display import display
from random import random

# program to apply negative effect on an image

filename = "landscape.jpg"
image = Image.open(filename)
[width,height] = image.size 
new_image = Image.new( 'RGB', (width,height), "black") 

pixels_old = image.load()
pixels_new = new_image.load() # creates the pixel map

for i in range(new_image.size[0]):    
    for j in range(new_image.size[1]):  
        red = (int)(255-pixels_old[i,j][0])
        green = (int)(255-pixels_old[i,j][1])
        blue = (int)(255-pixels_old[i,j][2])

        pixels_new[i,j] = (red,green,blue)

new_image.save("new_image.jpg")