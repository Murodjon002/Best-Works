import matplotlib.pyplot as plt
import numpy as np
import cv2
plt.figure(figsize=(10,6),dpi=100)
k=1
for i in range(1,7):
    file=open(f"Labels/{i}.txt")
    img=cv2.imread(f"{i}.jpg")
    img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    H,W=img.shape[:2]
    for i in file:
        i=i.split()
        
        x=float(i[1])*W
        y=float(i[2])*H
        w=float(i[3])*W
        h=float(i[4])*H
        x1=int(x-w/2)
        x2=int(x+w/2)
        y1=int(y-h/2)
        y2=int(y+h/2)
        img=cv2.rectangle(img,(x1,y1),(x2,y2),(255,0,0),2)
    img=cv2.resize(img,(600,600))
    plt.subplot(2,3,k)
    plt.imshow(img)
    plt.axis("off")
    k+=1
 
plt.show()