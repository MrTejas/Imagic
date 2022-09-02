from turtle import end_fill
from PIL import Image
import os
img = Image.open(r"flower.jpg")  
px = img.load()


name = img.filename
l = len(name)
cname = name[0:(l-4)]+"_compressed.jpg"

k=1

# print(px[4,4])
# print(img.size)
# print(img.mode)

m = img.size[0]
n = img.size[1]
    
m =  m - (m%4)
n = n - (n%4)


# Y = [[0 for x in range(m)] for y in range(n)] # luminance matrix

# Cr = [[0 for x in range(m)] for y in range(n)] # red chrominance matrix
# Cb = [[0 for x in range(m)] for y in range(n)] # blue chrominance matrix

Y = [0] * m
for i in range(m):
    Y[i] = [0] * n


Cr = [0] * m
for i in range(m):
    Cr[i] = [0] * n


Cb = [0] * m
for i in range(m):
    Cb[i] = [0] * n



for x in range(0,m,1):
    for y in range(0,n,1):
        
        r = px[x,y][0]
        g = px[x,y][1]
        b = px[x,y][2]
        
        Y[x][y] = (int)(0.299*r + 0.587*g + 0.114*b)
        Cb[x][y] = (int)(-0.1687*r -0.3313*g + 0.5*b + 128)
        Cr[x][y] = (int)(0.5*r - 0.4187*g -0.0813*b + 128)
        
        
ccname = "enc_"+cname[0:(len(cname)-4)]+".txt"
f = open(ccname,"a")



for x in range(0,m,2):
    for y in range(0,n,2):
        d1 = Cr[x][y]
        d2 = Cr[x+1][y]
        d3 = Cr[x+1][y+1]
        d4 = Cr[x][y+1]
        
        e1 = Cb[x][y]
        e2 = Cb[x+1][y]
        e3 = Cb[x+1][y+1]
        e4 = Cb[x][y+1]
        
        d = (int)((d1+d2+d3+d4)/4)
        e = (int)((e1+e2+e3+e4)/4)
        
        Cr[x][y]=Cr[x+1][y]=Cr[x+1][y+1]=Cr[x][y+1]=d
        Cb[x][y]=Cb[x+1][y]=Cb[x+1][y+1]=Cb[x][y+1]=e
        
for x in range(0,m,2):
    for y in range(0,n,2):
        f.write(str(Cr[x][y]))

for x in range(0,m,2):
    for y in range(0,n,2):
        f.write(str(Cb[x][y]))
        
        
        
        
        
        
        

        



# img.show()
img.save(cname)
print("Original Size : \t"+str(os.path.getsize(name))+ " bytes")
print("Compressed Size : \t"+str(os.path.getsize(cname))+ " bytes")
ratio = os.path.getsize(cname)/(float)(os.path.getsize(name))
print("comperssion ratio : \t "+str(ratio))
    


# size = (64*5,96*5)

# r_img = img.resize(size)
# r_img.save("r_img.jpg")
# r_img.show()