#encoding:utf-8
from PIL import Image,ImageFont,ImageDraw,ImageFilter
import random
def getImage():
    gm=Image.new('RGB',(100,30),"white") #生成一个面板，指定宽高，颜色

    font=ImageFont.truetype("simsun",20)

    draw=ImageDraw.Draw(gm)

    str="qwery456tutyuy0123uiupsadsadffjhk789"

    str1=""
    for i in range(5):
        c=str[random.randrange(0,str.__len__()-1)]
        str1+=c
        draw.text((i*20,0),text=c,fill="red",font=font)

    for i in range(4):
        y1=random.randint(0,30)
        y2=random.randint(0,30)
        draw.line(((0,y1),(100,y2)),fill="red",width=2)
    return gm,str1






