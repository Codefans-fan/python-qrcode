# -*- coding: utf-8 -*-
'''
Created on Mar 30, 2016

@author: fky
'''
from PIL import Image
from PIL import ImageDraw
from qrcode import QRCode




if __name__=='__main__':
    qr = QRCode(1)
    qr.add_data('fuck you')
    img = qr.make_image(fill_color='transparent')
    img_temp = Image.open('template.jpg')
    re_img = img_temp.resize((290,290),Image.ANTIALIAS)
    pixels = img.load()
    re_pixels = re_img.load()
    draw = ImageDraw.Draw(img)
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            if pixels[i,j][3] > 0:
                continue
            draw.point((i,j),(re_pixels[i,j][0],re_pixels[i,j][1],re_pixels[i,j][2],170))
    img.save('ll.png')
    


