# -*- coding: utf-8 -*-
#QrCodeUtil
import qrcode
from PIL import Image,ImageFont, ImageDraw
import qrcode
import zxing    #导入解析包
import random,os
import io

# 参数含义：

# version：值为1~40的整数，控制二维码的大小（最小值是1，是个12×12的矩阵）。 如果想让程序自动确定，将值设置为 None 并使用 fit 参数即可。
# error_correction：控制二维码的错误纠正功能。可取值下列4个常量。
# ERROR_CORRECT_L：大约7%或更少的错误能被纠正。
# ERROR_CORRECT_M（默认）：大约15%或更少的错误能被纠正。
# ROR_CORRECT_H：大约30%或更少的错误能被纠正。
# box_size：控制二维码中每个小格子包含的像素数。
# border：控制边框（二维码与图片边界的距离）包含的格子数（默认为4，是相关标准规定的最小值）。
# img.save：是将生成二维码图片保存到哪里。

# 参考文档：

# http://www.xuchanggang.cn/archives/1069.html

# http://www.cnblogs.com/linjiqin/p/4140455.html

# http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/00140767171357714f87a053a824ffd811d98a83b58ec13000

# 官网及参考手册

# http://pythonware.com/products/pil/

# http://effbot.org/imagingbook/

# 在当前目录生成临时文件，规避java的路径问题
def ocr_qrcode_zxing(filename):
    zx = zxing.BarCodeReader()      #调用zxing二维码读取包
    data = ''
    zxdata = zx.decode(filename)    #图片解码
    if zxdata:
        data = zxdata
    return data.raw    #返回记录的内容

def createQrcode(data,text=None,returnBytes = True,iconFileName=None,filename = None,level = 8,box_size=8,border=4):
    qr = qrcode.QRCode(version=level,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=box_size,border=border)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image()
    img = img.convert("RGBA")
    img_w,img_h = img.size
    factor = 4
    size_w = int(img_w / factor)
    size_h = int(img_h / factor)
    if iconFileName:
        icon = Image.open(iconFileName)
        icon_w,icon_h = icon.size
        if icon_w >size_w:
            icon_w = size_w
        if icon_h > size_h:
            icon_h = size_h
        icon = icon.resize((icon_w,icon_h),Image.ANTIALIAS)
        w = int((img_w - icon_w)/2)
        h = int((img_h - icon_h)/2)
        icon = icon.convert("RGBA")
        img.paste((255,255,255),(w,h,icon_w+w,icon_h+h))
        img.paste(icon,(w,h),icon)
    if text:
        draw = ImageDraw.Draw(img)
        
        self.font = ImageFont.truetype("3.ttf",50)
        offsetx,offsety=self.font.getoffset(text)
        width,height=self.font.getsize(text)

        draw.text((0,img_h-border), 'smile', fill = (255, 0 ,0)) #利用ImageDraw的内置函数，在图片上写入文字
    if filename:
        img.save(filename,"png")
    if returnBytes:
        imgByteArr = io.BytesIO()
        img.save(imgByteArr, format='PNG')
        imgByteArr = imgByteArr.getvalue()
        return imgByteArr
    else:
        return
if __name__ == '__main__':
    workPath = "D:/pythonWorkSpaces/pythonlib/MyPythonLib/Util/datas"
    os.chdir(workPath)
    createQrcode("1234","hello",filename="hello.png")