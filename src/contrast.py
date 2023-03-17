from PIL import Image
from IPython.display import display
from random import random
import math


# program to change contrast of an image

filename = "landscape.jpg"
image = Image.open(filename)
[width,height] = image.size 
new_image = Image.new( 'RGB', (width,height), "black") 

pixels_old = image.load()
pixels_new = new_image.load() # creates the pixel map

# desired contrast and corresponding contrast correction factor
contrast = 100
ccf = (259*(255+contrast))/(float(255*(259-contrast)))

print("Contrast Desired : "+str(contrast))
print("Contrast Correction Factor : "+str(ccf))


for i in range(new_image.size[0]):    
    for j in range(new_image.size[1]):  
        (r,g,b) = pixels_old[i,j]

        red = int(ccf*(r-128)+128)
        green = int(ccf*(g-128)+128)
        blue = int(ccf*(b-128)+128)

        pixels_new[i,j] = (red,green,blue)

new_image.save("new_image.jpg")