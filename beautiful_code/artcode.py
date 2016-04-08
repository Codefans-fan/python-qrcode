# -*- coding: utf-8 -*-
'''
Created on Apr 8, 2016

@author: fky
'''
import qrcode
from PIL import Image
from PIL import ImageDraw

class ArtCode(qrcode.QRCode):
    def __init__(self,back_img=None,transparent=100,version=1):
        super().__init__(version=version)
        self.transparent=transparent
        try:
            self.back_img = Image.open(back_img)
        except Exception as e:
            print(e)
        
    def make_image(self, image_factory=None, **kwargs):
        img = super().make_image(image_factory=image_factory, fill_color='transparent')
        re_img = self.back_img.resize(img.size,Image.ANTIALIAS)
        pixels = img.load()
        re_pixels = re_img.load()
        draw = ImageDraw.Draw(img)
        for i in range(img.size[0]):
            for j in range(img.size[1]):
                if pixels[i,j][3] > 0:
                    continue
                draw.point((i,j),(re_pixels[i,j][0],re_pixels[i,j][1],re_pixels[i,j][2],self.transparent))
        return img


if __name__=='__main__':
    qr = ArtCode('template.jpg')
    qr.add_data('fuck')
    img = qr.make_image()
    img.save('xx.png')
    