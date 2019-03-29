#coding:utf-8
import random
import os
from PIL import Image , ImageDraw , ImageFont , ImageFilter#图像，绘画，字体，模糊度
def fontdate():
    a = os.listdir("c:/Windows/Fonts")
    arr = []
    for value in a:
        b = os.path.splitext(value)
        if b[1] == ".TTF" or b[1] == ".ttf":
            arr.append(value)
    fontTTF = random.randint(0, len(arr))
    date = arr[fontTTF]
    return date
def fontfamily():
    return chr(random.randint(65 , 90))
def fontcol():
    return (random.randint(100,255) , random.randint(100,255) , random.randint(100,255))
def backcol():
    return (random.randint(0,150) , random.randint(0,150) , random.randint(0,150))

width = 80 * 5
height = 80
arr = []
image = Image.new("RGB" , (width , height) , backcol())
draw = ImageDraw.Draw(image)
for num in range(5):
    font = ImageFont.truetype(os.path.join("c:\\Windows\\Fonts", fontdate()), 36)
    value = fontfamily()
    arr.append(value)
    draw.text((80 * num + 10 , 10) , value , font = font , fill = fontcol())
image = image.filter(ImageFilter.BLUR)

image.save(os.path.join(os.path.abspath('..'), 'static\\Verification\\verification.png'), "png")
print(arr)
print(os.path.join(os.path.abspath('..'), 'static\\Verification\\verification.png'))

'''
from PIL import Image
im = Image.open("E:/table.jpg")
w,h = im.size
#mm = im.resize((w * 2 , h * 3))#放大操作，resize函数会返回一个数值，所以要用变量接收，该函数是不等比例放大，参数必须是整数，不能为小数
#mm.save("e:/table2.jpg")
im.thumbnail((w * 0.5 , h * 0.3))#缩小操作，该函数参数不能大于1，小于0
im.save("e:/table3.jpg")
'''
