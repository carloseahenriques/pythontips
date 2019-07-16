#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import time
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

Sample=time.strftime("%Y%m%d-%I:%M:%S")

img = Image.open("sample_in.jpg")
draw = ImageDraw.Draw(img)
# font = ImageFont.truetype(<font-file>, <font-size>)
font = ImageFont.truetype("DejaVuSansMono.ttf", 12)
# draw.text((x, y),"Sample Text",(r,g,b))
draw.rectangle(xy=[(5,5), (100,20)], fill=(255,255,120))
draw.text((5, 5), Sample, (100,255,0), font=font)
img.save('sample-out.jpg')
