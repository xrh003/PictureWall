# -*- coding: cp936 -*-
from PIL import Image
import os,sys
import fileName


picMatrix = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,1,1,1,1,1,0,0,1,1,1,1,1,0,0,1,1,1,1,1,0],
    [0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,1,0],
    [0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,1,0],
    [0,1,1,1,1,1,0,0,1,1,1,1,1,0,0,1,0,0,0,1,0],
    [0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,1,0,0,0,1,0],
    [0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,1,0,0,0,1,0],
    [0,1,1,1,1,1,0,0,1,1,1,1,1,0,0,1,1,1,1,1,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
]

w = len(picMatrix[0])
h = len(picMatrix)

mw = 100

path="./myPicture/"

toImage = Image.new('RGBA', (100 * w, 100 * (h + 1)))


def save_photo_wall():
    imgIndex = 0
    needImgNum = 0
    
    for y in range(h):
        for x in range(w):
            try:
                if picMatrix[y][x] == 1:
                    needImgNum = needImgNum + 1
                    filePath = path + "%s.jpg" % str(needImgNum)
                    fromImage = Image.open(filePath)
                    fromImage = fromImage.resize((100, 100), Image.ANTIALIAS)
                    toImage.paste(fromImage, (x * mw, y * mw))
                    imgIndex = imgIndex + 1
                else:
                    pass
            except IOError:
                pass
    print('Total images: %s' % needImgNum)

    toImage.show()
    toImage.save('./picturWall.png')

if __name__ == '__main__':
    fileName.fileRename_()
    fileName.fileRename()
    save_photo_wall()
