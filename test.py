from PIL import Image
import os
img = Image.open(r"sup.jpg")  
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

for x in range(0,m,2):
    for y in range(0,n,2):
        d1 = px[x,y]
        d2 = px[x+1,y]
        d3 = px[x+1,y+1]
        d4 = px[x,y+1]
        
        ra = (int)((d1[0]+d2[0]+d3[0]+d4[0])/4)
        ga = (int)((d1[1]+d2[1]+d3[1]+d4[1])/4)
        ba = (int)((d1[2]+d2[2]+d3[2]+d4[2])/4)
        
        px[x,y] = (ra,ga,ba)
        px[x+1,y] = (ra,ga,ba)
        px[x+1,y+1] = (ra,ga,ba)
        px[x,y+1] = (ra,ga,ba)
          

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