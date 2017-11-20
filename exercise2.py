from PIL import Image
import numpy as np

n=4
m=5
im1=Image.open("spongebob.png")
im2=Image.open("spongebob2.png")
im3=Image.open("spongebob3.png")

def LSH(im,n,m):
    #greyscale the images
    im=im.convert("L")
    #resize
    im=im.resize((n,m))
    im_array=np.array(im)
    #compare adjacent values
    comparison=np.zeros((m,n),dtype=bool)
    for i in range(m):
        for j in range(n-1):
            if im_array[i,j]>im_array[i,j+1]:
                comparison[i,j]=True
            else:
                comparison[i,j]=False
    h=hash(comparison.tostring())
    return(h)

h1=LSH(im1,n,m)
h2=LSH(im2,n,m)
h3=LSH(im3,n,m)

print(h1)
print(h2)
print(h3)

