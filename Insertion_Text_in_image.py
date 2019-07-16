#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

img = Image.open("sample_in.jpg")
draw = ImageDraw.Draw(img)
# font = ImageFont.truetype(<font-file>, <font-size>)
font = ImageFont.truetype("DejaVuSansMono.ttf", 10)
# draw.text((x, y),"Sample Text",(r,g,b))
draw.text((5, 5),"Sample Text",(255,0,0),font=font)
img.save('sample-out.jpg')
