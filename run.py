from PIL import Image
import glob, os, math, time, shutil
# Clear existed files
os.system("rm -rf export/ && mkdir export/")

filelist = [file for file in os.listdir('images') if file.endswith('.png')]
# Pasting
for img in filelist:
    image = Image.open('blank128.png')
    logo = Image.open('images/'+ img)
    image_copy = image.copy()
    position = (1, 74)
    image_copy.paste(logo, position)
    image_copy.save(img)
    shutil.move(img, 'export/')

import sprite