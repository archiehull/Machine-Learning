import matplotlib.pyplot as plt
import numpy as np
import os
import random
import matplotlib.pyplot as plt
from PIL import Image

#init image database path
db_path='./triple_mnist/'


#randomise the set the image is taken from
set_type=random.randint(1,3)
if(set_type==3):
    db_set='val/'
elif(set_type==2):
    db_set='train/'
elif(set_type==1):
    db_set='test/'

#combine set with db path
db_path=db_path+db_set

#create list of all subfolders in set
sub_folders=os.listdir(db_path)

#init images array
imgs=[]


for i in range(5):
    #select random subfolder and get pathname
    subfolder=random.choice(sub_folders)
    subfolder_path = os.path.join(db_path, subfolder)

    #select random image and get pathname
    img=random.choice(os.listdir(subfolder_path))
    img_path=os.path.join(subfolder_path, img)

    #open image and add to array
    img=Image.open(img_path)
    imgs.append((img, subfolder))


#display images using matplotlib
plt.figure(figsize=(10, 5))
for i, (image, label) in enumerate(imgs, start=1):
    plt.subplot(1, len(imgs), i)
    plt.imshow(image, cmap='gray')
    plt.title(f'Label: {label}')
    plt.axis('off')
plt.show()
