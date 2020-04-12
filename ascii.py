# -*- coding=utf-8 -*-

from PIL import Image
import argparse

#命令行输入参数处理,构建命令行输入参数处理实例
parser = argparse.ArgumentParser()

parser.add_argument('file')     #输入文件
parser.add_argument('-o', '--output')   #输出文件
parser.add_argument('--width', type = int, default = 80) #输出字符画宽
parser.add_argument('--height', type = int, default = 80) #输出字符画高

#获取参数
args = parser.parse_args()

IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

# 将256灰度映射到70个字符上
def get_char(r,g,b,alpha = 256):
#判断 alpha 值
    if alpha == 0:
        return ' '
#获取字符集的长度
    length = len(ascii_char)
#RGB转为灰度，范围0-255
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    unit = (256.0 + 1)/length
    return ascii_char[int(gray/unit)]

#import 不会调用的部分
if __name__ == '__main__':

    im = Image.open(IMG)
    im = im.resize((WIDTH,HEIGHT), Image.NEAREST)

    txt = ""
#遍历行
    for i in range(HEIGHT):
#遍历列
        for j in range(WIDTH):
#获取（j，i）字符串
            txt += get_char(*im.getpixel((j,i)))
        txt += '\n'

    print(txt)
    
    #字符画输出到文件
    if OUTPUT:
        with open(OUTPUT,'w') as f:
            f.write(txt)
    else:
        with open("output.txt",'w') as f:
            f.write(txt)
